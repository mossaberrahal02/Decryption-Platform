import tkinter as tk
from tkinter import ttk, messagebox
import math

class DecrypteurApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Décrypteur de Messages")
        self.root.geometry("700x550")
        self.root.configure(bg="#f0f0f0")
        self.root.resizable(True, True)
        
        # Style
        self.style = ttk.Style()
        self.style.configure("TButton", font=("Arial", 11), padding=10)
        self.style.configure("TLabel", font=("Arial", 12), background="#f0f0f0")
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TNotebook", background="#f0f0f0")
        self.style.configure("TNotebook.Tab", font=("Arial", 11, "bold"), padding=[20, 10])
        
        # Création du système d'onglets
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Création des pages pour chaque algorithme
        self.creer_page_cesar()
        self.creer_page_vigenere()
        self.creer_page_arith_mod()
        self.creer_page_inverse_mod()
    
    def creer_interface_commune(self, frame):
        """Crée l'interface commune à toutes les pages"""
        # Frame d'entrée
        input_frame = ttk.Frame(frame, padding=10)
        input_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        ttk.Label(input_frame, text="Message chiffré:").pack(anchor=tk.W, pady=5)
        text_input = tk.Text(input_frame, height=5, width=60, font=("Arial", 12))
        text_input.pack(fill=tk.BOTH, expand=True)
        
        # Frame de sortie
        output_frame = ttk.Frame(frame, padding=10)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        ttk.Label(output_frame, text="Résultat du déchiffrement:").pack(anchor=tk.W, pady=5)
        text_output = tk.Text(output_frame, height=5, width=60, font=("Arial", 12), bg="#e8f4f8")
        text_output.pack(fill=tk.BOTH, expand=True)
        
        return input_frame, text_input, output_frame, text_output
    
    def creer_page_cesar(self):
        # Création de la page César
        self.cesar_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.cesar_frame, text="César")
        
        # Interface commune
        input_frame, self.cesar_input, output_frame, self.cesar_output = self.creer_interface_commune(self.cesar_frame)
        
        # Paramètres spécifiques à César
        param_frame = ttk.Frame(input_frame)
        param_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(param_frame, text="Décalage (clé):").pack(side=tk.LEFT, padx=5)
        self.cesar_key = ttk.Entry(param_frame, width=10, font=("Arial", 12))
        self.cesar_key.pack(side=tk.LEFT, padx=5)
        self.cesar_key.insert(0, "3")  # Valeur par défaut
        
        # Bouton de déchiffrement
        ttk.Button(self.cesar_frame, text="Déchiffrer", command=self.dechiffrer_cesar, 
                  style="TButton").pack(pady=10)
    
    def creer_page_vigenere(self):
        # Création de la page Vigenère
        self.vigenere_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.vigenere_frame, text="Vigenère")
        
        # Interface commune
        input_frame, self.vigenere_input, output_frame, self.vigenere_output = self.creer_interface_commune(self.vigenere_frame)
        
        # Paramètres spécifiques à Vigenère
        param_frame = ttk.Frame(input_frame)
        param_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(param_frame, text="Clé (mot):").pack(side=tk.LEFT, padx=5)
        self.vigenere_key = ttk.Entry(param_frame, width=20, font=("Arial", 12))
        self.vigenere_key.pack(side=tk.LEFT, padx=5)
        self.vigenere_key.insert(0, "CLE")  # Valeur par défaut
        
        # Bouton de déchiffrement
        ttk.Button(self.vigenere_frame, text="Déchiffrer", command=self.dechiffrer_vigenere, 
                  style="TButton").pack(pady=10)
    
    def creer_page_arith_mod(self):
        # Création de la page Arithmétique Modulaire
        self.arith_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.arith_frame, text="Arithmétique Modulaire")
        
        # Interface commune
        input_frame, self.arith_input, output_frame, self.arith_output = self.creer_interface_commune(self.arith_frame)
        
        # Paramètres spécifiques à l'arithmétique modulaire
        param_frame = ttk.Frame(input_frame)
        param_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(param_frame, text="Clé:").pack(side=tk.LEFT, padx=5)
        self.arith_key = ttk.Entry(param_frame, width=10, font=("Arial", 12))
        self.arith_key.pack(side=tk.LEFT, padx=5)
        self.arith_key.insert(0, "5")  # Valeur par défaut
        
        ttk.Label(param_frame, text="Modulo:").pack(side=tk.LEFT, padx=5)
        self.arith_mod = ttk.Entry(param_frame, width=10, font=("Arial", 12))
        self.arith_mod.pack(side=tk.LEFT, padx=5)
        self.arith_mod.insert(0, "26")  # Valeur par défaut
        
        # Bouton de déchiffrement
        ttk.Button(self.arith_frame, text="Déchiffrer", command=self.dechiffrer_arithmetique_modulaire, 
                  style="TButton").pack(pady=10)
    
    def creer_page_inverse_mod(self):
        # Création de la page Inverse Modulo
        self.inverse_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.inverse_frame, text="Inverse Modulo")
        
        # Interface commune
        input_frame, self.inverse_input, output_frame, self.inverse_output = self.creer_interface_commune(self.inverse_frame)
        
        # Paramètres spécifiques à l'inverse modulo
        param_frame = ttk.Frame(input_frame)
        param_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(param_frame, text="Clé:").pack(side=tk.LEFT, padx=5)
        self.inverse_key = ttk.Entry(param_frame, width=10, font=("Arial", 12))
        self.inverse_key.pack(side=tk.LEFT, padx=5)
        self.inverse_key.insert(0, "7")  # Valeur par défaut
        
        ttk.Label(param_frame, text="Modulo:").pack(side=tk.LEFT, padx=5)
        self.inverse_mod = ttk.Entry(param_frame, width=10, font=("Arial", 12))
        self.inverse_mod.pack(side=tk.LEFT, padx=5)
        self.inverse_mod.insert(0, "26")  # Valeur par défaut
        
        # Informations sur la méthode
        info_frame = ttk.Frame(self.inverse_frame, padding=5)
        info_frame.pack(fill=tk.X, padx=10, pady=0)
        ttk.Label(info_frame, text="Note: La clé doit avoir un inverse modulo valide", 
                 font=("Arial", 10, "italic")).pack(anchor=tk.W)
        
        # Bouton de déchiffrement
        ttk.Button(self.inverse_frame, text="Déchiffrer", command=self.dechiffrer_inverse_modulo, 
                  style="TButton").pack(pady=10)
    
    def dechiffrer_cesar(self):
        try:
            message = self.cesar_input.get("1.0", tk.END).strip()
            if not message:
                messagebox.showwarning("Attention", "Veuillez entrer un message à déchiffrer")
                return
                
            decalage = int(self.cesar_key.get())
            
            resultat = ""
            for char in message:
                if char.isalpha():
                    ascii_offset = ord('A') if char.isupper() else ord('a')
                    # Déchiffrement César: shift dans la direction opposée
                    resultat += chr((ord(char) - ascii_offset - decalage) % 26 + ascii_offset)
                else:
                    resultat += char
            
            self.cesar_output.delete("1.0", tk.END)
            self.cesar_output.insert("1.0", resultat)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du déchiffrement César: {str(e)}")
    
    def dechiffrer_vigenere(self):
        try:
            message = self.vigenere_input.get("1.0", tk.END).strip()
            if not message:
                messagebox.showwarning("Attention", "Veuillez entrer un message à déchiffrer")
                return
                
            cle = self.vigenere_key.get().upper()
            
            if not cle:
                messagebox.showwarning("Attention", "Veuillez entrer une clé")
                return
            
            resultat = ""
            i = 0
            
            for char in message:
                if char.isalpha():
                    # Obtenir le décalage à partir de la lettre de la clé
                    cle_char = cle[i % len(cle)]
                    decalage = ord(cle_char) - ord('A')
                    
                    # Déchiffrement
                    ascii_offset = ord('A') if char.isupper() else ord('a')
                    resultat += chr((ord(char) - ascii_offset - decalage) % 26 + ascii_offset)
                    
                    i += 1
                else:
                    resultat += char
            
            self.vigenere_output.delete("1.0", tk.END)
            self.vigenere_output.insert("1.0", resultat)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du déchiffrement Vigenère: {str(e)}")
    
    def dechiffrer_arithmetique_modulaire(self):
        try:
            message = self.arith_input.get("1.0", tk.END).strip()
            if not message:
                messagebox.showwarning("Attention", "Veuillez entrer un message à déchiffrer")
                return
                
            modulo = int(self.arith_mod.get())
            key = int(self.arith_key.get())
            
            resultat = ""
            for char in message:
                if char.isalpha():
                    # Convertir lettre en nombre (0-25)
                    ascii_offset = ord('A') if char.isupper() else ord('a')
                    num = ord(char) - ascii_offset
                    
                    # Appliquer l'arithmétique modulaire
                    new_num = (num - key) % modulo
                    
                    # Convertir nombre en lettre
                    resultat += chr(new_num + ascii_offset)
                else:
                    resultat += char
            
            self.arith_output.delete("1.0", tk.END)
            self.arith_output.insert("1.0", resultat)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du déchiffrement par Arithmétique Modulaire: {str(e)}")
    
    def dechiffrer_inverse_modulo(self):
        try:
            message = self.inverse_input.get("1.0", tk.END).strip()
            if not message:
                messagebox.showwarning("Attention", "Veuillez entrer un message à déchiffrer")
                return
                
            modulo = int(self.inverse_mod.get())
            key = int(self.inverse_key.get())
            
            # Vérifier si la clé a un inverse modulaire
            inverse = self.trouver_inverse_modulaire(key, modulo)
            if inverse is None:
                messagebox.showerror("Erreur", f"La clé {key} n'a pas d'inverse modulo {modulo}")
                return
            
            resultat = ""
            for char in message:
                if char.isalpha():
                    # Convertir lettre en nombre (0-25)
                    ascii_offset = ord('A') if char.isupper() else ord('a')
                    num = ord(char) - ascii_offset
                    
                    # Appliquer l'inverse modulaire
                    new_num = (num * inverse) % modulo
                    
                    # Convertir nombre en lettre
                    resultat += chr(new_num + ascii_offset)
                else:
                    resultat += char
            
            self.inverse_output.delete("1.0", tk.END)
            self.inverse_output.insert("1.0", resultat)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors du déchiffrement par Inverse Modulo: {str(e)}")
    
    def trouver_inverse_modulaire(self, a, m):
        # Algorithme d'Euclide étendu pour trouver l'inverse modulaire
        for x in range(1, m):
            if (a * x) % m == 1:
                return x
        return None

# Lancement de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = DecrypteurApp(root)
    root.mainloop()