# New Caesar
### Author: madStacks
### Cryptography: 60 points

We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{})

`apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna` [new_caesar.py](new_caesar.py)

---

Download `new_caesar.py`. Let's take a look at their implementation.

We see that the alphabet is only the first 16 characters, `a-p`. `b16_encode(plain)` converts normal characters into our 16 character alphabet. Each character is converted into binary. Characters in binary have 8 bits, so the first 4 bits are converted into one character in the alphabet and the last 4 bits to another, since 4 bits have `2 ^ 4 = 16` possibilities. 

`shift(c,k)` performs a simple caesar shift over our 16 character alphabet.

FInally, we see the encryption. The key is a character `a-p` as expected. The flag is converted into our 16 character alphabet then caesar shifted by the key. Finally, it is output.

There are only 16 possibilities for the key, so it is simple to just try all of them. Shift the ciphertext by each possible key then convert from the 16 character alphabet to normal ascii.

[Here](newcaesarsolve.py) is my solve script.

Out of the 16 outputs, only one looks like a flag. Wrap with `picoCTF{}`.

flag: `picoCTF{et_tu?_23217b54456fb10e908b5e87c6e89156}`
