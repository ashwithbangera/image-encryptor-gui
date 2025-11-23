import base64
from cryptography.fernet import Fernet
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image

# ---- Key Generation ---- #
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("Key Generated", "Encryption key saved as secret.key")

# ---- Load Key ---- #
def load_key():
    return open("secret.key", "rb").read()

# ---- Encrypt Image ---- #
def encrypt_image():
    try:
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        key = load_key()
        fernet = Fernet(key)

        with open(file_path, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)

        with open("encrypted.img", "wb") as enc_file:
            enc_file.write(encrypted)

        messagebox.showinfo("Success", "Image encrypted as encrypted.img")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---- Decrypt Image ---- #
def decrypt_image():
    try:
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        key = load_key()
        fernet = Fernet(key)

        with open(file_path, "rb") as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)

        with open("decrypted.png", "wb") as dec_file:
            dec_file.write(decrypted)

        messagebox.showinfo("Success", "Image decrypted as decrypted.png")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---- GUI ---- #
root = Tk()
root.title("Image Encryptor GUI")
root.geometry("350x250")

Label(root, text="Image Encryption Tool", font=("Arial", 16, "bold")).pack(pady=10)

Button(root, text="Generate Key", command=generate_key, width=20).pack(pady=5)
Button(root, text="Encrypt Image", command=encrypt_image, width=20).pack(pady=5)
Button(root, text="Decrypt Image", command=decrypt_image, width=20).pack(pady=5)

root.mainloop()
