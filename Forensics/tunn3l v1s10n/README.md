# tunn3l v1s10n
### Danny
### Forensics: 40 points

We found this [file](tunn3l_v1s10n). Recover the flag.

---

Download the provided file. `file` and `binwalk` don't tell us anything interesting, so let's open it up in a hex editor.

The first two bytes are `42 4D`, or `BM`. These are the magic numbers for the BMP image format. [This link](http://www.ece.ualberta.ca/~elliott/ee552/studentAppNotes/2003_w/misc/bmp_file_format/bmp_file_format.htm) gives us information about the format of a BMP file.

Bytes 0-1 are `BM`. Our original file has this correctly. 

Bytes 2-5 should be the file size, in little endian. The bytes are `8E 26 2C 00`, or 2893454 in decimal. Checking this with `ls -l tunn3l_v1s10n` shows that this is correct.

Bytes 6-9 are reserved and should be zero. This checks out.

Bytes 10-13 should be the the offset from the beginning of the file to the beginning of the data, or basically the length of all the image information (Header + InfoHeader + ColorTable). What we have is `BA D0 00 00`. These 4 bytes were probably edited, and will need to be fixed.

Bytes 14-17 should be the size of InfoHeader, which is always 40. Instead, it is `BA D0 00 00` once again, telling us we need to fix this.

We don't see `BA D0 00 00` anywhere else, so presumably that's all we need to fix. Let's start with the second set of 4 changed bytes, bytes 14-17. This should be 40, or in 4 bytes of little endian hex, `28 00 00 00`.

Now for the first set, bytes 10-13. This should be the length of Header + InfoHeader + ColorTable. We know Header is 14 bytes and InfoHeader is 40 bytes. How long is ColorTable though? It depends on the bit depth, or bits used per pixel. This is encoded in bytes 28-29. In our file, that is `18 00`, or 24 in decimal. According to the BMP file format, if the bit depth is 24, then ColorTable is not present. Therefore, bytes 10-13 should just be 14 + 40 = 54 = `36 00 00 00`

Opening up the file we see a fake flag in the image. Looks like we still have more work to do. The dimensions of the image seem a little bit weird; it's very wide. In combination with the title, this makes me think that perhaps the size information of the file is incorrect. There might be more pixels encoded than the height and width dimensions say there are. Generally, this is only possible by decreasing the height, since pixels are encoded left to right and changing the width would make the image look wrong.

Let's check this hunch. We know that the image is 2893454 bytes, with the first 54 bytes the header information. This leaves 2893400 bytes of data.

Bytes 18-21 give us the width and bytes 22-25 give us the height. Here we see `6E 04 00 00` and `32 01 00 00`, or 1134 and 306 respectively.

Since the current image looks normal, we know that the height got decreased and the width is correct. Since the bit depth is 24, that means each pixel is encoded by 24 bits, or 3 bytes. Dividing 2893400 by 3 and then 1134 gives us 850.499 pixels of as the correct height. Round down to 850 pixels. This means the height should be `52 03 00 00`.

Now, our image displays the flag.

flag: `picoCTF{qu1t3_a_v13w_2020}`
