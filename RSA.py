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

def encode(m):
    message_bytes = message.encode("utf-8")
    hexlifyed_message = binascii.hexlify(message_bytes)
    encoded_message = int(hexlifyed_message, 16)
    return encoded_message

def decode(encoded_message):
    h2 = hex(encoded_message)
    h3 = h2[2:]
    b2 = h3.encode("ascii")
    b3 = binascii.unhexlify(b2)
    message = b3.decode("utf-8")
    return message

if __name__ == "__main__":

    p = subprocess.run(["openssl", "prime", "-generate", "-bits", "2048"], stdout=subprocess.PIPE)
    q = subprocess.run(["openssl", "prime", "-generate", "-bits", "2048"], stdout=subprocess.PIPE)

    e = 65537
    p = int(p.stdout)
    q = int(q.stdout)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = modInverse(e, phi_n)

    message = input()
    encoded_message = encode(message)
    print("encoded message = {}\n".format(encoded_message))

    cipher_text = encrypt(encoded_message, e, n)
    print("ciphertext = {}\n".format(cipher_text))

    decrypted_message = decrypt(cipher_text, d, n)
    plaintext_message = decode(decrypted_message)
    print("plaintext message = {}".format(plaintext_message))
