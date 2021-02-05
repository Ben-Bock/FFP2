# -*- coding: utf-8 -*-

#  FFP2
#  ---------------
#  A library for File-Finger-Prints (FFP)
#
#  Author:  Ben Bock (benbock@live.de)         
#  Website: https://github.com/Ben-Bock/FFP2
#  License: MIT (see LICENSE file)

import os
import unittest
from glob import glob
from flake8.api import legacy as flake8

import ffp2


class TestFlake8(unittest.TestCase):

    def test_flake8(self):
        """Test that we conform to PEP-8."""
        self.style_guide = flake8.get_style_guide(ignore=['I', 'F401', 'W504'])
        self.py_files = [y for x in os.walk(os.path.abspath('ffp2')) for y in glob(os.path.join(x[0], '*.py'))]
        self.report = self.style_guide.check_files(self.py_files)
        self.assertEqual(self.report.get_statistics('E'), [])


class TestBasics(unittest.TestCase):

    def test_get(self):
        self.assertEqual(
                        ffp2.Filefingerprint('./LICENSE'), 
                        'daaef2174018b4265d901d4a52333cf7')


if __name__ == "__main__":
    unittest.main()