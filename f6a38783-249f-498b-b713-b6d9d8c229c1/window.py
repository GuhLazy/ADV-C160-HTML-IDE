from tkinter import * 
root = Tk()
from PIL import Image, ImageTk
import os
from tkinter import filedialog

root.title("Html_ide")
root.minsize(500,500)
root.maxsize(1000,1000)
root.config(background="light_pink")

exit_img = ImageTk.PhotoImage(Image.open("exit.jpg"))
open_img = ImageTk.PhotoImage(Image.open("open.png"))
save_img = ImageTk.PhotoImage(Image.open("save.png"))

label = Label(root, text="File name")
label.place(relx=0.28, rely=0.03, anchor=CENTER)

text_input = Entry(root)
text_input.place(relx=0.46, rely=0.3, anchor=CENTER)

text_area = Text(root, width=80, height=35)
text_area.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()