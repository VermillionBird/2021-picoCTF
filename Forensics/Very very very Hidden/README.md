# Very very very Hidden
### Author: Sara
### Forensics: 300 points

Finding a flag may take many steps, but if you look diligently it won't be long until you find the light at the end of the tunnel. Just remember, sometimes you find the hidden treasure, but sometimes you find only a hidden map to the treasure. [try_me.pcap](try_me.pcap)

---

Open the packet capture in Wireshark. Filter by `http`. We see that two PNG images were retrieved, `duck.png` and `evil_duck.png`. Extract these two images (File -> Export Objects... -> HTTP).

![](duck.png) ![](evil_duck.png)

Clearly some data was encoded into `evil_duck.png` steganographically, but standard stegotools like zsteg, stegsolve, or steghide don't seem to output anything. Strings doesn't give any clues either, nor does binwalk.

Looking further we see another request to `powershell.org`. Strange, `powershell.org` doesn't seem to relate to steganography. In the `dns` queries, there is also `powershell.fios-router.home`. Powershell seems important but how? After a while, I finally googled "powershell steganography" and found [this blog post](https://pcsxcetrasupport3.wordpress.com/2020/07/22/powershell-steganography/). The author of the blog post helpfully also created a [tool](https://github.com/PCsXcetra/Decode_PS_Stego) to decode said Powershell Steganography.

Download and extract the tool, then run it using `evil_duck.png` as the input file. The default output length is fine.

The output looks like this:

```
$out = "flag.txt"
$enc = [system.Text.Encoding]::UTF8
$string1 = "HEYWherE(IS_tNE)50uP?^DId_YOu(]E@t*mY_3RD()B2g3l?"
$string2 = "8,:8+14>Fx0l+$*KjVD>[o*.;+1|*[n&2G^201l&,Mv+_'T_B"

$data1 = $enc.GetBytes($string1)
$bytes = $enc.GetBytes($string2)

for($i=0; $i -lt $bytes.count ; $i++)
{
    $bytes[$i] = $bytes[$i] -bxor $data1[$i]
}
[System.IO.File]::WriteAllBytes("$out", $bytes)
```

Followed by gibberish.

This is clearly a Powershell Script, as the blog post said. Run the powershell script to get the flag.

flag: `	picoCTF{n1c3_job_f1nd1ng_th3_s3cr3t_in_the_im@g3}`
