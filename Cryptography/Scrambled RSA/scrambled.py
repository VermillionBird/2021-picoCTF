from pwn import *
r = remote("mercury.picoctf.net", 61477)

r.recvuntil(": ")
flag = r.recvuntil("\n").strip().decode()

print(len(flag))

r.recvuntil(": ")
n = r.recvuntil("\n").strip().decode()

r.recvuntil(": ")
e = r.recvuntil("\n").strip().decode()

def get_res(inp):
    r.recvuntil(": ")
    r.sendline(inp)
    r.recvuntil(": ")
    res = r.recvuntil("\n").strip().decode()
    return res



import string
flag_chars = string.ascii_letters + string.digits + "_{}"
    

dict = {}

out = ''

while len(out) == 0 or out[-1] != "}":
    for char in flag_chars:
        inp = out + char
        res = get_res(inp)
        for i in range(1,len(inp)):
            temp = inp[0:i]
            section = dict[temp]
            res = res.replace(section,'')
        dict[inp] = res

    for key in dict:
        if len(key) == len(out)+1 and dict[key] in flag:
            flag.replace(dict[key],'')
            out = key



    print(out)

#picoCTF{bad_1d3a5_4981729}