# Wireshark twoo twooo two twoo...
### Author: Dylan
### Forensics: 100 points

Can you find the flag? [shark2.pcapng](shark2.pcapng).

---

Looking at the HTTP packets with the filter `http`, we see a bunch of red herring flags. The next place to look is at `dns` packets.

Here, we can see a lot of DNS requests to `[base64 string].reddshrimpandherring.com`. These look promising, perhaps concatenating the base64 results in our flag. Let's filter out the responses with `dns && dns.flags.response == 0` so we can only look at the reqeusts. Every request is sent 3 times. Let's reduce the clutter by filtering out the repetitions with `dns && dns.flags.response == 0 && frame.len < 100`.

![](/Images/wireshark2.PNG)

Looking at our packets, we see one with a different destination IP. The base64 in the query is `cGljb0NU`, which decoded from base64 is `picoCT`. Ok, let's add one last filter: `dns && dns.flags.response == 0 && frame.len<100 && ip.dst == 18.217.1.57`.

The remaining packets give the base64: `cGljb0NURntkbnNfM3hmMWxfZnR3X2RlYWRiZWVmfQ==` which gives us the flag.

flag: `picoCTF{dns_3xf1l_ftw_deadbeef}`
