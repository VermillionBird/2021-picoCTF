# Magikarp Ground Mission
### Author: Syreal
### General Skills: 30 points


Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `6dee9772`

---

Start the instance, then ssh to the provided container using the provided command and password. 

`ls` to view the files. `cat 1of3.flag.txt` to get the first third of the flag. `cat instructions-to-2of3.txt` tells you to go to the root directory. Do so with `cd /`. 

`cat 2of3.flag.txt` to get the second third of the flag. `cat instructions-to-3of3.txt` tells you to go to your home directory. Do so with `cd ~` or just `cd`. 

`cat 3of3.flag.txt` to get you the final part of the flag. Concatenate them to get the full flag.

flag: `picoCTF{xxsh_0ut_0f_\/\/4t3r_540e4e79}`
