# Disk, Disk, Sleuth!
### Author: Syreal
### Forensics: 110 points

Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: [dds1-alpine.flag.img.gz](https://mercury.picoctf.net/static/920731987787c93839776ce457d5ecd6/dds1-alpine.flag.img.gz)

---

Download the image file and unzip it with `gunzip dds1-alpine.flag.img.gz`. The description says to use sleuthkit's `srch_strings`, but you can just use `strings`.

Use `strings dds1-alpine.flag.img | grep pico` to search for strings and then search the strings for the flag.

flag: `picoCTF{f0r3ns1c4t0r_n30phyt3_564ff1a0}`
