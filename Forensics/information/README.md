# information
### Author: Susie
### Forensics: 10 points

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](cat.jpg)

---

The title probably refers to the metadata of the provided image. Checking it with `exiftool` gives an interesting entry in the License section:

```
License                         : cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9
```

This looks like base64. Decrypt it to get the flag.

flag: `picoCTF{the_m3tadata_1s_modified}`
