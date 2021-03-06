#!/usr/bin/env python
# -*- coding: utf-8 -*-
# System specific encoding and decoding
#


import sys

def system_encode(s):
    charset = sys.stdout.encoding
    return s.encode(charset, 'ignore')

def system_decode(s):
    charset = sys.stdout.encoding
    return s.decode(charset, 'ignore')