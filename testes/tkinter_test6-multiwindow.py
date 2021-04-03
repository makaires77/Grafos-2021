"""
https://www.geeksforgeeks.org/python-tkinter-toplevel-widget/?ref=rp
https://www.geeksforgeeks.org/combobox-widget-in-tkinter-python/?ref=lbp
https://stackoverflow.com/questions/16996432/how-do-i-bind-the-enter-key-to-a-function-in-tkinter
"""
from tkinter import *


# Create the window window
# with specified size and title
window = Tk()
window.title("window Window")
window.geometry("800x600")

# Create label for window window
label1 = Label(window, text = "This is the window window")
	
# define a function for 2nd toplevel window not associated with any parent window
def open_Toplevel2():
	
	# Create widget
	top2 = Toplevel()
	
	# define title for window
	top2.title("Toplevel2")
	
	# specify size
	top2.geometry("200x100")
	
	# Create label
	label = Label(top2,
				text = "This is a Toplevel2 window")
	
	# Create exit button.
	button = Button(top2, text = "Exit",
					command = top2.destroy)
	
	label.pack()
	button.pack()
	
	# Display untill closed manually.
	top2.mainloop()
	
# define a function for 1st toplevel which is associated with window window.
def open_Toplevel1():
	
	# Create widget
	top1 = Toplevel(window)
	
	# Define title for window
	top1.title("Toplevel1")
	
	# specify size
	top1.geometry("200x200")
	
	# Create label
	label = Label(top1,
				text = "This is a Toplevel1 window")
	
	# Create Exit button
	button1 = Button(top1, text = "Exit",
					command = top1.destroy)
	
	# create button to open toplevel2
	button2 = Button(top1, text = "open toplevel2",
					command = open_Toplevel2)
	
	label.pack()
	button2.pack()
	button1.pack()
	
	# Display untill closed manually
	top1.mainloop()

# Create button to open toplevel1
button = Button(window, text = "open toplevel1",
				command = open_Toplevel1)
label1.pack()

# position the button
button.place(x = 155, y = 50)
	
# Display untill closed manually
window.mainloop()
