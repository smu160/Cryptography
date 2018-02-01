#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 17:17:57 2018

@author: saveliyyusufov
"""
import math
import binascii
import subprocess

def isPrime(n):
    limit = int(math.sqrt(n))
    for i in range(2, limit+1):
        if (n % i == 0):
            return False
        
    return True


def ecnrypt(m, e, n):
    return pow(m, e, n)


def decrypt(C, d):
    return pow(C, d)


p = subprocess.run(["openssl", "prime", "-generate", "-bits", "2048"], stdout=subprocess.PIPE)
q = subprocess.run(["openssl", "prime", "-generate", "-bits", "2048"], stdout=subprocess.PIPE)
# print(str(result))



