from PIL import Image

def embed_msb_visual(input_image, output_image, secret):
    img = Image.open(input_image).convert("RGB")
    pixels = img.load()
    width, height = img.size

    # Convert secret → bits
    secret_bits = "".join(format(b, "08b") for b in secret.encode())
    secret_bits += "1111111111111110"  # end marker

    # Repeat the bitstream to cover a large area
    repeated_bits = (secret_bits * 500)  # repeat many times
    bit_len = len(repeated_bits)

    print(f"[+] Total bits to embed: {bit_len}")

    bit_idx = 0

    # Define a large region (40% x 40% of the image)
    region_w = int(width * 0.5)
    region_h = int(height * 0.5)

    print(f"[+] Embedding region: {region_w} x {region_h}")

    for y in range(region_h):
        for x in range(region_w):

            bit = repeated_bits[bit_idx % bit_len]
            bit_idx += 1

            r, g, b = pixels[x, y]

            r_bin = bit + format(r, "08b")[1:]
            g_bin = bit + format(g, "08b")[1:]
            b_bin = bit + format(b, "08b")[1:]

            pixels[x, y] = (int(r_bin, 2), int(g_bin, 2), int(b_bin, 2))

    img.save(output_image, "PNG")
    print("[+] MSB embedded with STRONG visual distortion")
    print(f"[+] Output saved as: {output_image}")


# =======================
FLAG = "ISC2CTF{MSB_SteG4N0_t35T1ng}"
embed_msb_visual("rocks.png", "visual_msb.png", FLAG)
