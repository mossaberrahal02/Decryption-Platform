import math

def encrypt(message, key):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, key):
    return encrypt(message, -key)

def vigenere_encrypt(message, key):
    encrypted_message = ""
    key = key.lower()
    key_index = 0

    for char in message:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            key_char = key[key_index % len(key)]
            key_shift = ord(key_char) - 97
            encrypted_message += chr((ord(char) - shift + key_shift) % 26 + shift)
            key_index += 1
        else:
            encrypted_message += char
    return encrypted_message

def vigenere_decrypt(message, key):
    decrypted_message = ""
    key = key.lower()
    key_index = 0

    for char in message:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            key_char = key[key_index % len(key)]
            key_shift = ord(key_char) - 97
            decrypted_message += chr((ord(char) - shift - key_shift) % 26 + shift)
            key_index += 1
        else:
            decrypted_message += char
    return decrypted_message

def mod_add(a, b, m):
    return (a + b) % m

def mod_subtract(a, b, m):
    return (a - b) % m

def mod_multiply(a, b, m):
    return (a * b) % m

def mod_divide(a, b, m):
    return mod_multiply(a, mod_inverse(b, m), m)

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"ya pas d'inverse modulaire pour {a} mod {m}.")
    else:
        return x % m
