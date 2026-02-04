from tkinter import *

window = Tk()

x = IntVar()

def display():
	if x.get() == 1:
		print("I like python")
		return
	print("...")

check = Checkbutton(window) #text="" variable=x, onvalue=1, offvalue=0, command=display)

check.config(text="Python")
check.config(variable=x)
check.config(onvalue=1)
check.config(offvalue=0)
check.config(command=display)
check.config(font=('IBM 3270 Semi-Condensed', 50))
check.config(bg="#5acffa")
check.config(fg="#f5abb9")

check.pack()
window.mainloop()
