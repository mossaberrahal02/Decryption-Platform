import streamlit as st
import crypto

def caesar_encrypt(message, key):
    return crypto.encrypt(message, key)

def caesar_decrypt(message, key):
    return crypto.decrypt(message, key)

def vigenere_encrypt(message, key):
    return crypto.vigenere_encrypt(message, key)

def vigenere_decrypt(message, key):
    return crypto.vigenere_decrypt(message, key)

def mod_add(a, b, m):
    return crypto.mod_add(a, b, m)

def mod_subtract(a, b, m):
    return crypto.mod_subtract(a, b, m)

def mod_multiply(a, b, m):
    return crypto.mod_multiply(a, b, m)

def mod_divide(a, b, m):
    return crypto.mod_divide(a, b, m)

def mod_inverse(a, m):
    try:
        return crypto.mod_inverse(a, m)
    except ValueError as e:
        return str(e)

def main():
    st.title("Plateforme de Cryptographie et Arithmétique Modulaire")

    st.sidebar.header("Sélectionner une méthode de chiffrement")
    method = st.sidebar.selectbox(
        "Choisir une méthode",
        ("Chiffrement de César", "Chiffrement de Vigenère", "Arithmétique Modulaire", "Inverse Modulo")
    )

    if method == "Chiffrement de César":
        st.header("Chiffrement de César")
        message = st.text_input("Entrez votre message:", "")
        key = st.number_input("Entrez la clé (nombre):", min_value=-25, max_value=25, value=3)
        
        action = st.selectbox("Choisir une action", ("Chiffrer", "Déchiffrer"))
        
        if action == "Chiffrer" and message:
            encrypted_message = caesar_encrypt(message, key)
            st.write(f"Message chiffré: {encrypted_message}")
        
        elif action == "Déchiffrer" and message:
            decrypted_message = caesar_decrypt(message, key)
            st.write(f"Message déchiffré: {decrypted_message}")

    elif method == "Chiffrement de Vigenère":
        st.header("Chiffrement de Vigenère")
        message = st.text_input("Entrez votre message:", "")
        key = st.text_input("Entrez la clé:", "")
        
        action = st.selectbox("Choisir une action", ("Chiffrer", "Déchiffrer"))
        
        if action == "Chiffrer" and message and key:
            encrypted_message = vigenere_encrypt(mnessage, key)
            st.write(f"Message chiffré: {encrypted_message}")
        
        elif action == "Déchiffrer" and message and key:
            decrypted_message = vigenere_decrypt(message, key)
            st.write(f"Message déchiffré: {decrypted_message}")

    elif method == "Arithmétique Modulaire":
        st.header("Arithmétique Modulaire")
        operation_type = st.selectbox(
            "Choisir une opération",
            ("Addition", "Soustraction", "Multiplication", "Division")
        )
        
        a = st.number_input("Entrez a:", value=0)
        b = st.number_input("Entrez b:", value=0)
        m = st.number_input("Entrez le module m:", value=1)
        
        if operation_type == "Addition":
            result = mod_add(a, b, m)
            st.write(f"({a} + {b}) % {m} = {result}")
        elif operation_type == "Soustraction":
            result = mod_subtract(a, b, m)
            st.write(f"({a} - {b}) % {m} = {result}")
        elif operation_type == "Multiplication":
            result = mod_multiply(a, b, m)
            st.write(f"({a} * {b}) % {m} = {result}")
        elif operation_type == "Division":
            result = mod_divide(a, b, m)
            st.write(f"({a} / {b}) % {m} = {result}")
    
    elif method == "Inverse Modulo":
        st.header("Inverse Modulo")
        a = st.number_input("Entrez a:", value=0)
        m = st.number_input("Entrez le module m:", value=1)
        
        if st.button("Calculer l'inverse modulo"):
            result = mod_inverse(a, m)
            st.write(f"L'inverse modulo de {a} mod {m} est: {result}")


if __name__ == "__main__":
    main()
