import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np
import matplotlib.image as mpimg
def save_fig(state,state_num, file_to_read='number images/'):
    im = []
    for block in state:
        image = mpimg.imread(file_to_read+str(block)+'.png')
        im.append(image)
#    im1 = mpimg.imread("number images/1.png")
#    im2 = mpimg.imread("number images/2.png") 
#    im3 = mpimg.imread("number images/3.png")
#    im4 = mpimg.imread("number images/4.png")
#    im5 = mpimg.imread("number images/5.png")
#    im6 = mpimg.imread("number images/6.png") 
#    im7 = mpimg.imread("number images/7.png")
#    im8 = mpimg.imread("number images/8.png")
#    im9 = mpimg.imread("number images/9.png")

    fig = plt.figure(figsize=(2., 2.))
    grid = ImageGrid(fig, 111,  # similar to subplot(111)
                     nrows_ncols=(3, 3),  # creates 3x3 grid of axes
                     axes_pad=0.01,  # pad between axes in inch.
                     )

    for ax, im in zip(grid, im):
        # Iterating over the grid returns the Axes.
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])
        ax.imshow(im)
    fig.savefig('puzzle/'+str(state_num), bbox_inches='tight')
    #plt.show()
