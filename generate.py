from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta

WIDTH = 1170
HEIGHT = 2532

BACKGROUND = (0, 0, 0)
TEXT = (170, 170, 170)

font = ImageFont.truetype("fonts/genshin_font.ttf", 48)

today = datetime.now() + timedelta(hours=5, minutes=30)

text = today.strftime("%A\n%d %B %Y")

img = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
draw = ImageDraw.Draw(img)

bbox = draw.multiline_textbbox(
    (0, 0),
    text,
    font=font,
    align="center",
    spacing=20,
)

text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]

x = (WIDTH - text_width) / 2
y = (HEIGHT - text_height) / 2

draw.multiline_text(
    (x, y),
    text,
    fill=TEXT,
    font=font,
    align="center",
    spacing=20,
)

img.save("output/wallpaper.png")
