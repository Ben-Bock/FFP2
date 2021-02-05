# -*- coding: utf-8 -*-
#  FFP2
#  ---------------
#  A library for File-Finger-Prints (FFP)
#
#  Author:  Ben Bock (benbock@live.de)           
#  Website: https://github.com/Ben-Bock/FFP2
#  License: MIT (see LICENSE file)
# 
# based on a great post on https://stackoverflow.com/questions/22058048/hashing-a-file-in-python/44873382
#

import hashlib


def Filefingerprint(filepath='', buffersize=65536):

    md5 = hashlib.md5()
    with open(filepath, 'rb') as f:
        while True:
            data = f.read(buffersize)
            if not data:
                break
            md5.update(data)
    return (md5.hexdigest())
