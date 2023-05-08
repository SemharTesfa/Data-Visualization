import tkinter as tk
from tkinter import messagebox
from Backend import BackEnd

class FrontEnd:
    def __init__(self, win, data):
        self.data = data
        self.bkend = BackEnd(data)
        button = tk.Button(win, text='XY Plot', width=25, command=self.draw_xy_plot)
        button1 = tk.Button(win, text='Bar Chart', width=25,command=self.draw_bar_chart)
        button2 = tk.Button(win, text='Linear Regression', width=25, command=self.draw_linear_regression)
        button.pack()
        button1.pack()
        button2.pack()

    def draw_xy_plot(self):
        self.bkend.draw_graph("xy_plot")

    def draw_bar_chart(self):
        self.bkend.draw_graph("bar_chart")

    def draw_linear_regression(self):
        self.bkend.draw_graph("linear_regression")


window = tk.Tk()
mywin=FrontEnd(window, "Temperature.html")
window.title('Data Visualization')
window.geometry('500x300')
window.mainloop()

