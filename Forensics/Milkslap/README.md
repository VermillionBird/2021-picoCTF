# Milkslap
### Author: James Lynch
### Forensics: 200 points

[🥛](http://mercury.picoctf.net:48319/)

---

Open the link and you see a website modeled after eelslap. As this is a forensics problem, not a web problem, we likely have to find the flag from the image used on the website.

Inspect Element, go to Network, reload the page, then download `concat_v.png`. I've also attached it [here](concat_v.png).

As it's a png file, let's start by running it through `zsteg`. `zsteg` outputs the flag under the stego scheme `b1,b,lsb,xy`. This means the flag was encoded into the least significant bit of the blue RGB channel.

flag: `picoCTF{imag3_m4n1pul4t10n_sl4p5}`
