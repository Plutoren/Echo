import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from web_get import *
from UserPreferences import *
from recommend_algorithm import *


class Echo(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for f in (StartPage, PagePlanner, PageHotel, PageRestaurant, PageAttraction):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row = 0)
        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row = 0, column = 0, sticky = "nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def store_user_data(self, dates):
        self.data = dates

    def get_data(self):
        return self.data


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text = "Start Page")
        label.grid(row = 0, padx = 1)

        text1 = tk.Label(self, text = "start date").grid(row = 1, column = 0)
        text2 = tk.Label(self, text = "end date").grid(row = 4, column = 0)
        text3 = tk.Label(self, text = "Month").grid(row = 2, column = 1)
        text4 = tk.Label(self, text = "Day").grid(row = 2, column = 3)
        text5 = tk.Label(self, text = "Month").grid(row = 5, column = 1)
        text6 = tk.Label(self, text = "Day").grid(row = 5, column = 3)
        text7 = tk.Label(self, text="name: ").grid(row=6, column=0)

        box1_value = tk.StringVar()
        box1 = ttk.Combobox(self, textvariable = box1_value)
        box1["values"] = ("1","2","3","4","5","6","7","8","9","10","11","12")
        box1.current(0)
        box1.grid(row = 2, column = 2)

        box2_value = tk.StringVar()
        box2 = ttk.Combobox(self, textvariable = box2_value)
        box2["values"] = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30")
        box2.current(0)
        box2.grid(row = 2, column = 4)

        box3_value = tk.StringVar()
        box3 = ttk.Combobox(self, textvariable = box3_value)
        box3["values"] = ("1","2","3","4","5","6","7","8","9","10","11","12")
        box3.current(0)
        box3.grid(row = 5, column = 2)

        box4_value = tk.StringVar()
        box4 = ttk.Combobox(self, textvariable = box4_value)
        box4["values"] = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30")
        box4.current(0)
        box4.grid(row = 5, column = 4)


        entry1_value = tk.StringVar()
        entry1 = tk.Entry(self, textvariable=entry1_value).grid(row=6, column=1)

        data = [box1_value.get(), box2_value.get(), box3_value.get(), box4_value.get(), entry1_value.get()]
        controller.data = data

        button1 = tk.Button(self, text = "Submit", command = lambda: controller.show_frame(PagePlanner))
        button1.grid(row = 7, column = 0)

class PagePlanner(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        button1 = tk.Button(self, text = "Hotel", command = lambda: controller.show_frame(PageHotel)).grid(row = 1, column = 1)
        button2 = tk.Button(self, text = "Restaurant", command = lambda: controller.show_frame(PageRestaurant)).grid(row = 2, column = 1)
        button3 = tk.Button(self, text = "Attraction", command = lambda: controller.show_frame(PageAttraction)).grid(row = 3, column = 1)
        button4 = tk.Button(self, text = "Restart", command = lambda: controller.show_frame(StartPage)).grid(row = 4, column = 1)

        duration = 3
        for i in range(duration):
            label1 = tk.Label(self, text= "day {}".format(i)).grid(row = 5+i, column = 0)
            label = tk.Label(self, text="This is where the event is going to show up").grid(row= 5+i,column= 4)

class PageHotel(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        text = controller.get_data()
        label = tk.Label(self, text = "{}".format(text))
        label.pack(pady = 10, padx = 10)

        image = Image.open("cat.jpg")
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(self, image=photo)
        label.image = photo # keep a reference!
        label.pack()

        button1 = tk.Button(self, text = "Submit", command = lambda: controller.show_frame(PagePlanner))
        button1.pack()

class PageRestaurant(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        text = controller.get_data()
        label = tk.Label(self, text = "{}".format(text))
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Submit", command = lambda: controller.show_frame(PagePlanner))
        button1.pack()

class PageAttraction(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        text = controller.get_data()
        label = tk.Label(self, text = "{}".format(text))
        label.pack(pady = 10, padx = 10)

        button1 = tk.Button(self, text = "Submit", command = lambda: controller.show_frame(PagePlanner))
        button1.pack()

if __name__ == "__main__":
    app = Echo()
    app.mainloop()
