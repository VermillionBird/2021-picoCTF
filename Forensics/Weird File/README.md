# Weird File
### Author: 
### Forensics: 20 points

 What could go wrong if we let Word documents run programs? (aka "in-the-clear").[weird.docm](weird.docm).

---

You can use `olevba` from the `oletools` python package to view any macros in the word doc. `olevba -c weird.docm` outputs the following:

```
olevba 0.56 on Python 3.9.1 - http://decalage.info/python/oletools
===============================================================================
FILE: weird.docm
Type: OpenXML
WARNING  For now, VBA stomping cannot be detected for files in memory
-------------------------------------------------------------------------------
VBA MACRO ThisDocument.cls 
in file: word/vbaProject.bin - OLE stream: 'VBA/ThisDocument'
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Sub AutoOpen()
    MsgBox "Macros can run any program", 0, "Title"
    Signature

End Sub
 
 Sub Signature()
    Selection.TypeText Text:="some text"
    Selection.TypeParagraph
    
 End Sub
 
 Sub runpython()

Dim Ret_Val
Args = """" '"""
Ret_Val = Shell("python -c 'print(\"cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9\")'" & " " & Args, vbNormalFocus)
If Ret_Val = 0 Then
   MsgBox "Couldn't run python script!", vbOKOnly
End If
End Sub
```

The string in the print statement is the base64 encoded flag.

flag: `picoCTF{m4cr0s_r_d4ng3r0us}`
