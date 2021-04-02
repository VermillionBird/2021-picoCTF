# Double DES
### Author: madStacks
### Cryptography: 120 points

I wanted an encryption service that's more secure than regular DES, but not as slow as 3DES... The flag is not in standard format. `nc mercury.picoctf.net 37751` [ddes.py](ddes.py)

---

Opening the program we see a simple implementation of DES applied twice, with two different, random keys. The keys however, are 6 digits and then two spaces.

DES actually uses a 56 bit key, not a 64 bit key as the 8 byte key length suggests. The LSB of each byte is ignored, meaning that instead of 10 possible digits, our key will only have 5 possible digits per byte.

We can just bruteforce using digits of 1,3,5,7, and 9. There are only (5 ^ 12) possibilities, so not that bad.

Connect to the service provided and get a DDES encrypted flag. Use that in your solve script.

[Here](ddessolve.py) is my solve script. There are some optimizations that could be made, like making sure you don't use a pair of keys that's already been used in the other order.

flag: `9af5126b7bc7f825b3cae0e32bd1acb4`
