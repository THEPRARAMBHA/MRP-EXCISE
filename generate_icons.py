"""
Generate PWA icons from logo-source.png using Pillow.
Pillow is pre-installed on GitHub Actions ubuntu-latest runners.
"""
import os
from PIL import Image

# Load the source logo
src = Image.open("logo-source.png").convert("RGBA")

# Create icons/ folder
os.makedirs("icons", exist_ok=True)

# Generate all required PWA icon sizes
sizes = [72, 96, 128, 144, 152, 192, 384, 512]
for s in sizes:
    # Use LANCZOS for high-quality downsampling
    img = src.copy()
    img.thumbnail((s, s), Image.LANCZOS)
    # Create a square canvas with white background
    canvas = Image.new("RGBA", (s, s), (255, 255, 255, 255))
    # Center the logo on the canvas
    offset = ((s - img.width) // 2, (s - img.height) // 2)
    canvas.paste(img, offset, img)
    # Save as PNG
    canvas.save(f"icons/icon-{s}.png", "PNG")
    print(f"Created icons/icon-{s}.png ({s}x{s})")

# Maskable icon (512x512, full-bleed with padding)
img = src.copy()
canvas = Image.new("RGBA", (512, 512), (255, 255, 255, 255))
# For maskable, use 80% of space (safe zone)
safe = int(512 * 0.8)
img.thumbnail((safe, safe), Image.LANCZOS)
offset = ((512 - img.width) // 2, (512 - img.height) // 2)
canvas.paste(img, offset, img)
canvas.save("icons/icon-512-maskable.png", "PNG")
print("Created icons/icon-512-maskable.png")

# Screenshot for PWA listing (use 512x512 version)
os.makedirs("screenshots", exist_ok=True)
canvas_sc = Image.new("RGBA", (1080, 1920), (17, 17, 17, 255))
logo_sc = src.copy()
logo_sc.thumbnail((600, 600), Image.LANCZOS)
offset_sc = ((1080 - logo_sc.width) // 2, (1920 - logo_sc.height) // 2)
canvas_sc.paste(logo_sc, offset_sc, logo_sc)
canvas_sc.save("screenshots/screen1.png", "PNG")
print("Created screenshots/screen1.png")

print("All icons generated successfully from logo-source.png!")
