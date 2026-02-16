import tkinter as tk
from itertools import cycle
from PIL import Image, ImageTk
import time

root = tk.Tk()
root.title("Slideshow")

image_path = [
    r"C:\Users\lenovo\Downloads\SUBHRA.jpeg",
    r"C:\Users\lenovo\Downloads\AADHAR.jpeg",
    r"C:\Users\lenovo\Downloads\CER.jpeg",
    r"C:\Users\lenovo\Downloads\SUBHRA.jpeg"
]

image_size = (1080,1080)
images = [Image.open(path).resize(image_size) for path in image_path]
photo_images = [ImageTk.PhotoImage(image) for image in images]


label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_path)):
        update_image()

button = tk.Button(root, text="Play Button", command=start_slideshow)
button.pack()

root.mainloop()