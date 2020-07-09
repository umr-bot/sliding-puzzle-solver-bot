 ### Basic NxN sliding puzzle solver 
from puzzle_generator import puzzle as puzzle
import numpy as np 
from pynput.keyboard import Key, Listener
#from threading import Thread
import tkinter as tk
from PIL import ImageTk, Image

puz = puzzle()
arr = puz.blocks
# function to be called when 
# keyboard buttons are pressed 
def key_press(event): 
    key = event.char
    if(key == 'w'): puz.transpose('up')
    if(key == 's'): puz.transpose('down')
    if(key == 'a'): puz.transpose('left')
    if(key == 'd'): puz.transpose('right')
    print(key, 'is pressed') 
    base_path = "number images/"
    photo_val = 1
    for i in range(4):
        for j in range(4):
            num_photo = np.where(arr == photo_val)[0][0]
            path = base_path + str(num_photo+1) + ".png"

            im = Image.open(path) # PIL image
            tkimage = ImageTk.PhotoImage(im) # tk converted image from PIL image
            panel = tk.Label(root, image=tkimage) # handle and binding of tkimage to root
            panel.image = tkimage # set the panels image to tkimage

            x = (j%4)*50
            y = (i%4)*50
            panel.place(x=x,y=y)
            photo_val += 1

root = tk.Tk()
root.title("Join")
root.geometry("500x500")
#root.configure(background='')
#img  = Image.open("number images/blank_image.png")
base_path = "number images/"
photo_val = 1
for i in range(4):
    for j in range(4):
        num_photo = np.where(arr == photo_val)[0][0]
        path = base_path + str(num_photo+1) + ".png"
        
        im = Image.open(path) # PIL image
        tkimage = ImageTk.PhotoImage(im) # tk converted image from PIL image
        panel = tk.Label(root, image=tkimage) # handle and binding of tkimage to root
        panel.image = tkimage # set the panels image to tkimage

        x = (j%4)*50
        y = (i%4)*50
        panel.place(x=x,y=y)
        photo_val += 1

#Saved in the same relative location
#img.save("pasted_picture.png")

# here we are binding keyboard
# with the main window
root.bind('<Key>', lambda a : key_press(a))

root.wm_title("Sliding puzzle solver")
root.mainloop()


