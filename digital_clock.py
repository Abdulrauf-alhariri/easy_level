from tkinter import Tk, Label
import time

app = Tk()
app.title("My digital clock")
app.geometry("360x140")
app.resizable(0, 0)

label = Label(app, font=("Boulder", 60, "bold"),
              bg="Purple", fg="black", bd=30)
label.grid(row=0, column=1)


def digital_clock():
    time_live = time.strftime('%H: %M: %S')
    label.config(text=time_live)
    label.after(200, digital_clock)


label.pack(anchor='center')
digital_clock()
app.mainloop()
