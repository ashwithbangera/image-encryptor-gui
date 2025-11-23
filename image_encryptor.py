import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import random


# ---------------------------
# Pixel Manipulation Functions
# ---------------------------

def swap_pixels(img, key):
    """Shuffle pixels using a deterministic random key."""
    w, h = img.size
    pixels = list(img.getdata())

    rng = random.Random()
    rng.seed(key)

    indices = list(range(len(pixels)))
    rng.shuffle(indices)

    shuffled = [None] * len(pixels)
    for i, idx in enumerate(indices):
        shuffled[i] = pixels[idx]

    out = Image.new(img.mode, img.size)
    out.putdata(shuffled)
    return out


def inverse_swap_pixels(img, key):
    """Reverse the shuffle done by swap_pixels."""
    w, h = img.size
    pixels = list(img.getdata())

    rng = random.Random()
    rng.seed(key)

    indices = list(range(len(pixels)))
    rng.shuffle(indices)

    out_pixels = [None] * len(pixels)
    for i, idx in enumerate(indices):
        out_pixels[idx] = pixels[i]

    out = Image.new(img.mode, img.size)
    out.putdata(out_pixels)
    return out


def math_op(img, key, op):
    """Add/Sub/Mul operations for each RGB pixel."""
    if img.mode not in ("RGB", "RGBA"):
        img = img.convert("RGB")

    data = list(img.getdata())
    out = []

    for px in data:
        r, g, b = px[:3]

        if op == "add":
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256

        elif op == "sub":
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256

        elif op == "mul":
            r = (r * key) % 256
            g = (g * key) % 256
            b = (b * key) % 256

        if len(px) == 4:
            out.append((r, g, b, px[3]))
        else:
            out.append((r, g, b))

    new_img = Image.new(img.mode, img.size)
    new_img.putdata(out)
    return new_img


# ---------------------------
# GUI Application
# ---------------------------

class ImageEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Encryption Tool")

        self.img = None
        self.display_img = None

        frame = tk.Frame(root)
        frame.pack(padx=10, pady=10)

        tk.Button(frame, text="Open Image", command=self.open_image).grid(row=0, column=0)

        tk.Label(frame, text="Key (text or number):").grid(row=1, column=0, sticky="w")
        self.key_entry = tk.Entry(frame)
        self.key_entry.grid(row=1, column=1)

        tk.Label(frame, text="Numeric Key (for math ops):").grid(row=2, column=0, sticky="w")
        self.num_key_entry = tk.Entry(frame)
        self.num_key_entry.insert(0, "7")
        self.num_key_entry.grid(row=2, column=1)

        tk.Button(frame, text="Swap Pixels (Encrypt)", command=self.encrypt_swap).grid(row=3, column=0)
        tk.Button(frame, text="Unswap Pixels (Decrypt)", command=self.decrypt_swap).grid(row=3, column=1)

        tk.Button(frame, text="Add (Encrypt)", command=lambda: self.apply_math("add")).grid(row=4, column=0)
        tk.Button(frame, text="Subtract (Decrypt)", command=lambda: self.apply_math("sub")).grid(row=4, column=1)
        tk.Button(frame, text="Multiply", command=lambda: self.apply_math("mul")).grid(row=5, column=0)

        tk.Button(frame, text="Save Image", command=self.save_image).grid(row=6, column=0, columnspan=2, pady=5)

        self.canvas = tk.Canvas(root, width=500, height=400, bg="lightgray")
        self.canvas.pack()

    def open_image(self):
        path = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg *.jpeg *.bmp")])
        if not path:
            return
        self.img = Image.open(path).convert("RGBA")
        self.show_image(self.img)

    def show_image(self, img):
        w, h = img.size
        max_w, max_h = 500, 400
        scale = min(max_w / w, max_h / h, 1)
        resized = img.resize((int(w * scale), int(h * scale)))
        self.display_img = ImageTk.PhotoImage(resized)
        self.canvas.delete("all")
        self.canvas.create_image(250, 200, image=self.display_img)

    def get_key(self):
        key = self.key_entry.get()
        if key.strip() == "":
            messagebox.showerror("Error", "Enter a key!")
            return None
        try:
            return int(key)
        except:
            return sum(ord(c) for c in key)

    def get_num_key(self):
        try:
            return int(self.num_key_entry.get())
        except:
            messagebox.showerror("Error", "Numeric key must be an integer")
            return None

    def encrypt_swap(self):
        key = self.get_key()
        if key is None or self.img is None:
            return
        self.img = swap_pixels(self.img, key)
        self.show_image(self.img)

    def decrypt_swap(self):
        key = self.get_key()
        if key is None or self.img is None:
            return
        self.img = inverse_swap_pixels(self.img, key)
        self.show_image(self.img)

    def apply_math(self, op):
        key = self.get_num_key()
        if key is None or self.img is None:
            return
        self.img = math_op(self.img, key, op)
        self.show_image(self.img)

    def save_image(self):
        if not self.img:
            messagebox.showerror("Error", "No image to save!")
            return
        path = filedialog.asksaveasfilename(defaultextension=".png")
        if not path:
            return
        self.img.save(path)
        messagebox.showinfo("Saved", "Image saved successfully!")


# ---------------------------
# Run app
# ---------------------------

if __name__ == "__main__":
    root = tk.Tk()
    ImageEncryptorApp(root)
    root.mainloop()

