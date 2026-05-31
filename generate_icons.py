import os, struct, zlib

def create_icon(size):
    w = size
    bg = bytes([17, 17, 17, 255])
    fg = bytes([255, 255, 255, 255])
    data = [bytearray(bg * w) for _ in range(w)]
    def sp(x, y):
        if 0 <= x < w and 0 <= y < w:
            data[y][x*4:x*4+4] = fg
    pad = w // 6
    L = pad; R = w - pad - 1; T = pad; B = w - pad - 1
    th = max(w // 14, 2)
    mid = w // 2; midy = (T + B) // 2
    for y in range(T, B + 1):
        for t in range(th):
            sp(L + t, y)
            sp(R - t, y)
    for i in range(midy - T + th):
        f = i / max(1, midy - T)
        lx = L + round(f * (mid - L))
        rx = R - round(f * (R - mid))
        for t in range(th):
            sp(lx + t, T + i)
            sp(rx - t, T + i)
    def chunk(ct, d):
        c = ct + d
        return struct.pack(">I", len(d)) + c + struct.pack(">I", zlib.crc32(c) & 0xffffffff)
    ihdr = struct.pack(">IIBBBBB", w, w, 8, 6, 0, 0, 0)
    raw = b""
    for row in data:
        raw += b"\x00" + bytes(row)
    compressed = zlib.compress(raw, 6)
    return b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", compressed) + chunk(b"IEND", b"")

os.makedirs("icons", exist_ok=True)
for s in [72, 96, 128, 144, 152, 192, 384, 512]:
    with open(f"icons/icon-{s}.png", "wb") as f:
        f.write(create_icon(s))
    print(f"Created icons/icon-{s}.png")

with open("icons/icon-512-maskable.png", "wb") as f:
    f.write(create_icon(512))
print("Created icons/icon-512-maskable.png")

os.makedirs("screenshots", exist_ok=True)
with open("screenshots/screen1.png", "wb") as f:
    f.write(create_icon(512))
print("Created screenshots/screen1.png")
print("All icons created successfully!")
