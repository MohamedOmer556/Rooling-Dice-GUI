import tkinter
from PIL import Image, ImageTk
import random

# Main Window
root = tkinter.Tk()
root.geometry('400x400')
root.title('Rolling Dice by Moha')

# Designing the Buttons
# Adding label into the frame
blank_line = tkinter.Label(root, text='MoOoHA',
                           fg='light green',
                           bg='dark green',
                           font='Helvetica 10 bold italic')
blank_line.pack()

# adding label with different font and formatting
head_label = tkinter.Label(root, text='rolling dice',
                           fg='light blue',
                           bg='dark blue',
                           font='Helvetica 16 bold italic')
head_label.pack()


#  images To choose from
dice = ['die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']

dice_image = ImageTk.PhotoImage(Image.open(random.choice(dice)))

# construct a label widget for image
image_label = tkinter.Label(root, image=dice_image)
image_label.image = dice_image

image_label.pack(expand=True)


def rolling_dice():
    dice_image = ImageTk.PhotoImage(Image.open(random.choice(dice)))

    # update image
    image_label.configure(image=dice_image)
    # keep a reference
    image_label.image = dice_image


# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll it', command=rolling_dice)

button.pack(expand=True)




root.mainloop()
