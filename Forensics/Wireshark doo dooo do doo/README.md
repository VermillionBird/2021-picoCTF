# Wireshark doo dooo do doo...
### Author: Dylan
### Forensics: 50 points

Can you find the flag? [shark1.pcapng](shark1.pcapng).

---

Open up the provided network capture with Wireshark. The first thing I usually do with packet captures is look at HTTP packets, if there are any. Apply the filter `http`.

There are a lot of POST requests their corresponding responses. Ignore them.

![](/Images/wireshark1.PNG)

The first HTTP GET request's response contains the flag in its returned html. It is ciphered using ROT13, so uncipher it to get the flag.

flag: `picoCTF{p33kab00_1_s33_u_deadbeef}`
