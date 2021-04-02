import string
import binascii
import sys
from Crypto.Cipher import DES

def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()

import itertools

def double_decrypt(msg, KEY1, KEY2):
    b = binascii.unhexlify(msg)

    cipher1 = DES.new(KEY1, DES.MODE_ECB)
    dec_msg = cipher1.decrypt(b)
    cipher2 = DES.new(KEY2, DES.MODE_ECB)
    return cipher2.decrypt(dec_msg)
seen = []
for combo in itertools.product('13579', repeat=6):
    key = pad(''.join(combo))
    if key not in seen:
        seen.append(key)
    for combo2 in itertools.product('13579', repeat=6):
        key2 = pad(''.join(combo2))
        dec = double_decrypt("f419781796879c8b8ad14d6f4e57d62302dfbd34d0d95772e873087072f1580fae46bac7e5617283", key, key2)
        try:        
            dec = dec.decode()
            if dec.isprintable():
                print(key, key2, dec)
                sys.exit(0)
        except:
            pass
        dec = double_decrypt("f419781796879c8b8ad14d6f4e57d62302dfbd34d0d95772e873087072f1580fae46bac7e5617283", key2, key)
        try:        
            dec = dec.decode()
            if dec.isprintable():
                print(key2, key, dec)
                sys.exit(0)
        except:
            pass

#9af5126b7bc7f825b3cae0e32bd1acb4