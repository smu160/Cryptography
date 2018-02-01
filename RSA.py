import subprocess
import binascii


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modInverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception("Modular inverse does not exist for {} {}".format(a, m))
    else:
        return x % m


def encrypt(m, e, n):
    return pow(m, e, n)


def decrypt(C, d, n):
    return pow(C, d, n)


p = subprocess.run(["openssl", "prime", "-generate", "-bits", "2048"], stdout=subprocess.PIPE)
q = subprocess.run(["openssl", "prime", "-generate", "-bits", "2048"], stdout=subprocess.PIPE)

e = 65537
p = int(p.stdout)
q = int(q.stdout)
n = p * q
phi_n = (p - 1) * (q - 1)
d = modInverse(e, phi_n)

message = input()
message_bytes = message.encode('utf-8')
h = binascii.hexlify(message_bytes)
encoded_message = int(h, 16)
print("message = {}\n".format(encoded_message))

cipher_text = encrypt(encoded_message, e, n)
print("ciphertext = {}\n".format(cipher_text))

decrypted = decrypt(cipher_text, d, n)
h2 = hex(decrypted)
h3 = h2[2:]
b2 = h3.encode('ascii')
b3 = binascii.unhexlify(b2)
plaintext = b3.decode('utf-8')

print("plaintext = {}\n".format(plaintext))








