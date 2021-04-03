# Play Nice
### Author: madStacks
### Cryptography: 110 points

Not all ancient ciphers were so bad... The flag is not in standard format. `nc mercury.picoctf.net 40742` [playfair.py](playfair.py)

---

Opening the provided python file, we see that we need to decrypt an encrypted message, and if we get it correct, we get the flag. This is just a Playfiar cipher. Any online decoder works fine.

Connecting to the service we see:

```
Here is the alphabet: irlgektq8ayfp5zu037nov1m9xbc64shwjd2
Here is the encrypted message: h5a1sqeusdi38obzy0j5h3ift7s2r2
What is the plaintext message? 
```

I used [dcode](https://www.dcode.fr/playfair-cipher). Input the alphabet, using a 6x6 matrix. Input the encrypted message to get the plaintext message. dcode outputs it in all caps, so convert it to lowercase before inputting it into the service. The service then returns the flag.

flag: `25a0ea7ff711f17bddefe26a6354b2f3`
