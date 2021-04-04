# Trivial Flag Transfer Protocol
### Author: Danny
### Forensics: 90 points

Figure out how they moved the [flag](tftp.pcapng).

---

The title refers to TFTP (Trivial File Transfer Protocol), a protocol for transfering files.

![](/Images/tftp.PNG)

Using Wireshark, File -> Export Objects -> TFTP. Save all the files.

`instructions.txt` is ROT13 encoded and reveals the message `TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN`.

`plan` is also ROT13 encoded and reveals the message `I USED THE PROGRAM AND HID IT WITH - DUEDILIGENCE. CHECK OUT THE PHOTOS`.

The program refers to `program.deb`. Install the program. It turns out it's `steghide`, which I already had.

`steghide extract -sf [file]` extracts hidden information from the provided file. Use it with the 3 images, inputting the password `DUEDILIGENCE` each time. `picture3.bmp` had `flag.txt` hidden in it.

flag: `picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}`
