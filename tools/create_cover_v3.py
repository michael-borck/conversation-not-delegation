#!/usr/bin/env python3
"""
Generate KDP ebook cover for 'Conversation, Not Delegation'.

White background, Comic Sans title (leaning into the comic aesthetic),
tightly cropped comic panel filling more of the space.

Output: images/cover-v3.png (1800 x 2700 px, 300 DPI at 6x9 print)
"""

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

WIDTH = 1800
HEIGHT = 2700

PROJECT_ROOT = Path(__file__).resolve().parent.parent
COMIC_PATH = PROJECT_ROOT / "images" / "comic-strip" / "00-panel1.png"
OUTPUT_PATH = PROJECT_ROOT / "images" / "cover-v3.png"

BG = (255, 255, 255)
TITLE_COLOUR = (20, 20, 20)
SUBTITLE_COLOUR = (80, 80, 80)
AUTHOR_COLOUR = (100, 100, 100)


def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def text_width(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0]


def text_height(draw, text, font):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[3] - bbox[1]


def main():
    img = Image.new("RGB", (WIDTH, HEIGHT), BG)
    draw = ImageDraw.Draw(img)

    # Fonts
    comic_bold = "/System/Library/Fonts/Supplemental/Comic Sans MS Bold.ttf"
    comic_reg = "/System/Library/Fonts/Supplemental/Comic Sans MS.ttf"
    system_font = "/System/Library/Fonts/Helvetica.ttc"

    title_font = load_font(comic_bold, 158)
    subtitle_font = load_font(comic_reg, 54)
    author_font = load_font(comic_reg, 158)

    # Title — big, bold, Comic Sans, owning it
    y = 180
    for line in ["Conversation,", "Not Delegation"]:
        w = text_width(draw, line, title_font)
        draw.text(((WIDTH - w) // 2, y), line, fill=TITLE_COLOUR, font=title_font)
        y += 190

    # Subtitle — clean system font for contrast
    subtitle = "How to Think With AI, Not Just Use It"
    sw = text_width(draw, subtitle, subtitle_font)
    draw.text(((WIDTH - sw) // 2, y + 20), subtitle, fill=SUBTITLE_COLOUR, font=subtitle_font)

    # Comic panel — load and crop tightly
    comic = Image.open(COMIC_PATH).convert("RGBA")

    # Auto-crop whitespace from the comic
    # Convert to grayscale, find non-white bounds
    gray = comic.convert("L")
    bbox = gray.point(lambda x: 0 if x > 240 else 255).getbbox()
    if bbox:
        comic = comic.crop(bbox)

    # Scale comic to fill most of the available space
    comic_top = y + 100
    comic_bottom = HEIGHT - 280
    available_h = comic_bottom - comic_top
    available_w = WIDTH - 120

    ratio = min(available_w / comic.width, available_h / comic.height)
    new_w = int(comic.width * ratio)
    new_h = int(comic.height * ratio)
    comic = comic.resize((new_w, new_h), Image.LANCZOS)

    # Paste comic with white background
    comic_x = (WIDTH - new_w) // 2
    comic_y = comic_top + 20  # positioned just below subtitle with breathing room

    comic_bg = Image.new("RGB", (new_w, new_h), BG)
    if comic.mode == "RGBA":
        comic_bg.paste(comic, mask=comic.split()[3])
    else:
        comic_bg.paste(comic)
    img.paste(comic_bg, (comic_x, comic_y))

    # Author — at the bottom
    author = "Michael Borck"
    aw = text_width(draw, author, author_font)
    draw.text(((WIDTH - aw) // 2, HEIGHT - 250), author, fill=AUTHOR_COLOUR, font=author_font)

    # Save
    img.save(OUTPUT_PATH, "PNG", dpi=(300, 300))
    print(f"Cover saved to: {OUTPUT_PATH}")
    print(f"Dimensions: {WIDTH} x {HEIGHT} px")


if __name__ == "__main__":
    main()
