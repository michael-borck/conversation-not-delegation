#!/usr/bin/env python3
"""
Generate a KDP ebook cover for 'Conversation, Not Delegation'.

Output: images/cover.png (2560 x 1600 px, KDP ebook standard)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# Dimensions
WIDTH = 2560
HEIGHT = 1600

# Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
COMIC_PATH = PROJECT_ROOT / "images" / "comic-strip" / "00-conversation-not-delegation.png"
OUTPUT_PATH = PROJECT_ROOT / "images" / "cover.png"

# Colours
BG_COLOUR = (255, 255, 255)
TITLE_COLOUR = (20, 20, 20)
SUBTITLE_COLOUR = (80, 80, 80)
AUTHOR_COLOUR = (100, 100, 100)


def get_font(size, bold=False):
    """Try to load a clean system font, fall back to default."""
    font_paths = [
        # macOS
        "/System/Library/Fonts/Helvetica.ttc",
        "/System/Library/Fonts/SFNSDisplay.ttf",
        "/Library/Fonts/Arial.ttf",
        # Linux
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ]
    bold_paths = [
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial Bold.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    ]
    paths = bold_paths if bold else font_paths
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


def main():
    # Create canvas
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_COLOUR)
    draw = ImageDraw.Draw(img)

    # Fonts
    title_font = get_font(120, bold=True)
    subtitle_font = get_font(56)
    author_font = get_font(48)

    # Title
    title = "Conversation, Not Delegation"
    tx = (WIDTH - text_width(draw, title, title_font)) // 2
    draw.text((tx, 80), title, fill=TITLE_COLOUR, font=title_font)

    # Subtitle
    subtitle = "How to Think With AI, Not Just Use It"
    sx = (WIDTH - text_width(draw, subtitle, subtitle_font)) // 2
    draw.text((sx, 220), subtitle, fill=SUBTITLE_COLOUR, font=subtitle_font)

    # Comic strip
    comic = Image.open(COMIC_PATH)
    # Convert to RGB if RGBA (for white background)
    if comic.mode == "RGBA":
        bg = Image.new("RGB", comic.size, BG_COLOUR)
        bg.paste(comic, mask=comic.split()[3])
        comic = bg

    # Scale comic to fit width with padding
    max_comic_width = WIDTH - 200
    max_comic_height = HEIGHT - 500
    ratio = min(max_comic_width / comic.width, max_comic_height / comic.height)
    new_size = (int(comic.width * ratio), int(comic.height * ratio))
    comic = comic.resize(new_size, Image.LANCZOS)

    # Centre comic vertically in available space
    comic_x = (WIDTH - comic.width) // 2
    comic_y = 320 + (max_comic_height - comic.height) // 2
    img.paste(comic, (comic_x, comic_y))

    # Author
    author = "Michael Borck"
    ax = (WIDTH - text_width(draw, author, author_font)) // 2
    draw.text((ax, HEIGHT - 100), author, fill=AUTHOR_COLOUR, font=author_font)

    # Save
    img.save(OUTPUT_PATH, "PNG", dpi=(300, 300))
    print(f"Cover saved to: {OUTPUT_PATH}")
    print(f"Dimensions: {WIDTH} x {HEIGHT} px")


if __name__ == "__main__":
    main()
