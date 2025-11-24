🖼️ Image Encryptor GUI (Python + Tkinter)

A simple and beginner-friendly Image Encryption Tool built using Python, Tkinter, and Pillow (PIL).  
This tool encrypts and decrypts images using pixel manipulation techniques such as:

- Swapping pixel RGB values  
- Applying reversible mathematical transformations  
- Simple, understandable encryption logic  

This project is perfect for:
- Cybersecurity beginners  
- Python learners  
- College or internship projects  
- GitHub portfolio building  

---

## 🚀 Features

✔ Load any image (JPG, PNG, JPEG)  
✔ Encrypt the image using pixel transformation  
✔ Decrypt the encrypted image  
✔ Save encrypted/decrypted images  
✔ GUI built using Tkinter  
✔ Beginner-friendly codebase  
✔ No complex cryptography — only pixel math  

---

## 🔐 How Encryption Works

This tool performs basic reversible operations:

### 🔸 1. Swap Red ↔ Blue channels
(R, G, B) → (B, G, R)

### 🔸 2. Add a secret key value  
R = (R + key) % 256
G = (G + key) % 256
B = (B + key) % 256

### 🔸 3. Decryption reverses both operations  
Because the operations are reversible, the original image can be perfectly restored.

> ❗ Note: This is not meant for strong cryptography — it's for learning pixel manipulation + encryption concepts.

## 📦 Installation

1. Clone the repository
bash
git clone https://github.com/<your-username>/image-encryptor-gui.git
cd image-encryptor-gui

2. Create a virtual environment
bash
python3 -m venv venv
source venv/bin/activate

3. Install the required dependency
bash
pip install pillow
(Or if you have a requirements file)
bash
pip install -r requirements.txt

▶️ How to Run
bash
python image_encryptor.py
The GUI window will open.


