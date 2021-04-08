# Surfing the Waves
### Author: James Lynch
### Forensics: 150 points

While you're going through the FBI's servers, you stumble across their incredible taste in music. One [main.wav](main.wav) you found is particularly interesting, see if you can find the flag!

---

The wav file just plays garbled sound. Open it in Audacity. The spectrogram also doesn't reveal any text or flag. `binwalk` doesn't reveal anything either. What does seem interesting though, is that if you zoom in on the waveform, all the values are positive.

![](/Images/waveform.PNG)

After quite a bit of googling, I stumble across this [writeup](https://github.com/AMACB/HSCTF-2020-writeups/blob/master/UntitledAudioChallenge.md). Long story short, in that challenge, the all positive data in the wav file encoded a PNG. 

After trying several different things, I managed to get the encoding scheme. Each frame in the wav file encoded a single digit hex number `0-f`. Combining these hex digits into a long hex string, then converting that to bytes outputted a valid file. This turned out to be the python program that generated the wav file. This also had the flag in it.

[Here](surfing.py) is my solve script, and [here](surfingout.py) is the outputted python program.

flag: `picoCTF{mU21C_1s_1337_c1faf2a7}`
