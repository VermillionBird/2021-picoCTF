# MacroHard WeakEdge
### Author: madStacks
### Forensics: 60 points

I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](Forensics%20is%20fun.pptm)

---

Microsoft Office files are all zip files, so you can unzip the powerpoint. In the unzipped folder, go to `ppt/slideMasters/` and there is a file called `hidden`. This folder has the flag encoded in base64.

flag: `picoCTF{D1d_u_kn0w_ppts_r_z1p5}`
