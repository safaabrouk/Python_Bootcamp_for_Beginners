# Python - Class based Tkinter UI

import tkinter as tk

class MyWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.label = tk.Label(self, text="Welcome To my First Window !")
        self.label.pack()

        self.entry = tk.Entry(self)
        self.entry.pack()

        self.button = tk.Button(self, text="Validate", command=self.show_input)
        self.button.pack()


        self.title("My App !")
        self.geometry("300x200")

    def show_input(self):
        text = self.entry.get()
        self.label.config(text=f"You typed : {text}")


app = MyWindow()
app.mainloop()