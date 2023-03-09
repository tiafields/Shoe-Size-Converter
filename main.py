#program shoe converter

import os;
import tkinter as tk
print("TESTING")
#from tkinter import ttk
class shoeSizeConverter(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.title("American/European Shoe Converter")
        self.geometry("500x1000")
        #self.configure(bg = "white")

        print(os.getcwd())

        #Impletmenting American Flag Photo
        self.photo = tk.PhotoImage(file="Pics/US Flag Resized 2.png")
        #THIS DOES NOT WORK DELETE THIS LATER THE COMMENTED CODE
        #self.photo.alt = "Alternative text for US Flag Resized 2.png"
        label = tk.Label(self, image = self.photo, width=200, height=100)
        # THIS DOES NOT WORK DELETE THIS LATER THE COMMENTED CODE
        #label.image = self.photo
        label.pack()

        #Female American shoe size to female European shoe size
        self.usaWomanLabel = tk.Label(self, text = "Enter an American Female Shoe Size: ")
        self.usaWomanLabel.pack()

        self.usaWomanEntry = tk.Entry(self)
        self.usaWomanEntry.pack()

        self.usaWomanButton = tk.Button(self, text = "Convert to European", command = self.convertToFemaleEuro)
        self.usaWomanButton.pack()

        # Impletmenting European Flag Photo
        self.photo2 = tk.PhotoImage(file="Pics/EU Flag Resized 3.png")
        label = tk.Label(self, image=self.photo2, width=200, height=100)
        label.pack()

        #Female European shoe size to female american shoe size
        self.euroWomanLabel = tk.Label(self, text = "Enter a European Female Shoe Size: ")
        self.euroWomanLabel.pack()

        self.euroWomanEntry = tk.Entry(self)
        self.euroWomanEntry.pack()

        self.euroWomanButton = tk.Button(self, text = "Convert to American", command = self.convertToFemaleAmerican)
        self.euroWomanButton.pack()

        # Impletmenting American Flag Photo
        self.photo3 = tk.PhotoImage(file="Pics/US Flag Resized 2.png")
        label = tk.Label(self, image=self.photo3, width=200, height=100)
        label.pack()


        # Male American shoe size to Male European Shoe Size
        self.usaMenLabel = tk.Label(self, text = "Enter an American Male Shoe Size: ")
        self.usaMenLabel.pack()

        self.usaMenEntry = tk.Entry(self)
        self.usaMenEntry.pack()

        self.usaMenButton = tk.Button(self, text = "Convert to European", command=self.convertToMaleEuro)
        self.usaMenButton.pack()

        # Impletmenting European Flag Photo
        self.photo4 = tk.PhotoImage(file="Pics/EU Flag Resized 3.png")
        label = tk.Label(self, image=self.photo4, width=200, height=100)
        label.pack()

        #Male European shoe size to Male American shoe size

        self.euroManLabel = tk.Label(self, text="Enter a European Male Shoe Size: ")
        self.euroManLabel.pack()

        self.euroManEntry = tk.Entry(self)
        self.euroManEntry.pack()

        self.euroManButton = tk.Button(self, text="Convert to American", command=self.convertToMaleAmerican)
        self.euroManButton.pack()

        #All Conversions

        self.listedConversionsLabel = tk.Label(self, text ="Click Below For Your Conversions")
        self.listedConversionsLabel.pack(pady=10)

        self.button = tk.Button(self, text="View Conversions", command=self.open_second_window)
        self.button.pack()



    def convertToFemaleEuro (self):
        usaWoman = float(self.usaWomanEntry.get())
        euroWoman = usaWoman +30
        self.result_label.config(text=f"{usaWoman} = {euroWoman}")

    def convertToFemaleAmerican(self):
        euroWoman = float(self.euroWomanEntry.get())
        usaWoman = euroWoman - 30
        self.result_label.config(text=f"{euroWoman} = {usaWoman}")

    def convertToMaleEuro(self):
        usaMan = float(self.usaMenEntry.get())
        euroMan = usaMan + 32.5
        self.result_label.config(text=f"{usaMan} = {euroMan}")

    def convertToMaleAmerican(self):
        euroMan = float(self.euroManEntry.get())
        usaMan = euroMan - 32.5
        self.result_label.config(text=f"{euroMan} = {usaMan}")

    def open_second_window(self):
        SecondWindow(self)
        #second_window = tk.Toplevel(self)
        #second_window.title("Second Window")

        #second_window_label = tk.Label(second_window, text="Hello from the second window!")
        #second_window_label.pack(padx=10, pady=10)

class SecondWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Your Conversions")
        self.geometry("500x500")

        yourConversionsLabel= tk.Label(self, text="Listed below is all the data you converted.")
        yourConversionsLabel.pack()

        btn_close = tk.Button(self, text="Close", command=self.destroy)
        btn_close.pack()

gui = shoeSizeConverter()
gui.mainloop()

