# Scrambled: RSA
### Author: Sara
### Cryptography: 140 points

Hmmm I wonder if you have learned your lesson... Let's see if you understand RSA and how the encryption works. Connect with `nc mercury.picoctf.net 61477`.

---

Connect to the service and we receive something similar to this:

```
flag: 446362518558400186109981415107393936713221819222026934750885514927885759778785747232338476349836510185293096228073344680750550713160162054260392227492515444308733997285219579717256955031940541997179021725553777819843637846050103201810030377633109605827193084136714193649601932633826364854182879111275757955815167363035030140...(more not shown)
n: 65496449241807949892280933519586989972785989760091378430728021070571891668632750502774573754354936537434158815842758685213934327516975187420177036642952307990530718890556300131184670950052610475277655951177726301897431672847119152251248127335282035946364856778490184449313735770124761135345586978927027976799
e: 65537
I will encrypt whatever you give me:
```

The encrypted flag is absolutely massive, so it's clearly not simple RSA. We can confirm this by inputting `'a'` and seeing that the encryption is different than the normal RSA encryption of `'a'` with the given `n` and `e`. We then begin some reconaissance.

If you encrypt a sequence of 2 or more characters repeatedly, sometimes you get different encryptions, which is strange. It turns out that the different encryptions are just scrambled versions of each other, and part of the encryption is always the encrypted version of the first letter, another part a sequence unique to the first two letters, and so on. 


For instance, say you encrypt `'ab'`. The output of the text will be the concatenation, in some order, of the encryption of `'a'` and another sequence unique to `'ab'`. If you encrypt `'abc'`, the output of the text will be the concatentation, in some order, of the encryption of `'a'`, the sequence unique to `'ab'`, and a sequence unique to `'abc'`. And so on, for any input.

![](/Images/scrambledrsa.png)

Here, the encryption of `'a'` is highlighted green. The sequence unique to `'ab'` is highlighted red. The sequence unique to `'abc'` is highlighted blue. You can see it matches my description.

Knowing this, we can slowly bruteforce the flag. We first encrypt all the characters that might be in the flag. One of the encryptions of these characters will be in the given encrypted flag. The flag therefore starts with that letter. 

Next, we encrypt all the two character sequences starting with the letter we just found. These encryptions will have enc(first_letter) in the encryption, so we remove it to get the sequence unique to those two letters. One of these sequences will appear in the encrypted flag, so the flag therefore starts with those two letters.

For three letters, we remove the encryption of the first letter and the sequence unique to the first two letters to get the sequence unique to the third letter. If it appears in the encrypted flag, the flag starts with those three letters.

We continue this until we get the whole flag. I'm not sure if this is the intended solution or not, since RSA was not used in the solve.

[Here](scrambled.py) is my solve script.

flag: `picoCTF{bad_1d3a5_4981729}`
