 ### Basic NxN sliding puzzle solver 
from puzzle_generator import puzzle as puzzle
import numpy as np 
#from pynput.keyboard import Key, Listener
#from threading import Thread
import tkinter as tk
from PIL import ImageTk, Image
N = 3
puz = puzzle(N=N)
state = ['3', '7', '5', '6', '8', '1', '9', '2', '4']
state = np.array(state).astype(int)
puz.generate_puzzle(state)
up,down,left,right = 0,1,2,3
class cnt(): 
    def __init__(self, initial_value=0):
        self.num = initial_value
cnt = cnt()
###########################################################################
# function to be called when 
# keyboard buttons are pressed 
def key_press(event): 
    key = event.char
    if(key == 'w'): puz.transpose(up)
    if(key == 's'): puz.transpose(down)
    if(key == 'a'): puz.transpose(left)
    if(key == 'd'): puz.transpose(right)
    if(key == 'q'): 
        root.destroy()
        return # return to after root.mainloop() if successfully exited
    #print(key, 'is pressed')
    print("state",cnt.num)
    print(puz.blocks.reshape(3,3))
    base_path = "number images/"
    photo_val = 0
    for i in range(N):
        y = i*50
        for j in range(N):
            #num_photo = np.where(puz.blocks == photo_val)[0][0]
            #print("num_photo",num_photo)
            photo = puz.blocks[photo_val]
            path = base_path + str(photo) + ".png"

            im = Image.open(path) # PIL image
            tkimage = ImageTk.PhotoImage(im) # tk converted image from PIL image
            panel = tk.Label(root, image=tkimage) # handle and binding of tkimage to root
            panel.image = tkimage # set the panels image to tkimage

            x = j*50 # paste image colum by column, from left to right
            panel.place(x=x,y=y)
            photo_val += 1
    cnt.num += 1
###############################################################################

root = tk.Tk()
root.title("Join")
root.geometry("300x300")
#root.configure(background='')
#img  = Image.open("number images/blank_image.png")
print("starting state")
print(puz.blocks.reshape(3,3))
base_path = "number images/"
photo_val = 0
for i in range(N):
    y = i*50
    for j in range(N):
        #num_photo = np.where(puz.blocks == photo_val)[0][0]
        photo = puz.blocks[photo_val]
        path = base_path + str(photo) + ".png"
        
        im = Image.open(path) # PIL image
        tkimage = ImageTk.PhotoImage(im) # tk converted image from PIL image
        panel = tk.Label(root, image=tkimage) # handle and binding of tkimage to root
        panel.image = tkimage # set the panels image to tkimage

        x = j*50
        panel.place(x=x,y=y)
        photo_val += 1
cnt.num += 1

#Saved in the same relative location
#img.save("pasted_picture.png")

# here we are binding keyboard
# with the main window
root.bind('<Key>', lambda a : key_press(a))

root.wm_title("Sliding puzzle solver")
root.mainloop()
