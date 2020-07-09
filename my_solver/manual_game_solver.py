 ### Basic NxN sliding puzzle solver 
from puzzle_generator import puzzle as puzzle
import numpy as np 
from pynput.keyboard import Key, Listener
from threading import Thread
from PIL import Image

puz = puzzle()

def draw_puzzle(arr):
    #Image on which we want to paste
    img = Image.open("number images/blank_image.png")

    #arr = np.arange(1,17)
    #np.random.shuffle(arr)
    base_path = "number images/"
    photo_val = 1
    for i in range(4):
        for j in range(4):
            num_photo = np.where(arr == photo_val)[0][0]
            path = base_path + str(num_photo+1) + ".png"
            im = Image.open(path)
            x = (j%4)*50
            y = (i%4)*50
            img.paste(im, (x,y))
            photo_val += 1

    #Saved in the same relative location
    #img.save("pasted_picture.png")

    img.show()

def on_press(key):
    print('{0} pressed'.format(key))
    if(str(key) == 'Key.up'): puz.transpose('up')
    if(str(key) == 'Key.down'): puz.transpose('down')
    if(str(key) == 'Key.right'): puz.transpose('right')
    if(str(key) == 'Key.left'): puz.transpose('left')
    draw_puzzle(puz.blocks)
def on_release(key):
    print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False
#def listen():
# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

#Thread(target = listen).start()
#Thread(target = draw(puz.blocks)).start()
