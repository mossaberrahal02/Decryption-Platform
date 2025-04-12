# caesar.py

import math

# Caesar Cipher functions
def encrypt(message, key):
    """
    Encrypts the message using Caesar Cipher.
    """
    encrypted_message = ""
    for char in message:
        if char.isalpha():  # Only encrypt alphabetic characters
            shift = 65 if char.isupper() else 97  # For uppercase or lowercase
            encrypted_message += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_message += char  # Non-alphabet characters are unchanged
    return encrypted_message

def decrypt(message, key):
    """
    Decrypts the message using Caesar Cipher.
    """
    return encrypt(message, -key)  # Decrypt is just encryption with the negative key

# Vigenère Cipher functions
def vigenere_encrypt(message, key):
    """
    Encrypts the message using Vigenère Cipher.
    """
    encrypted_message = ""
    key = key.lower()
    key_index = 0

    for char in message:
        if char.isalpha():  # Only encrypt alphabetic characters
            shift = 65 if char.isupper() else 97  # For uppercase or lowercase
            key_char = key[key_index % len(key)]
            key_shift = ord(key_char) - 97
            encrypted_message += chr((ord(char) - shift + key_shift) % 26 + shift)
            key_index += 1
        else:
            encrypted_message += char  # Non-alphabet characters are unchanged
    return encrypted_message

def vigenere_decrypt(message, key):
    """
    Decrypts the message using Vigenère Cipher.
    """
    decrypted_message = ""
    key = key.lower()
    key_index = 0

    for char in message:
        if char.isalpha():  # Only decrypt alphabetic characters
            shift = 65 if char.isupper() else 97  # For uppercase or lowercase
            key_char = key[key_index % len(key)]
            key_shift = ord(key_char) - 97
            decrypted_message += chr((ord(char) - shift - key_shift) % 26 + shift)
            key_index += 1
        else:
            decrypted_message += char  # Non-alphabet characters are unchanged
    return decrypted_message

# Modular Arithmetic Functions
def mod_add(a, b, m):
    """Returns (a + b) % m"""
    return (a + b) % m

def mod_subtract(a, b, m):
    """Returns (a - b) % m"""
    return (a - b) % m

def mod_multiply(a, b, m):
    """Returns (a * b) % m"""
    return (a * b) % m

def mod_divide(a, b, m):
    """Returns (a / b) % m. This is a * mod_inverse(b, m) % m"""
    return mod_multiply(a, mod_inverse(b, m), m)

# Extended Euclidean Algorithm to find modular inverse
def extended_gcd(a, b):
    """
    Returns the gcd of a and b, along with the coefficients of Bézout's identity
    (i.e., x and y such that ax + by = gcd(a, b))
    """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

def mod_inverse(a, m):
    """Returns the modular inverse of a under modulo m, if it exists"""
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError(f"No modular inverse for {a} mod {m}.")
    else:
        return x % m
