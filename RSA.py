#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 17:17:57 2018

@author: saveliyyusufov
"""

import subprocess


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modInverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def ecnrypt(m, e, n):
    return pow(m, e, n)


def decrypt(C, d):
    return pow(C, d)


p = subprocess.run(["openssl", "prime", "-generate", "-bits", "2048"], stdout=subprocess.PIPE)
q = subprocess.run(["openssl", "prime", "-generate", "-bits", "2048"], stdout=subprocess.PIPE)

e = 65537
p = int(p.stdout)
q = int(q.stdout)
n = p * q
phi_n = (p - 1) * (q - 1)
d = modInverse(e, phi_n)

m = 5356858

C = pow(m, e, n)

print(pow(C, d, n))







