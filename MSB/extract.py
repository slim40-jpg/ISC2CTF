from PIL import Image

def extract_msb_visual(image_path):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()
    width, height = img.size

    region_w = int(width * 0.5)
    region_h = int(height * 0.5)

    bitstream = ""

    for y in range(region_h):
        for x in range(region_w):
            r, g, b = pixels[x, y]
            bitstream += format(r, "08b")[0]  # MSB of Red (redundant but stable)

    end_marker = "1111111111111110"
    pos = bitstream.find(end_marker)

    if pos == -1:
        return "[!] Marker not found"

    data_bits = bitstream[:pos]

    bytes_out = []
    for i in range(0, len(data_bits), 8):
        byte = data_bits[i:i+8]
        if len(byte) < 8:
            break
        bytes_out.append(int(byte, 2))

    return bytes(bytes_out).decode(errors="ignore")


# =====================
flag = extract_msb_visual("visual_msb.png")
print("[+] Extracted:", flag)
