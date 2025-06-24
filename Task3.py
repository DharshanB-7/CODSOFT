import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import random

captions = [
    "A beautiful scenery with mountains.",
    "A dog is playing in the park.",
    "A person is standing near a car.",
    "An empty street with buildings around.",
    "A cat is sitting on a chair.",
    "A group of people walking outdoors.",
    "A sunset view behind the trees.",
    "A food item served on a plate.",
    "A beach with waves hitting the shore.",
    "A bird flying in the blue sky."
]

def generate_caption():
    return random.choice(captions)

class CaptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Captioning")
        self.root.geometry("600x500")

        self.label = tk.Label(root, text="Upload an image to get a caption", font=("Arial", 14))
        self.label.pack(pady=10)

        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack()

        self.caption_label = tk.Label(root, text="", font=("Arial", 12), wraplength=500)
        self.caption_label.pack(pady=10)

        self.button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.button.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return

        image = Image.open(file_path).resize((400, 300))
        self.tk_image = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)

        caption = generate_caption()
        self.caption_label.config(text=caption)

if __name__ == "__main__":
    root = tk.Tk()
    app = CaptionApp(root)
    root.mainloop()
