from tkinter import*
window=Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)
window.minsize(width=300, height=100)

my_label=Label(text="is equal to")
my_label.grid(column=0,row=1)

input=Entry(width=10)
input.grid(row=0,column=1)

def miles_to_km():
    km=float(input.get())*1.609
    km_label["text"]=km

km_label=Label(text="0")
km_label.grid(column=1,row=1)

button=Button(text="Calculate", command=miles_to_km)
button.grid(row=2,column=1)

miles_label=Label(text="Miles")
miles_label.grid(row=0,column=2)

kilo_label=Label(text="Km")
kilo_label.grid(row=1,column=2)

window.mainloop()