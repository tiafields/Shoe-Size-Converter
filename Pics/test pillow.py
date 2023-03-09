import tkinter as tk

class ConversionApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.conversions = []
        self.create_widgets()

    def create_widgets(self):
        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.add_button = tk.Button(self.master, text="Add Conversion", command=self.add_conversion)
        self.add_button.pack()

        self.display_button = tk.Button(self.master, text="Display Conversions", command=self.display_conversions)
        self.display_button.pack()

    def add_conversion(self):
        conversion = self.entry.get()
        self.conversions.append(conversion)
        self.entry.delete(0, tk.END)

    def display_conversions(self):
        top = tk.Toplevel(self.master)
        tk.Label(top, text="Conversions:").pack()
        for conversion in self.conversions:
            tk.Label(top, text=conversion).pack()

root = tk.Tk()
app = ConversionApp(master=root)
app.mainloop()
