import soundfile as sf

data, samplerate = sf.read('main.wav')

def convert(i):
    if i > 9:
        return chr(ord('a')+i-10)
    else:
        return i

with open('surfingout.py', 'wb') as file:
    old_min = min(data)
    old_range = max(data)-old_min
    new_min = 0
    new_range = 15 + 0.999999999999999 - new_min
    output = [int((n-old_min)/old_range*new_range+new_min) for n in data]
    out = ''.join([str(convert(num)) for num in output])
    file.write(bytes.fromhex(out))