from PIL import PngImagePlugin, Image


flag = "ISC2CTF{pNg_m3T4D4tA_x0R_}"
key = "Danish"

xored = bytes([ord(flag[i]) ^ ord(key[i % len(key)]) for i in range(len(flag))])


img = Image.open("xor/file.png")
meta = PngImagePlugin.PngInfo()
meta.add_text("Question", "What is her nationality?")
img.save("xor/step1.png", pnginfo=meta)

with open("xor/step1.png", "rb") as f:
    data = f.read()

marker = b"SECRET_DATA:"
with open("xor/challenge.png", "wb") as f:
    f.write(data + marker + xored)

