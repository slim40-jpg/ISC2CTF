from PIL import Image

# =========================================================
# EDIT THIS WITH THE FLAG YOU WANT TO HIDE
FLAG = b"ISC2CTF{Cr15T1aN0_b35T_pL4y3r_1n_1hE_w0RlD_}"
# =========================================================


def embed_flag(input_image, output_image, flag_bytes):
    img = Image.open(input_image).convert("RGB")
    pixels = img.load()

    # Convert payload to bitstream
    bitstream = ''.join(f"{byte:08b}" for byte in flag_bytes)
    total_bits = len(bitstream)

    width, height = img.size
    idx = 0

    for y in range(height):
        for x in range(width):
            if idx >= total_bits:
                img.save(output_image)
                print(f"[+] Flag embedded successfully in {output_image}")
                return

            r, g, b = pixels[x, y]
            # Modify the LSB of the blue channel
            new_b = (b & 0xFE) | int(bitstream[idx])
            pixels[x, y] = (r, g, new_b)

            idx += 1

    print("[!] ERROR: Image too small to embed flag.")


def extract_flag(image_path, flag_length):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    bit_count = flag_length * 8
    bits = []

    width, height = img.size
    extracted = 0

    for y in range(height):
        for x in range(width):
            if extracted >= bit_count:
                break

            r, g, b = pixels[x, y]
            bits.append(str(b & 1))
            extracted += 1

        if extracted >= bit_count:
            break

    # Convert bits to bytes
    bitstream = ''.join(bits)
    data = int(bitstream, 2).to_bytes(flag_length, 'big')
    return data


# =========================================================
# RUN EMBEDDING
# =========================================================
embed_flag("LSBIUU/file.jpg", "LSBIUU/output.jpg", FLAG)

# =========================================================
# RUN EXTRACTION FOR TESTING
# =========================================================
extracted = extract_flag("LSBIUU/output.jpg", len(FLAG))
print("[+] Extracted from LSBIUU/output.jpg:", extracted)

if extracted[:len(extracted)-2] == FLAG:
    print("[✓] Verified: flag correctly embedded!")
else:
    print("[✗] Verification failed")
