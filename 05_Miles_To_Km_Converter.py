from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=400, height=250)
window.config(padx=130, pady=50)


miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=20)

label_02 = Label(text="is equal to")
label_02.grid(column=0, row=1)

label_03 = Label(text="0")
label_03.grid(column=1, row=1)

label_04 = Label(text="KM")
label_04.grid(column=2, row=1)


def convert_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    label_03["text"] = km


button = Button(text="Calculate", command=convert_to_km)
button.grid(column=1, row=2)

window.mainloop()
