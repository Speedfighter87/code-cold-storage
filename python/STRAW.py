from tkinter import *

count = 0
def m1 ():
	global count

	count += 1
	print(f"you have {count} Berry's!!!")
	counter.config(text=count)

Unit = Tk()
#Unit.geometry("690x420")

mountain = PhotoImage(file="/home/speedfighter87/Desktop/images/mountain.png")

THEfont = font=('3270 Nerd Font Mono', 64, "bold")

berry = Button(Unit, text="collect")

berry.config(command=m1) #calls func
berry.config(font=THEfont)
berry.config(bg="#5acffa")
berry.config(fg="#f5abb9")
#berry.config(image=mountain)
berry.config(compound="bottom")
#berry.config(state=DISABLED)
berry.config(state=ACTIVE)

counter = Label(Unit, text=count)
counter.config(font=THEfont)

berry.pack()
counter.pack()

Unit.mainloop()
