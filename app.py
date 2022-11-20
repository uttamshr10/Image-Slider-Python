from itertools import cycle
import tkinter as tk


class App(tk.Tk):
    # Tk window/label adjusts to size of image
    def __init__(self, images, x, y, delay):

        tk.Tk.__init__(self)

        self.geometry('+{}+{}'.format(x, y))
        self.delay = delay

        self.pictures = cycle((tk.PhotoImage(file=image), image)
                              for image in images)
        self.picture_display = tk.Label(self)
        self.picture_display.pack()

    def show_slides(self):
        # cycle through the images and display them

        img_object, img_name = next(self.pictures)
        self.picture_display.config(image=img_object)
        self.title(img_name)
        self.after(self.delay, self.show_slides)

    def run(self):
        self.mainloop()


# set miliseconds time between slideshow
delay = 3500


# get a series of images you have in the working folder or use full path
images = [
    '1.jpg',
    '2.jpg',
    '3.jpg',
    '4.jpg',
    '5.jpg',
    '6.jpg',
    '7.jpg',
    '8.jpg',
    '9.jpg',
    '10.jpg'
]
x = 100
y = 50
app = App(images, x, y, delay)
app.show_slides()
app.run()
