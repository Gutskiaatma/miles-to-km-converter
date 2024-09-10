from tkinter import *


window =Tk()
window.title("Miles to km converter")
window.minsize(width=200, height=100)
window.config(padx=40, pady=40)


my_label = Label(text="Miles",  font=("Arial", 10))
my_label.grid(column=4, row=0)


my_label = Label(text="Km",  font=("Arial", 10))
my_label.grid(column=4, row=2)

my_label = Label(text="is equal to",  font=("Arial", 15))
my_label.grid(column=1, row=2)
Km_result = Label(text="0",  font=("Arial", 10))
Km_result.grid(column=3, row=2)

Miles_input = Entry(width=7)
Miles_input.grid(column=3, row=0)

def miles_to_km():
    miles = float(Miles_input.get())
    km = round(miles * 1.60934)
    Km_result.config(text=f"{km}")

button = Button(text="Convert", command=miles_to_km)
button.grid(column=3, row=4)




window.mainloop()