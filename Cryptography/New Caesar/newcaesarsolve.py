x = "apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna"
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
for i in range(16):
    out =   ""
    for char in x:
        out += ALPHABET[(ord(char) + i) % len(ALPHABET)]
    dec = ""
    for i in range(0,len(out),2):
        a = '{0:04b}'.format(ord(out[i])-LOWERCASE_OFFSET) + '{0:04b}'.format(ord(out[i+1])-LOWERCASE_OFFSET) 
        dec += chr(int(a,2))

    print(dec)