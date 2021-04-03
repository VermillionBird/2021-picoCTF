# Compress and Attack
### Author: Jake Beley
### Cryptography: 130 points

Your goal is to find the flag. [compress_and_attack.py](compress_and_attack.py) `nc mercury.picoctf.net 33976`

---

```python
import zlib
from random import randint
import os
from Crypto.Cipher import Salsa20

flag = open("./flag").read()


def compress(text):
    return zlib.compress(bytes(text.encode("utf-8")))

def encrypt(plaintext):
    secret = os.urandom(32)
    cipher = Salsa20.new(key=secret)
    return cipher.nonce + cipher.encrypt(plaintext)

def main():
    while True:
        usr_input = input("Enter your text to be encrypted: ")
        compressed_text = compress(flag + usr_input)
        encrypted = encrypt(compressed_text)
        
        nonce = encrypted[:8]
        encrypted_text =  encrypted[8:]
        print(nonce)
        print(encrypted_text)
        print(len(encrypted_text))
```

Opening `compress_and_attack.py` we see that the service takes our text, prepends it with the flag, compresses it with `zlib.compress`, then encrypts it using Salsa20, outputting the result and the length of the result to us.

Salsa20 is a stream cipher that is cryptographically secure as of right now. So the challenge is not to attack Salsa20, as the implementation here is secure. The title suggests our attack should be targetting the compression.

`zlib` uses DEFLATE, a lossless method of compression. Lossless methods of compression depend on the fact that typical data will have redundancies in characters. While this writeup will not go into details on zlib's compression method, it suffices to say that the more repetitions of sequences of characters there are, the shorter the resulting encoding. 

![](/Images/compressattack.PNG)

You can try it out in python yourself.

Since Salsa20 is a stream cipher, the length of the ciphertext reflects the length of the plaintext. Therefore, if we input sequences of characters that are in the flag, the length of the encoded `flag+input` will be shorter and the length of the ciphertext will be shorter.

We can write a script to bruteforce each character of the flag one by one. We try every character, and the one that results in the shortest ciphertext is the next character in our flag.

[Here](casolve.py) is my solve script.

flag: `picoCTF{sheriff_you_solved_the_crime}`
