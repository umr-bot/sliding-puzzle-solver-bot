from PIL import Image
import numpy as np

def draw_puzzle(arr):
    #Image on which we want to paste
    img = Image.open("number images/blank_image.png")

    #arr = np.arange(1,17)
    np.random.shuffle(arr)
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
