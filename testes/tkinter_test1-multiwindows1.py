import tkinter as tk


class Win1:
    def __init__(self, master):
        self.master = master
        self.master.geometry("400x300")
        self.show_widgets()

    def show_widgets(self):
        self.frame = tk.Frame(self.master)
        self.master.title("Window n.1")
        self.create_button("Click to open Window 2", Win2)
        self.create_button("Click to open Window 3", Win3)
        self.frame.pack()

    def create_button(self, text, _class):
        "Button that creates a new window"
        tk.Button(
            self.frame, text=text,
            command=lambda: self.new_window(_class)).pack()

    def new_window(self, _class):
            global win2, win3

            try:
                if _class == Win2:
                    if win2.state() == "normal":
                        win2.focus()
            except:  
                win2 = tk.Toplevel(self.master)
                _class(win2)

            try:
                if _class == Win3:
                    if win3.state() == "normal":
                        win3.focus()
            except:  
                win3 = tk.Toplevel(self.master)
                _class(win3)

    def close_window(self):
        self.master.destroy()

class Win2(Win1):

    def show_widgets(self):
        "A frame with a button to quit the window"
        self.master.title("Window 2")
        self.frame = tk.Frame(self.master, bg="red")
        self.quit_button = tk.Button(
            self.frame, text=f"Quit this window n. 2",
            command=self.close_window)
        self.quit_button.pack()
        self.create_button("Open window 3 from window 2", Win3)
        self.frame.pack()



class Win3(Win2):

    def show_widgets(self):
        self.master.title("Window 3")
        self.frame = tk.Frame(self.master, bg="green")
        self.quit_button = tk.Button(
            self.frame, text=f"Quit this window n. 3",
            command=self.close_window)
        self.label = tk.Label(
            self.frame, text="THIS IS ONLY IN THE THIRD WINDOW")
        self.label.pack()
        self.frame.pack()



root = tk.Tk()
app = Win1(root)
root.mainloop()
