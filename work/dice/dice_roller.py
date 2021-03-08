import tkinter
from PIL import Image, ImageTk
import random

def window():
    # toplevel widget which represents the main window of an application
    root = tkinter.Tk()
    root.geometry('400x400')
    root.title('Layla Roll the Dice')

    # Adding label into the frame
    l0 = tkinter.Label(root, text="")
    l0.pack()

    # adding label with different font and formatting
    l1 = tkinter.Label(root, text="Hello from Layla Dice!", fg = "light green",
            bg = "dark green",
            font = "Helvetica 16 bold italic")
    l1.pack()

    # images
    dice = ['work/dice/die1.PNG', 'work/dice/die2.PNG', 'work/dice/die3.PNG', 'work/dice/die4.PNG', 'work/dice/die5.PNG', 'work/dice/die6.PNG']
    # simulating the dice with random numbers between 0 to 6 and generating image
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

    # construct a label widget for image
    label1 = tkinter.Label(root, image=image1)
    label1.image = image1

    # packing a widget in the parent widget 
    label1.pack( expand=True)

    # function activated by button
    def rolling_dice():
        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        # update image
        label1.configure(image=image1)
        # keep a reference
        label1.image = image1


    # adding button, and command will use rolling_dice function
    button = tkinter.Button(root, text='Roll the Dice', fg='blue', command=rolling_dice)

    # pack a widget in the parent widget
    button.pack( expand=True)
    
    # call the mainloop of Tk
    # keeps window open
    root.mainloop()