# Static ain't always noise
### Author: Syreal
### General Skills: 15 points

Can you look at the data in this binary: [static](static)? This [BASH script](ltdis.sh) might help!

---

Make the script executable and run it. It turns out it asks for a file as an argument. Run `ltdis.sh static`. It outputs two files, with the disassembly at `static.ltdis.x86_64.txt` and strings at `static.ltdis.strings.txt`. The flag is in the strings file.

Alternatively, instead of using the script, you could also have just used the `strings` command for the same result.

flag: `picoCTF{d15a5m_t34s3r_ae0b3ef2}`
