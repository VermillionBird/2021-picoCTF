# No Padding, No Problem
### Author: Sara
### Cryptography: 90 points

Oracles can be your best friend, they will decrypt anything, except the flag's ciphertext. How will you break it? Connect with `nc mercury.picoctf.net 10333`.

---

Upon connection to the oracle, we see:

```
Welcome to the Padding Oracle Challenge
This oracle will take anything you give it and decrypt using RSA. It will not accept the ciphertext with the secret message... Good Luck!


n: 53798724109991336602804713105138600065627977034132253733974318184308114914563723407682997519893953004109884348376676521948436423646028777740715078799858381062405576922517304543896986859218695905466630986406221089033743391477484273795748783200185286185624716089226917926054886428397954459446727627656377722049
e: 65537
ciphertext: 18728522276935945735804931382179738554853119608931410877823126868300903394695379636425237957213275389838734891061408432704624659011993329619150775769495313432348697571286604155985107736825974496537676440374753849241784899023498109311944345628830301127424809785048523085351745823292270527576035731956958594835


Give me ciphertext to decrypt: 
```

As stated, giving the ciphertext will not work. How can we get it to decrypt our flag then?

Well, in RSA `c = m ^ e mod n`. What if we pass it the ciphertext of `m * 2`? Then we can just divide the returned plaintext by 2 to get the flag.

Since `c = m ^ e mod n`

```
c2 = (m * 2) ^ e mod n
   = (m ^ e) * (2 ^ e) mod n
   = ((m ^ e) mod n * (2 ^ e) mod n) mod n
   = (c * (2^e) mod n) mod n
```

Connect to the oracle, give it `c2`, receive `m * 2`, divide by 2, then convert to hex and then ascii to get the flag.

flag: `picoCTF{m4yb3_Th0se_m3s54g3s_4r3_difurrent_1772735}`
