#Program Celsius to Fahrenheit
#Author: Tia Fields
#Last Date Modified: 2.22.2022


import tkinter as tk

class shoeSizeConverter:
    def __init__(self, master):
        self.master = master
        master.title("Shoe Size Converter")

        #Female American shoe size to female European shoe size
        self.usaWomanLabel = tk.Label(master, text= "Enter an American Female Shoe Size: ")
        self.usaWomanLabel.pack()

        self.usaWomanEntry = tk.Entry(master)
        self.usaWomanEntry.pack()

        self.usaWomanButton = tk.Button(master, text = "Convert to European", command = self.convertToFemaleEuro)
        self.usaWomanButton.pack()

        #Female European shoe size to female American shoe size
        self.euroWomanLabel = tk.Label(master, text="Enter a European Female Shoe Size: ")
        self.euroWomanLabel.pack()

        self.euroWomanEntry = tk.Entry(master)
        self.euroWomanEntry.pack()

        self.euroWomanButton = tk.Button(master, text="Convert to American", command = self.convertToFemaleAmerican)
        self.euroWomanButton.pack()

        # Male American shoe size to Male European shoe size
        self.usaMenLabel = tk.Label(master, text="Enter an American Male Shoe Size: ")
        self.usaMenLabel.pack()

        self.usaMenEntry = tk.Entry(master)
        self.usaMenEntry.pack()

        self.usaMenButton = tk.Button(master, text="Convert to European", command=self.convertToMaleEuro)
        self.usaMenButton.pack()

        # Male European shoe size to Male American shoe size
        self.euroManLabel = tk.Label(master, text="Enter a European Male Shoe Size: ")
        self.euroManLabel.pack()

        self.euroManEntry = tk.Entry(master)
        self.euroManEntry.pack()

        self.euroManButton = tk.Button(master, text="Convert to American", command=self.convertToMaleAmerican)
        self.euroManButton.pack()
        # Result display
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def convertToFemaleEuro(self):
        usaWoman = float(self.usaWomanEntry.get())
        euroWoman = usaWoman + 30
        self.result_label.config(text= f"{usaWoman} = {euroWoman}")

    def convertToFemaleAmerican(self):
        euroWoman = float(self.euroWomanEntry.get())
        usaWoman = euroWoman - 30
        self.result_label.config(text=f"{euroWoman} = {usaWoman}")

    def convertToMaleEuro(self):
        usaMan = float(self.usaMenEntry.get())
        euroMan = usaMan + 32.5
        self.result_label.config(text= f"{usaMan} = {euroMan}")

    def convertToMaleAmerican(self):
        euroMan = float(self.euroManEntry.get())
        usaMan = euroMan - 32.5
        self.result_label.config(text=f"{euroMan} = {usaMan}")

root = tk.Tk()
gui = shoeSizeConverter(root)
root.mainloop()