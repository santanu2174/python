from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root=tk.Tk()
root.title("Image Slide Show")

#List of  Image Path
image_path = [
    r"C:\Users\lenovo\Downloads\SUBHRA.jpeg",
    r"C:\Users\lenovo\Downloads\AADHAR.jpeg",
    r"C:\Users\lenovo\Downloads\CER.jpeg",
    r"C:\Users\lenovo\Downloads\SUBHRA.jpeg"
]

#Resize images to 1080x1080
image_size = (1080,1080)
images = [Image.open(path).resize(image_size) for path in image_path]
photo_images=[ImageTk.PhotoImage(image) for image in images]

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

play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack()

root.mainloop()