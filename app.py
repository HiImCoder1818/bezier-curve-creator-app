import tkinter as tk
from PIL import Image,ImageTk
from tkinter.filedialog import askdirectory

import os

class App:
    def __init__(self, width, height, buffer=70):
        self.width = width
        self.height = height
        self.buffer = buffer

        self.root = tk.Tk()
        self.root.geometry(f"{width+buffer+250}x{height+buffer}")
        self.root.resizable(False, False)
        self.root.title("Path Creator")

        self.canvas = tk.Canvas(self.root, width=width+buffer, height=height+buffer)
        self.canvas.pack()
        self.field = ImageTk.PhotoImage(Image.open("field.png"))
        self.canvas.create_image(width/2, height/2, anchor=tk.CENTER, image=self.field)

        
    def create_lines(self):
        for i in range(6):
            self.canvas.create_line((106+(2/3))*i, self.height+self.buffer/2, (106+(2/3))*(i+1), self.height+self.buffer/2, fill="blue", width=5)
            self.canvas.create_line((106+(2/3))*i, self.height, (106+(2/3))*i, self.height+self.buffer, fill="black", width=5)
            self.canvas.create_text((((106+(2/3))*i) + ((106+(2/3))*(i+1)))/2, self.height+self.buffer/2+20, text="106.66px", font=('Helvetica 15 bold'))

        self.canvas.create_line(5, self.height, 5, self.height+self.buffer, fill="black", width=5)
        self.canvas.create_line(640, self.height, 640, self.height+self.buffer, fill="black", width=5)

    def pixel_inch_lines(self):
        for i in range(144):
            self.canvas.create_line(self.width+self.buffer/2-20, (4+(4/9))*i, self.width+self.buffer-self.buffer/2+20, (4+(4/9))*i, fill="black", width=1)
            self.canvas.create_line(self.width+self.buffer/2, (4+(4/9))*i, self.width+self.buffer/2, (4+(4/9))*(i+1), fill="green", width=5)

    def draw_metric_text(self):
        self.green_label = tk.Label(self.root, text="-", font=('Helvetica 100 bold'), fg="green")
        self.green_label.place(x=885, y=120, anchor=tk.CENTER)
        self.green = tk.Label(self.root, text="4.44px", font=('Helvetica 15 bold'))
        self.green.place(x=885, y=150, anchor=tk.CENTER)

        self.blue_label = tk.Label(self.root, text="-", font=('Helvetica 100 bold'), fg="blue")
        self.blue_label.place(x=885, y=220, anchor=tk.CENTER)
        self.blue = tk.Label(self.root, text="106.66px", font=('Helvetica 15 bold'))
        self.blue.place(x=885, y=250, anchor=tk.CENTER)

        self.conv_label = tk.Label(self.root, text="scale", font=('Helvetica 25 bold'))
        self.conv_label.place(x=885, y=320, anchor=tk.CENTER)
        self.conv = tk.Label(self.root, text="4.44px = 1in", font=('Helvetica 15 bold'))
        self.conv.place(x=885, y=350, anchor=tk.CENTER)

    def draw_buttons(self):
        self.export = tk.Button(self.root, text="Export Control \nPoints", font=('Helvetica 12 bold'), command=self.browsefunc)
        self.export.place(x=60, y=200, anchor=tk.CENTER)

        self.add_bz = tk.Button(self.root, text="Add Bezier \nCurve", font=('Helvetica 12 bold'))
        self.add_bz.place(x=60, y=400, anchor=tk.CENTER)

    def browsefunc(self):
        directory = askdirectory()
        os.chdir(directory)

        with open("control_points.txt", "+w") as f:
            f.write("[(0, 0), (0, 0), (0, 0)]")

    def start(self):
        self.root.mainloop()

app = App(640, 640)
app.create_lines()
app.pixel_inch_lines()
app.draw_metric_text()
app.draw_buttons()
app.start()