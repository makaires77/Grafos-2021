# Program to make a simple entry screen
import tkinter as tk

root=tk.Tk()

# setting the windows size
root.geometry("800x600")

# declaring string variable
# for storing name and password
ordem_var = tk.StringVar()
name_var  = tk.StringVar()
lon_var   = tk.StringVar()
lat_var   = tk.StringVar()
# passw_var = tk.StringVar()
cities=[]

# defining a function that will
# get the name and password and
# print them on the screen
def submit():

    ordem = ordem_var.get()
    name  = name_var.get()
    lon   = lon_var.get()
    lat   = lat_var.get()
    # password  = passw_var.get()
    
	
    print(" Ordem Cidades: "+ ordem)
    print("Nome da Cidade: "+ name)
    print("     Longitude: "+ lon)
    print("      Latitude: "+ lat)
    # print("   Password: " + password)

    cities.append((ordem, name, (lon, lat)))
    print("Cidades:", cities)

    ordem_var.set("")
    name_var.set("")
    lon_var.set("")
    lat_var.set("")
    # passw_var.set("")
	
	
	
# creating a label for
# ordem_cities using widget Label
ordem_label = tk.Label(root, text = 'Ordem', font=('calibre',10, 'bold'))

# creating a entry for input
# name using widget Entry
ordem_entry = tk.Entry(root,textvariable = ordem_var, font=('calibre',10,'normal'))

# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'Cidade', font=('calibre',10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

# creating a label for password
lon_label = tk.Label(root, text = 'Longitude', font = ('calibre',10,'bold'))

# entrando com as coordenadas
lon_entry =tk.Entry(root, textvariable = lon_var, font = ('calibre',10,'normal'))

# creating a label for password
lat_label = tk.Label(root, text = 'Latitude', font = ('calibre',10,'bold'))

# entrando com as coordenadas
lat_entry =tk.Entry(root, textvariable = lat_var, font = ('calibre',10,'normal'))


# # creating a label for password
# passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))

# # creating a entry for password
# passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')

# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)

# placing the label and entry in the required position using grid method
ordem_label.grid(row=0,column=0)
ordem_entry.grid(row=0,column=1)
name_label.grid(row=1,column=0)
name_entry.grid(row=1,column=1)
lon_label.grid(row=1,column=2)
lon_entry.grid(row=1,column=3)
lat_label.grid(row=1,column=4)
lat_entry.grid(row=1,column=5)
sub_btn.grid(row=1,column=6)

# performing an infinite loop
# for the window to display
root.mainloop()
