# New Vignere
### Author: madStacks
### Cryptography: 300 points

Another slight twist on a classic, see if you can recover the flag. (Wrap with picoCTF{}) bgjpchahecjlodcdbobhjlfadpbhgmbeccbdefmacidbbpgioecobpbkjncfafbe [new_vignere.py](new_vignere.py)

---

Opening up the provided program, we see that it is essentially the same as [New Caesar](../New%20Caesar/) except using Vigenere instead of Caesar. I will assume you have read New Caesar or solved it. 

```python
flag = "redacted"
assert all([c in "abcdef0123456789" for c in flag])

key = "redacted"
assert all([k in ALPHABET for k in key]) and len(key) < 15
```

Futhermore, we see the key is all letters `a-p`, with length less than 15, and the flag is all hex.

Vigenere is essentially just Caesar Cipher with a different shift for each character. For instance, with a key of `'abcdef'`, encrypting `'sampleplaintext'` with Vigenere is as follows:

```
Plaintext:  sampleplaintext
Key:        abcdefabcdefabc
Ciphertext: sbospjpmclryeyv
```

Let's start by figuring out the key length is.

First, use `[b16_encode(x) for x in "abcdef0123456789"]` in python to get the b16 equivalent of the flag characters. The output is `['gb', 'gc', 'gd', 'ge', 'gf', 'gg', 'da', 'db', 'dc', 'dd', 'de', 'df', 'dg', 'dh', 'di', 'dj']`. This is very important, as we can see that the first character of every two is either `'g'` or `'d'` pre-encryption. Let's call the first character of every two character sequence the differentiator, as it differentiates between letters and numbers.

This means that for every character in the key, the characters encrypted by that key character that are also differentiators should only result in at most two possible values. Let's check each key length to see which one satisfies that property.

```python
enc = "bgjpchahecjlodcdbobhjlfadpbhgmbeccbdefmacidbbpgioecobpbkjncfafbe"
for i in range(15):
    for x in range(math.lcm(i,2)):
        print(enc[x::math.lcm(i,2)])  
        #prints all characters encrypted by same key character and also either all differentiators or not differentiators)
    print(str(i) + "\n")
```

This script will print blocks of rows, one block per key length. For each block, starting with the first row, check every other row (these are the rows of encrypted differentiators) and make sure that they all have at most two characters per row.

We see the only key length that satisfies this is 9. I've annotated the output to show which key character position encrypts which row of differentiators.

```
bbeb -> key pos 1
ghfk
jjmj -> key pos 3
plan
cfcc -> key pos 5 
haif
adda -> key pos 7
hpbf
ebbb -> key pos 9
chpe
jgg  -> key pos 2
lmi
obo  -> key pos 4 
dee
ccc  -> key pos 6
dco
bbb  -> key pos 8
odp
```

Now we begin determining the key. Instead of solving for the key used for encryption, you can just solve for the key used for decryption. Note that `ord('g')-ord('d') = 3 mod 16`.

For key pos 1, `ord('e')-ord('b') = 3 mod 16` so `'e'` is `'g'` shifted and `'b'` is `'d'` shifted. The shift to undo it is therefore 2.

For key pos 2, `ord('j')-ord('g') = 3 mod 16` so `'j'` is `'g'` shifted and `'g'` is `'d'` shifted. The shift to undo it is therefore 13.

For key pos 3, `ord('m')-ord('j') = 3 mod 16` so `'m'` is `'g'` shifted and `'j'` is `'d'` shifted. The shift to undo it is therefore 10.

For key pos 4, `ord('b')-ord('o') = 3 mod 16` so `'b'` is `'g'` shifted and `'o'` is `'d'` shifted. The shift to undo it is therefore 5.

For key pos 5, `ord('f')-ord('c') = 3 mod 16` so `'f'` is `'g'` shifted and `'c'` is `'d'` shifted. The shift to undo it is therefore 1.

For key pos 6, we only have one character, `'c'`. This could be either `'g'` or `'d'` shifted. The shift to undo it is therefore either 1 or 4.

For key pos 7, `ord('d')-ord('a') = 3 mod 16` so `'d'` is `'g'` shifted and `'a'` is `'d'` shifted. The shift to undo it is therefore 3.

For key pos 8, we only have one character, `'b'`. This could be either `'g'` or `'d'` shifted. The shift to undo it is therefore either 2 or 5.

For key pos 9, `ord('e')-ord('b') = 3 mod 16` so `'e'` is `'g'` shifted and `'b'` is `'d'` shifted. The shift to undo it is therefore 2.

Our decryption key is therefore `'cnkfb(b,e)d(c,f)c'`. I tried `'cnkfbbdcc'` which worked.

[Here](newvigneresolve.py) is my solve script.

flag: `picoCTF{3489de46040aa96e55be9c1251172676}`
