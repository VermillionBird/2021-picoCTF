# Matryoshka doll
### Author: Susie/Pandu
### Forensics: 30 points

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](dolls.jpg)

---

The title and description imply that there are other files hidden inside `dolls.jpg`. The best way to check for these is to use `binwalk`. `binwalk dolls.jpg` gives us:

```
DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             PNG image, 594 x 1104, 8-bit/color RGBA, non-interlaced
3226          0xC9A           TIFF image data, big-endian, offset of first image directory: 8
272492        0x4286C         Zip archive data, at least v2.0 to extract, compressed size: 378954, uncompressed size: 383938, name: base_images/2_c.jpg
651612        0x9F15C         End of Zip archive, footer length: 22
```

We can see that there is a zipfile hidden inside the image, with another image inside it. `binwalk -e dolls.jpg` can extract it for us, extracting it into `_dolls.jpg.extracted`. Navigating into `base_images/` we see that this image likely similarly has a zipfile in it.

Continue using `binwalk -e` on each extracted image. Once you binwalk `4_c.jpg` you will see that instead of a zipfile hiding inside that image, `flag.txt` was hiding in it.

flag: `picoCTF{bf6acf878dcbd752f4721e41b1b1b66b}`
