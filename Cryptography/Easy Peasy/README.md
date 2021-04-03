# Easy Peasy
### Author: madStacks
### Cryptography: 40 points


A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{}) `nc mercury.picoctf.net 11188` [otp.py](otp.py)

---

Download `otp.py`. OTPs are unbreakable, as mentioned in the challenge description, but only if implemented properly. Let's take a look at the program.

```python
import os.path

KEY_FILE = "key"
KEY_LEN = 50000
FLAG_FILE = "flag"
```

First, notice that the flag is retrieved from a file, and is 50000 bytes long. 

```python
def startup(key_location):
	flag = open(FLAG_FILE).read()
	kf = open(KEY_FILE, "rb").read()

	start = key_location
	stop = key_location + len(flag)

	key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
	print("This is the encrypted flag!\n{}\n".format("".join(result)))

	return key_location
```

`startup(key_location)` takes an index as a parameter, and reads bytes from the key file starting from that index. It then uses the key to xor with the flag, and prints out the encrypted flag. Finally, it returns the ending location.

```python
def encrypt(key_location):
	ui = input("What data would you like to encrypt? ").rstrip()
	if len(ui) == 0 or len(ui) > KEY_LEN:
		return -1

	start = key_location
	stop = key_location + len(ui)

	kf = open(KEY_FILE, "rb").read()

	if stop >= KEY_LEN:
		stop = stop % KEY_LEN
		key = kf[start:] + kf[:stop]
	else:
		key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))

	print("Here ya go!\n{}\n".format("".join(result)))

	return key_location
```

`encrypt(key_location)` is similar, but encrypts your input. Crucially, however, notice that if the data you'd like to encrypt ends up requiring more bytes than there are remaining from the start location, it **wraps around to the beginning of the key file**. If you reuse a key, it is no longer an OTP and is vulnerable to attack.

```python
print("******************Welcome to our OTP implementation!******************")
c = startup(0)
while c >= 0:
	c = encrypt(c)
```

Looking at the rest of the code, the flag is encrypted with the first bytes of the flag. Then, it encrypts what you request.

Our attack will be as follows:

```python
from pwn import *

r = remote('mercury.picoctf.net', 11188)
r.recv()
r.recvuntil('\n')
flag = r.recvuntil('\n').decode('ascii').strip()
flag = bytes.fromhex(flag)
```

First, retrieve the encrypted flag. Decode it from hex and store the bytes in a flag variable. 

```python
r.recv()
r.sendline('A'*(50000-len(flag)))
r.recvuntil('\n\n')
```

Next, encrypt `(50000-len(flag))` gibberish characters. This will wrap us around to the beginning of the key file, and the next bytes we encrypt will reuse the bytes of the key used to encrypt the flag. 

```python
r.recv()
r.sendline('A'*len(flag))
ret = r.recv().replace(b'Here ya go!\n', b'').strip()
ret = bytes.fromhex(ret.decode('ascii'))
```

Encrypt `len(flag)` characters. I used just `'A'`s. Retrieve the output of this encryption, decode it from hex, and store the bytes in another variable.

```python
def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


key = byte_xor(b'A' * len(flag), ret)
flag = byte_xor(key, flag)
print(flag.decode('ascii'))
```

Now xor the bytes of the encrypted `'A'`s with the `'A'`s. This will return the bytes of the key used in the encryption. `flag` is encrypted using the same key bytes, so xor flag with the key bytes to get the plaintext flag. Wrap with `picoCTF{}`.

My solve script is [here](otpsolve.py).

flag: `picoCTF{7904ff830f1c5bba8f763707247ba3e1}`
