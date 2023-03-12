#Program Name: Shoe Size Converter
#Author: Tia Fields
#Date Last Modified: 3.12.2023

#This program allows a user to type a shoe size (Male or Female, European or American)
# in the entry bars and press the "convert to" buttons and it will output the other
#countries show size. It will then store all the data you have typed into another window
#called "Your Conversions." You can close this external window and then clear your entries and start again.

import tkinter as tk

#defines class for shoe conversion
class shoeSizeConverterApp:
    #constructor method for initilizing class attributes
    def __init__(self, master):
        #assigns parameter to attribute
        self.master = master
        #gives title to app
        master.title("Shoe Size Converter")
        #sets gui window dimensions
        master.geometry("250x930")
        #assigns empty list
        self.entries = []

        #USA WOMAN TO EURO WOMAN SHOE CONVERSION SECTION
        #imports american flag image
        self.usaWomanImage = tk.PhotoImage(file="Pics/USA Flag 4.png")
        self.label = tk.Label(self.master, image=self.usaWomanImage, text = "American Flag")
        self.label.pack()
        self.label.configure(image=self.usaWomanImage, compound="top")

        #creates label
        self.usaWomenLabel = tk.Label(master, text = "Enter an American Female Shoe Size")
        self.usaWomenLabel.pack()

        #creates entry box
        self.usaWomanEntry = tk.Entry(master, width=30)
        self.usaWomanEntry.pack(padx=5,pady=5)

        #creates button for USA woman to EURO woman Shoe conversion
        self.usaWomanButton = tk.Button(master, text="Convert to Female European", command=self.usaWomanCallBack)
        self.usaWomanButton.pack()

        #creates listbox and sets dimensions
        self.usaWomanListBox = tk.Listbox(master, width=30, height=1)
        self.usaWomanListBox.pack(padx=5, pady=5)

        #button designed to clear entries in entry box
        self.usaWomanClearButton = tk.Button(master, text="Clear", command=self.usaWomanClearCallBack)
        self.usaWomanClearButton.pack(padx=10, pady=5)

        #EURO WOMAN TO USA WOMAN
        #imports european union flag image
        self.euroWomanImage = tk.PhotoImage(file="Pics/EU Flag 4.png")
        self.label = tk.Label(self.master, image=self.euroWomanImage, text = "European Union Flag")
        self.label.pack()
        self.label.configure(image=self.euroWomanImage, compound="top")

        #creates label
        self.euroWomenLabel = tk.Label(master, text="Enter an European Female Shoe Size")
        self.euroWomenLabel.pack()

        #creates entry box
        self.euroWomanEntry = tk.Entry(master, width=30)
        self.euroWomanEntry.pack(padx=5, pady=5)

        #creates button for EURO woman to USA woman Shoe conversion
        self.euroWomanButton = tk.Button(master, text="Convert to Female American", command=self.eruoWomanCallback)
        self.euroWomanButton.pack()

        #creates lsitbox and sets dimensions
        self.euroWomanListBox= tk.Listbox(master, width=30, height=1)
        self.euroWomanListBox.pack(padx=5, pady=5)

        #button designed to clear entries in the entry box
        self.euroWomanClearButton = tk.Button(master, text="Clear", command=self.euroWomanClearCallBack)
        self.euroWomanClearButton.pack(padx=5, pady=5)

        # USA MEN TO EURO MEN SHOE CONVERSION SECTION
        #imports american flag image
        self.usaMenImage = tk.PhotoImage(file="Pics/USA Flag 4.png")
        self.label = tk.Label(self.master, image=self.usaMenImage, text = "American Flag")
        self.label.pack()
        self.label.configure(image=self.usaMenImage, compound="top")

        #creates label
        self.usaMenLabel = tk.Label(master, text="Enter an American Male Shoe Size")
        self.usaMenLabel.pack()

        #creates entry box
        self.usaMenEntry = tk.Entry(master, width=30)
        self.usaMenEntry.pack(padx=5, pady=5)

        #creates button for USA men to EURO men Shoe conversion
        self.usaMenButton = tk.Button(master, text="Convert to Male European", command=self.usaMenCallBack)
        self.usaMenButton.pack()

        #creates listbox and sets dimensions
        self.usaMenListBox = tk.Listbox(master, width=30, height=1)
        self.usaMenListBox.pack(padx=5, pady=5)

        #button designed to clear entries in the entry box
        self.usaMenClearButton = tk.Button(master, text="Clear", command=self.usaMenClearCallBack)
        self.usaMenClearButton.pack(padx=5, pady=5)

        # EURO MEN TO USA MEN SHOE CONVERSION SECTION
        #imports american flag image
        self.euroMenImage = tk.PhotoImage(file="Pics/EU Flag 4.png")
        self.label = tk.Label(self.master, image=self.euroMenImage, text = "European Union Flag")
        self.label.pack()
        self.label.configure(image=self.euroMenImage, compound="top")

        #creates label
        self.euroMenLabel = tk.Label(master, text="Enter an European Male Shoe Size")
        self.euroMenLabel.pack()

        #creates entry box
        self.euroMenEntry = tk.Entry(master, width=30)
        self.euroMenEntry.pack(padx=5, pady=5)

        #creates button for EURO Men to USA Men Shoe Conversion
        self.euroMenButton = tk.Button(master, text="Convert to Male American", command=self.euroMenCallback)
        self.euroMenButton.pack()

        #creates listbox and sets dimensions
        self.euroMenListBox = tk.Listbox(master, width=30, height=1)
        self.euroMenListBox.pack(padx=5, pady=5)

        #button designed to clear entries in entry box
        self.euroMenClearButton = tk.Button(master, text="Clear", command=self.euroMenClearCallBack)
        self.euroMenClearButton.pack(padx=5, pady=5)

        #creates label
        self.showConversionsLabel = tk.Label(master, text = "Click Below for Your Conversions")
        self.showConversionsLabel.pack()

        #button that exports all conversions to second window
        self.euroMenSaveButton = tk.Button(master, text="Show All Conversions", command=self.showAllConversionsCallBack)
        self.euroMenSaveButton.pack(padx=5, pady=5)

    #USA WOMAN TO EURO WOMAN FUNCTIONS
    #defines function conversion for usa woman shoe size to euro woman shoe size
    def usaWomanAdd(self):
            usaWoman1 = int(self.usaWomanEntry.get())
            euroWoman1 = usaWoman1 + 30
            self.usaWomanListBox.insert(tk.END, "USA Woman " + str(usaWoman1) + " = EU Woman " + str(euroWoman1))
            self.entries.append("USA Woman " + str(usaWoman1) + " = EU Woman " + str(euroWoman1))
            self.usaWomanEntry.delete(0, tk.END)

    #creates a call back function
    def usaWomanCallBack(self):
        self.usaWomanAdd()
        print("USA Female converts EU Female Shoe Size Button was clicked.")

    #defines function to clear entries in entry box
    def usaWomanClearFunction(self):
        self.usaWomanListBox.delete(0, tk.END)
        self.entries = []

    #creates a callback function
    def usaWomanClearCallBack(self):
        self.usaWomanClearFunction()
        print("Your entries have been deleted.")

    # EURO WOMAN TO USA WOMAN FUNCTIONS
    #defines function conversion for euro women shoe size to usa woman shoe size
    def euroWomanAdd(self):
        euroWoman2 = int(self.euroWomanEntry.get())
        usaWoman2 = euroWoman2 - 30
        self.euroWomanListBox.insert(tk.END, "EU Woman " + str(euroWoman2) + " = USA Woman " + str(usaWoman2))
        self.entries.append("EU Woman " + str(euroWoman2) + " = USA Woman " + str(usaWoman2))
        self.euroWomanEntry.delete(0, tk.END)

    #creates a callback function
    def eruoWomanCallback(self):
        self.euroWomanAdd()
        print("EU Female converts USA Female Shoe Size Button was clicked.")

    #defines function to clear entries in entry box
    def euroWomanClearFunction(self):
        self.euroWomanListBox.delete(0, tk.END)
        self.entries = []

    #creates a callback function
    def euroWomanClearCallBack(self):
        self.euroWomanClearFunction()
        print("Your entries have been deleted.")

    #USA MEN TO EURO MEN FUNCTIONS
    #defines function conversion for usa men shoe size to euro men shoe size
    def usaMenAdd(self):
        usaMen1 = int(self.usaMenEntry.get())
        euroMen1 = usaMen1 + 33
        self.usaMenListBox.insert(tk.END, "USA Men " + str(usaMen1) + " = EU Men " + str(euroMen1))
        self.entries.append("USA Men " + str(usaMen1) + " = EU Men " + str(euroMen1))
        self.usaMenEntry.delete(0, tk.END)

    #creates a callback function
    def usaMenCallBack(self):
        self.usaMenAdd()
        print("USA Male converts EU Male Shoe Size Button was clicked.")

    #defines function to clear entries in entry box
    def usaMenClearFunction(self):
        self.usaMenListBox.delete(0, tk.END)
        self.entries = []
    #creates a callback function
    def usaMenClearCallBack(self):
        self.usaMenClearFunction()
        print("Your entries have been deleted.")

    # EURO MEN TO USA MEN FUNCTIONS
    #defines function conversion for euro men to usa men shoe size
    def euroMenAdd(self):
        euroMen2 = int(self.euroMenEntry.get())
        usaMen2 = euroMen2 - 33
        self.euroMenListBox.insert(tk.END, "EU Men " + str(euroMen2) + " = USA Men " + str(usaMen2))
        self.entries.append("EU Men " + str(euroMen2) + " = USA Men " + str(usaMen2))
        self.euroMenEntry.delete(0, tk.END)

    #creates a callback function
    def euroMenCallback(self):
        self.euroMenAdd()
        print("EU Male converts USA Male Shoe Size Button was clicked.")

    #defines function to clear entries in entry box
    def euroMenClearFunction(self):
        self.euroMenListBox.delete(0, tk.END)
        self.entries = []

    #crates a callback function
    def euroMenClearCallBack(self):
        self.euroMenClearFunction()
        print("Your entries have been deleted.")

    #defines function to display all conversions that have been made and places into a second window called "Your Conversions"
    def showAllConversions(self):
        window = tk.Toplevel(self.master)
        window.title("Your Conversions")
        text = tk.Text(window)
        text.pack()
        for euroMenEntry in self.entries:
            text.insert(tk.END, euroMenEntry + "\n")
        #creates a button called close, and destroys page for second window
        secondWindowCloseButton = tk.Button(window, text="Close", command=window.destroy)
        secondWindowCloseButton.pack(pady=10)

    #creates a callback function
    def showAllConversionsCallBack(self):
        self.showAllConversions()
        print("Show All Conversions Button was clicked.")

root = tk.Tk()
root.title("Accessible GUI")
app = shoeSizeConverterApp(root)
root.mainloop()
