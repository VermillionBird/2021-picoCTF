# Disk, disk, sleuth! II
### Author: Syreal
### Forensics: 130 points

All we know is the file with the flag is named `down-at-the-bottom.txt`... Disk image: [dds2-alpine.flag.img.gz](https://mercury.picoctf.net/static/2e54f22211165e9f33a47bdb8a09268b/dds2-alpine.flag.img.gz)

---

I used [Autopsy](https://www.autopsy.com/) for this. Open a case and add the image as a Disk Image file after unzipping the image. View File Types By Extension, then go to Documents, and then Plain Text. The flag is in the file.

![](Images/autopsy.PNG)

flag: `picoCTF{f0r3ns1c4t0r_n0v1c3_db59daa5}`
