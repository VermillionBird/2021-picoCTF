from pwn import *

r = remote('mercury.picoctf.net', 11188)
r.recv()
r.recvuntil('\n')
flag = r.recvuntil('\n').decode('ascii').strip()
flag = bytes.fromhex(flag)
r.recv()
r.sendline('A'*(50000-len(flag)))
r.recvuntil('\n\n')
r.recv()
r.sendline('A'*len(flag))
ret = r.recv().replace(b'Here ya go!\n', b'').strip()
ret = bytes.fromhex(ret.decode('ascii'))


def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


key = byte_xor(b'A' * len(flag), ret)
flag = byte_xor(key, flag)
print(flag.decode('ascii'))