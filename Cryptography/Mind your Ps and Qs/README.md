# Mind your Ps and Qs
### Author: Sara
### Cryptography: 20 points


In RSA, a small e value can be problematic, but what about N? Can you decrypt this? [values](values)

---

Open the values file to reveal:
```
Decrypt my super sick RSA:
c: 421345306292040663864066688931456845278496274597031632020995583473619804626233684
n: 631371953793368771804570727896887140714495090919073481680274581226742748040342637
e: 65537
```
In RSA:
```
m = c ^ d mod n
n = p * q
d = e ^ -1 mod φ(n)
φ(n) = (p-1)*(q-1)
```
`m` is the plaintext message, `c` is the ciphertext message, `n` is the modulus, `p` and `q` are the prime factors of `n`, `e` is the public exponent, and `d` is the private exponent.

The security of RSA depends on the impracticality of factorizing `n`, where the prime factors of `n` are so large that it would take years to find the factors of `n`. But here, `n` is quite small, and easily factorable.

Using [this integer factorization calculator](https://www.alpertron.com.ar/ECM.HTM) `n` is factored in about 8 minutes for me. The site also gives Euler's totient `φ(n)`.  

```
p = 1461849912200000206276283741896701133693
q = 431899300006243611356963607089521499045809
φ(n) = (p-1)(q-1) =  631371953793368771804570727896887140714061729769155038068711341335911329840163136
```

On python 3.8 and later, you can use `pow(e, -1, φ(n))` to find `d`, replacing `e` and `φ(n)` with the real numbers.

`d = 86820026055294556838164569629472617179839240561509150603097892917271661878321409`

Now just find `m = c ^ d mod n` with `pow(c,d,n)`.

`m = 13016382529449106065927291425342535437996222135352905256639647889241102700065917`

Converting that to hex and characters using `bytes.fromhex(hex(m)[2:])` gives the flag.

flag: `picoCTF{sma11_N_n0_g0od_55304594}`
