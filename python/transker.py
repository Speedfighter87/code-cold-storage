from tkinter import *

window = Tk() #prep an wind

window.geometry("690x420") #specs the size
window.title("winker") #names the window



V1 = PhotoImage(file="/home/speedfighter87/Desktop/images/v1.png")
suggestion = PhotoImage(file="/home/speedfighter87/Desktop/images/notme.png")
threeseventwenty = font=('3270 Nerd Font Mono', 40, "bold")

noun = Label(
	window, text="Wink ;-)", 
	font=threeseventwenty, 
	fg="#ffffff", 
	bg="#f5abb9",
	relief=RAISED,
	bd=10,
	padx=20,
	pady=15,
	image=suggestion,
	compound="bottom"
	)


noun.pack()
#noun.place(x="100", y="100")

window.iconphoto(True, V1) #sets icon
window.config(background="#5acffa")

window.mainloop() #disp an wind
		  #also "listen"
