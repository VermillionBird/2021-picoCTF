# Nice netcat...
### Author: Syreal
### General Skills: 15 points


There is a nice program that you can talk to by using this command in a shell: `$ nc mercury.picoctf.net 49039`, but it doesn't speak English...

---

Connect to the program with the provided netcat command to receive the following output:

```
112 
105 
99 
111 
67 
84 
70 
123 
103 
48 
48 
100 
95 
107 
49 
116 
116 
121 
33 
95 
110 
49 
99 
51 
95 
107 
49 
116 
116 
121 
33 
95 
51 
100 
56 
52 
101 
100 
99 
56 
125 
10
```

This looks like decimal ascii codes, converting gives you the flag.

flag: `picoCTF{g00d_k1tty!_n1c3_k1tty!_3d84edc8}`
