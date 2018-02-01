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


def encrypt(m, e, n):
    return pow(m, e, n)


def decrypt(C, d):
    return pow(C, d, n)


p = subprocess.run(["openssl", "prime", "-generate", "-bits", "2048"], stdout=subprocess.PIPE)
q = subprocess.run(["openssl", "prime", "-generate", "-bits", "2048"], stdout=subprocess.PIPE)

e = 65537
p = int(p.stdout)
q = int(q.stdout)
n = p * q
phi_n = (p - 1) * (q - 1)
d = modInverse(e, phi_n)

m = 110101101101101101110110

C = encrypt(m, e, n)

print(C)

print(decrypt(C, d))







