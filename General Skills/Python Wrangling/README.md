# Python Wrangling
### Author: Syreal
### General Skills: 10 points


Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](ende.py) using [this password](pw.txt) to get [the flag](flag.txt.en)

---

Download all the files. Run `ende.py` with `python ende.py` to get: `Usage: ende.py (-e/-d) [file]`. `flag.txt.en` suggests an encrypted flag, so we should use the `-d` option to decrypt it.

`python ende.py -d flag.txt.en` then asks us for the password. `cat pw.txt` gives us the password, which we put into the program to get the flag.

flag: `picoCTF{4p0110_1n_7h3_h0us3_68f88f93}`
