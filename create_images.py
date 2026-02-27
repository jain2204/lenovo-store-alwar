#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('images/products', exist_ok=True)

width, height = 800, 600
products = {
    'thinkpad.jpg': ('ThinkPad', '#2B2B2B', '#E2231A'),
    'legion.jpg': ('Legion', '#4A0000', '#FFD700'),
    'yoga.jpg': ('Yoga', '#663399', '#87CEEB'),
    'ideapad.jpg': ('IdeaPad', '#1E40AF', '#90EE90'),
    'tablet.jpg': ('Tablets', '#228B22', '#FFB6C1'),
    'hero-thinkpad.jpg': ('ThinkPad Pro', '#1a1a1a', '#D3D3D3'),
}

for filename, (product_name, text_color, bg_color) in products.items():
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    text_rgb = tuple(int(text_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    draw.rectangle([(10, 10), (width-10, height-10)], outline=text_rgb, width=3)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 72)
    except:
        font = ImageFont.load_default()
    text = f"Lenovo {product_name}"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (width - text_w) // 2
    y = (height - text_h) // 2
    draw.text((x, y), text, fill=text_rgb, font=font)
    filepath = f'images/products/{filename}'
    img.save(filepath)
    print(f'Created {filepath}')
