# FFP2
Simple library to generate File-Fingerprints (hashes over content to compare files or check for changes) 

---------------------------------------------

FFP2 can help you to generate fingerprint (hashes) over the content of files. Wiht that you can easily check
if 2 different files have the very same content or if the content of a file was modified.

Installation
-------------------------------

```console
$ pip install ffp2
```

Usage
-----------------------
```pycon
>>> from ffp2 import Filefingerprint
>>> fingerprint = Filefingerprint('FilepathGoesHere')
>>> print (fingerprint)

```
