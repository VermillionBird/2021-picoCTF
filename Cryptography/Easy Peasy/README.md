# Easy Peasy
### Author: madStacks
### Cryptography: 40 points


A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) `nc mercury.picoctf.net 11188` [otp.py](otp.py)

---

Download `otp.py`. OTPs are unbreakable, as mentioned in the challenge description, but only if implemented properly. Let's take a look at the program.

First, notice that the flag is retrieved from a file, and is 50000 bytes long. 

`startup(key_location)` takes an index as a parameter, and reads bytes from the key file starting from that index. It then uses the key to xor with the flag, and prints out the encrypted flag. Finally, it returns the ending location.

`encrypt(key_location)` is similar, but encrypts your input. Crucially, however, notice that if the data you'd like to encrypt ends up requiring more bytes than there are remaining from the start location, it **wraps around to the beginning of the key file**. If you reuse a key, it is no longer an OTP and is vulnerable to attack.

Looking at the rest of the code, the flag is encrypted with the first bytes of the flag. Then, it encrypts what you request.

Our attack will be as follows:

First, retrieve the encrypted flag. Decode it from hex and store the bytes in a flag variable. Next, encrypt `(50000-len(flag))` gibberish characters. This will wrap us around to the beginning of the key file, and the next bytes we encrypt will reuse the bytes used to encrypt the flag. Encrypt `len(flag)` characters. I used just `'A'`. Retrieve the output of this encryption, decode it from hex, and store the bytes in another variable.

Now xor the bytes of the encrypted `'A'`s with the `'A'`s. This will return the bytes of the key used in the encryption. `flag` is encrypted using the same key bytes, so xor flag with the key bytes to get the plaintext flag. Wrap with `picoCTF{}`.

My solve script is [here](otpsolve.py).

flag: `picoCTF{7904ff830f1c5bba8f763707247ba3e1}`
