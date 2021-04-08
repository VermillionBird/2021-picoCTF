# It is my Birthday 2
### Author:
### Cryptography: 270 points

"My birthday is coming up again, but I want to have a very exclusive party for only the best cryptologists. See if you can solve my challenge, upload 2 valid PDFs that are different but have the same SHA1 hash. They should both have the same 1000 bytes at the end as the original invite. [invite.pdf](invite.pdf)

---

According to [SHAttered.io](https://shattered.io/), SHA-1 has a practical cryptographic exploit that allows you to create two pdfs with the same SHA1 hash.

![](https://shattered.io/static/pdf_format.png)

Taking a look at this image and looking over the [paper](https://shattered.io/static/shattered.pdf), we can see that the two PDFs will have a pre-determined prefix, then calculated collision blocks that will make the two PDFs have the same SHA1 hash **for any suffix appended to both the PDFs**.

[This python script](https://github.com/nneonneo/sha1collider/blob/master/collide.py) generates two PDFs with the same SHA1 hash two input pdfs. 

[This python script I wrote](shatteredsolve.py) takes the two generated PDFs then appends the last 1000 bytes of `invite.pdf`. The generated PDFs will have the same SHA1 hash, have different contents, and have the same 1000 last bytes as the original invite, fulfilling the requirement.

Upload them to the site to get the flag. At the time of this writeup, the site is not available and I regrettably did not write down the flag during the competition.

flag: `TBA`
