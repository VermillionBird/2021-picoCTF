x = "bgjpchahecjlodcdbobhjlfadpbhgmbeccbdefmacidbbpgioecobpbkjncfafbe"
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
'''
[b16_encode(x) for x in "abcdef0123456789"]=
['gb', 'gc', 'gd', 'ge', 'gf', 'gg', 'da', 'db', 'dc', 'dd', 'de', 'df', 'dg', 'dh', 'di', 'dj']
'''
KEYLEN=9
'''
first row and every other row after should only have 2 letters possible

enc = "bgjpchahecjlodcdbobhjlfadpbhgmbeccbdefmacidbbpgioecobpbkjncfafbe"
for i in range(15):
    for x in range(math.lcm(i,2)):
        print(enc[x::math.lcm(i,2)])
    print(str(i) + "\n")
'''
'''
bbeb -> key pos 1 shift of 2 = c
ghfk
jjmj -> key pos 3 shift of 10 = k
plan
cfcc -> key pos 5 shift of 1 = b
haif
adda -> key pos 7 shift of 3 = d
hpbf
ebbb -> key pos 9 shift of 2 = c
chpe
jgg  -> key pos 2 shift of 13 = n
lmi
obo  -> key pos 4 shift of 5 = f
dee
ccc  -> key pos 6 shift of 1 or 4 = b or e
dco
bbb  -> key pos 8 shift of 2 or 5 = c or f
odp

cnkfb(b,e)d(c,f)c

cnkfbbdcc worked

'''
        
key = "cnkfbbdcc"
out = ""
for index, char in enumerate(x):
    char_pos = ord(char) - LOWERCASE_OFFSET 
    key_char = ord(key[index % 9]) - LOWERCASE_OFFSET
    out += ALPHABET[(char_pos + key_char) % len(ALPHABET)]
dec = ""
for i in range(0,len(out),2):
    a = '{0:04b}'.format(ord(out[i])-LOWERCASE_OFFSET) + '{0:04b}'.format(ord(out[i+1])-LOWERCASE_OFFSET) 
    dec += chr(int(a,2))

if all([c in "abcdef0123456789" for c in dec]):
    print(dec)