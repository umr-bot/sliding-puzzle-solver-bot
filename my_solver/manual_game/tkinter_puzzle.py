import tkinter
from tkinter import * 
#from tkinter.ttk import *
  
# creating tkinter window 
root = tkinter.Toplevel() 
  
# Adding widgets to the root window 
tkinter.Label(root, text = 'button1', font =( 
  'Verdana', 15)).pack(side = TOP, pady = 10) 
  
# Creating a photoimage object to use image 
photo = tkinter.PhotoImage(file = "number images/1.png") 
  
# here, image option is used to 
# set image on button 
tkinter.Button(root, text = 'Click Me !', image = photo).pack(side = TOP) 
  
mainloop() 
