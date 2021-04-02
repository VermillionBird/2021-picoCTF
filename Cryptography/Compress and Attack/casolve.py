from pwn import *
import string

alpha = string.ascii_letters + '_}'

r = remote('mercury.picoctf.net', 33976)
flag = 'picoCTF{'
while flag[-1] != '}':
    curr = -1
    for i in alpha:
        r.sendline(flag + i)
        r.recvuntil('\n')
        r.recvuntil('\n')
        length = r.recvuntil('\n').strip()
        length = int(length)
        if curr == -1:
            curr = length
        if length < curr:
            flag += i
            print(flag)
            break
