from tkinter import *

nerdfont = ('3270 Nerd Font Mono', 120)

window = Tk()
window.title("inputs.")

def submit():
	username = widget.get()
	print(username)

def delete():
	widget.delete(0, END)

def backspace():
	widget.delete(len(widget.get()) - 1, END)

widget = Entry()
submit = Button(window, text="submit", command=submit)
delete = Button(window, text="delete", command=delete)
backspace = Button(window, text="backspace", command=backspace)

widget.config(font=nerdfont)
widget.config(bg="#5acffa")
widget.config(fg="#ffffff")
widget.config(width=10)
#widget.config(show="#")
#widget.insert(0, "you trans")
#widget.config(state=DISABLED)

widget.pack()
submit.pack()
delete.pack()
backspace.pack()
window.mainloop()
