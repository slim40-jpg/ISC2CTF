import wave

wav = wave.open("wav_flag/flag.wav" , "rb")
n_channels , sample_width , frame_rate , nbr_frames , comp_type , compname = wav.getparams()
frames = bytearray(wav.readframes(nbr_frames))
wav.close()

# extract the LSBs
bits = ''.join(str(frames[i] & 1) for i in range(len(frames)))

# convert 8 bits at a time to text
flag = ''.join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))

print(flag[:30])
