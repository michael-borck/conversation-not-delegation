#!/usr/bin/env python3
"""
Generate a polished KDP ebook cover for 'Conversation, Not Delegation'.

Dark background, clean typography, comic panel with rounded frame.
Matches the borck.education brand aesthetic.

Output: images/cover-v2.png (1600 x 2560 px, KDP ebook standard portrait)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WIDTH = 1600
HEIGHT = 2560

PROJECT_ROOT = Path(__file__).resolve().parent.parent
COMIC_PATH = PROJECT_ROOT / "images" / "comic-strip" / "00-panel1.png"
OUTPUT_PATH = PROJECT_ROOT / "images" / "cover-v2.png"

# Colours — dark theme matching borck.education
BG_COLOUR = (10, 10, 11)           # --black
CARD_BG = (22, 22, 26)             # --gray-5
CARD_BORDER = (30, 30, 35)         # --gray-4 ish
ACCENT = (34, 197, 94)             # --accent green
ACCENT_DIM = (5, 46, 22)           # --accent-low
WHITE = (232, 230, 227)            # --white
GRAY_1 = (154, 154, 158)           # --gray-1
GRAY_2 = (94, 94, 99)             # --gray-2


def get_font(size, bold=False):
    """Try DM Sans first, then system fonts."""
    dm_sans_paths = [
        Path.home() / "Library/Fonts/DMSans-Bold.ttf",
        Path.home() / "Library/Fonts/DMSans-Regular.ttf",
        Path.home() / "Library/Fonts/DM_Sans/DMSans-Bold.ttf",
        Path.home() / "Library/Fonts/DM_Sans/DMSans-Regular.ttf",
    ]
    system_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    bold_system = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    ]

    # Try DM Sans first
    for p in dm_sans_paths:
        if p.exists():
            try:
                return ImageFont.truetype(str(p), size)
            except OSError:
                continue

    # Fall back to system fonts
    paths = bold_system if bold else system_paths
    for path in paths:
        if Path(path).exists():
            try:
                return ImageFont.truetype(path, size, index=1 if bold and path.endswith(".ttc") else 0)
            except (OSError, IndexError):
                try:
                    return ImageFont.truetype(path, size)
                except OSError:
                    continue
    return ImageFont.load_default()


def text_width(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def draw_rounded_rect(draw, xy, radius, fill=None, outline=None, width=1):
    """Draw a rounded rectangle."""
    x0, y0, x1, y1 = xy
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def main():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOUR)
    draw = ImageDraw.Draw(img)

    # Subtle radial glow behind the comic area
    glow = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOUR)
    glow_draw = ImageDraw.Draw(glow)
    cx, cy = WIDTH // 2, HEIGHT // 2 - 100
    for r in range(400, 0, -2):
        alpha = int(15 * (r / 400))
        colour = (ACCENT_DIM[0] + alpha, ACCENT_DIM[1] + alpha, ACCENT_DIM[2] + alpha)
        glow_draw.ellipse(
            [cx - r * 2, cy - r * 2, cx + r * 2, cy + r * 2],
            fill=colour
        )
    glow = glow.filter(ImageFilter.GaussianBlur(radius=80))
    img = Image.composite(glow, img, glow.convert("L"))
    draw = ImageDraw.Draw(img)

    # Fonts
    title_font = get_font(120, bold=True)
    subtitle_font = get_font(48)
    author_font = get_font(44)
    tag_font = get_font(28)

    # Top accent line
    line_y = 200
    line_w = 120
    draw.rounded_rectangle(
        [(WIDTH - line_w) // 2, line_y, (WIDTH + line_w) // 2, line_y + 4],
        radius=2, fill=ACCENT
    )

    # Title
    y = 260
    for line in ["Conversation,", "Not Delegation"]:
        w = text_width(draw, line, title_font)
        draw.text(((WIDTH - w) // 2, y), line, fill=WHITE, font=title_font)
        y += 140

    # Subtitle
    subtitle = "How to Think With AI, Not Just Use It"
    sw = text_width(draw, subtitle, subtitle_font)
    draw.text(((WIDTH - sw) // 2, y + 30), subtitle, fill=GRAY_1, font=subtitle_font)

    # Comic panel — framed in a card-style container
    comic = Image.open(COMIC_PATH).convert("RGBA")

    # Scale comic
    card_padding = 40
    card_margin = 120
    max_comic_w = WIDTH - (card_margin * 2) - (card_padding * 2)
    max_comic_h = 1100

    ratio = min(max_comic_w / comic.width, max_comic_h / comic.height)
    new_w = int(comic.width * ratio)
    new_h = int(comic.height * ratio)
    comic = comic.resize((new_w, new_h), Image.LANCZOS)

    # Card background
    card_x0 = (WIDTH - new_w - card_padding * 2) // 2
    card_y0 = 680
    card_x1 = card_x0 + new_w + card_padding * 2
    card_y1 = card_y0 + new_h + card_padding * 2

    draw_rounded_rect(draw, (card_x0, card_y0, card_x1, card_y1),
                      radius=20, fill=CARD_BG, outline=CARD_BORDER, width=2)

    # Paste comic (white background for the comic itself)
    comic_x = card_x0 + card_padding
    comic_y = card_y0 + card_padding

    # Create white background for comic area
    comic_bg = Image.new("RGB", (new_w, new_h), (255, 255, 255))
    if comic.mode == "RGBA":
        comic_bg.paste(comic, mask=comic.split()[3])
    else:
        comic_bg.paste(comic)
    img.paste(comic_bg, (comic_x, comic_y))

    # Accent tag below comic
    tag_text = "A methodology for thinking with AI"
    tw = text_width(draw, tag_text, tag_font)
    tag_pad_h = 12
    tag_pad_w = 24
    tag_x = (WIDTH - tw - tag_pad_w * 2) // 2
    tag_y = card_y1 + 40
    draw_rounded_rect(
        draw,
        (tag_x, tag_y, tag_x + tw + tag_pad_w * 2, tag_y + 28 + tag_pad_h * 2),
        radius=20, fill=ACCENT_DIM, outline=ACCENT, width=1
    )
    draw.text((tag_x + tag_pad_w, tag_y + tag_pad_h), tag_text, fill=ACCENT, font=tag_font)

    # Author
    author = "Michael Borck"
    aw = text_width(draw, author, author_font)
    draw.text(((WIDTH - aw) // 2, HEIGHT - 180), author, fill=GRAY_2, font=author_font)

    # Bottom accent line
    draw.rounded_rectangle(
        [(WIDTH - line_w) // 2, HEIGHT - 100, (WIDTH + line_w) // 2, HEIGHT - 96],
        radius=2, fill=ACCENT
    )

    # Save
    img.save(OUTPUT_PATH, "PNG", dpi=(300, 300))
    print(f"Cover saved to: {OUTPUT_PATH}")
    print(f"Dimensions: {WIDTH} x {HEIGHT} px")


if __name__ == "__main__":
    main()
