# -*- coding: utf-8 -*-

#  FFP2
#  ---------------
#  A library for File-Finger-Prints (FFP)
#
#  Author:  Ben Bock (benbock@live.de)           
#  Website: https://github.com/Ben-Bock/FFP2
#  License: MIT (see LICENSE file)

from ffp2 import Filefingerprint

fingerprint = Filefingerprint('./LICENSE')
print(fingerprint)
