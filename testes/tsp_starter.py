# Program to make a simple entry screen
from core import *
from solver import *
from uitk import *

import tkinter as tk
import time
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from math import factorial
from PIL import ImageTk, Image
from tkinter import filedialog


## Abre automaticamente interface gráfica ao carregar este módulo
class Application(tk.Frame):
    
    def __init__(self):
        self.window=tk.Tk()
        global ordem
        ordem = tk.IntVar(value=0)
        
        # setting the window size
        self.window.geometry("1200x800")

        tk.Frame.__init__(self, self.window)
        self.create_widgets()

    def create_widgets(self):
        self.window.wm_title('Grafos - Prof.Raimir - Equipe05 (Marcos Aires, Fernando Oliveira e Ricardo Carubbi)')
        self.grid()

        # Create label for the window
        self.label1 = tk.Label(self.window, text = "Caixeiro Viajante - TSP", font=('calibre',12, 'bold'))
        self.label2 = tk.Label(self.window, text ='Posição das Cidades', font = "50")
        
        
        # declaring string variable for storing entries
        ordem_var = tk.IntVar()
        name_var  = tk.StringVar()
        lon_var   = tk.IntVar()
        lat_var   = tk.IntVar()
        # passw_var = tk.StringVar()
        cities=[]

        
        # define a function for 2nd toplevel window not associated with any parent window
        def open_Toplevel2():
            
            num_cities = len(cities)
            num_possible_paths = int(calc_all_symmetric_paths(num_cities))

            coordinates_x_max = 800
            coordinates_y_max = 600

            # cities = random_cities(num_cities, coordinates_x_max, coordinates_y_max)
            # cities = defined_cities(num_cities)
            user_interface = GraphicalInterface(coordinates_x_max, coordinates_y_max, num_possible_paths)
            solve_state = SolveState()

            t0=time.time()

            def solve():
                return solve_random_step(cities, solve_state)
                # return solve_lexicographic_symmetric_step(cities, solve_state)


            def draw(is_best_path, progress):
                user_interface.draw(cities, is_best_path, progress)


            for progress in range(0, num_possible_paths):
                is_best_path = solve()
                draw(is_best_path, progress + 1)


            draw_end_state(user_interface.canvas, cities)
            t1=time.time()

            print("Todos caminhos verificados.")
            print(round(t1-t0,2)," segundos")

            # # Display untill closed manually.
            # top2.mainloop()
        


        # define a function for 1st toplevel which is associated with window "window".
        def open_Toplevel1():
            
            # Create widget
            top1 = tk.Toplevel(self.window)
            
            # Define title for window
            top1.title("Simulação para o Grafo gerado")
            
            # specify size
            top1.geometry("1200x800")
            
            # Create label
            label = tk.Label(top1, text = "TSP")
            
            # Create Exit button
            button1 = tk.Button(top1, text = "Fechar", command = top1.destroy)
            
            # create button to open toplevel2
            button2 = tk.Button(top1, text = "Ver dados do processamento", command = open_Toplevel2)
            

            # plot function is created for plotting the graph in tkinter window
            def plot():

                # criação da tela de figura que exibirá o gráfico
                fig = Figure(figsize = (10, 5), dpi = 100)

                # função a ser plotada
                p = [i for i in range(101)]
                q = [i*100 for i in range(101)]
                y = [i**2 for i in range(101)]
                z = [factorial(i) for i in range(9)]

                # adding the subplot
                plot1 = fig.add_subplot(111)
                # plot1 = fig.add_subplot(121)

                # comando para plotar o gráfico
                plot1.plot(p, label='constante', linewidth=2)
                plot1.plot(q, label='linear', linewidth=2)
                plot1.plot(y, label='polinomial', linewidth=2)
                plot1.plot(z, label='fatorial', linewidth=2) 

                # creating the Tkinter canvas containing the Matplotlib figure
                canvas = FigureCanvasTkAgg(fig, master = top1)
                canvas.draw()

                # placing the canvas on the Tkinter window
                canvas.get_tk_widget().grid(row=8,column=1)

                # creating the Matplotlib toolbar
                toolbar = NavigationToolbar2Tk(canvas, top1, pack_toolbar=False)
                toolbar.update()
                toolbar.grid(row=10,column=1)

                # placing the toolbar on the Tkinter window
                canvas.get_tk_widget().grid(row=9,column=1)


            # Posiciona o botão criado na janela principal
            plot_button = tk.Button(master = top1,
                            command = plot,
                            height = 2,
                            width = 10,
                            text = "Plotar")


            label.grid(row=0,column=0)
            button1.grid(row=1,column=0)
            button2.grid(row=1,column=1)


            # plota o gráfico do matplotlib
            plot_button.grid(row=2,column=0)
            



            # Display untill closed manually
            top1.mainloop()


        # defining a function that will get data and print them on the screen
        def submit():
            
            ## Variáveis a serem utilizadas
            idc   = ordem_var.get()
            name  = name_var.get()
            lon   = lon_var.get()
            lat   = lat_var.get()
            
            print(" Ordem Cidades: ", idc)
            print("Nome da Cidade: ", name)
            print("     Longitude: ", lon)
            print("      Latitude: ", lat)

            cities.append(City(name=name, pos=(int(lon), int(lat)), number=idc))
            num_cities = len(cities)

            print("Qte_Cities:", num_cities, "Cidades:", cities)

            # ordem_var.set("")
            name_var.set("")
            lon_var.set("")
            lat_var.set("")


        # Create button to open toplevel1
        button = tk.Button(self.window, text = "Abrir Grafo", command = open_Toplevel1)

        # position the button
        button.place(x = 155, y = 50)


        Checkbutton1 = tk.IntVar()
        Checkbutton2 = tk.IntVar()

        Button1 = tk.Checkbutton(self.window, text = "Aleatória",
                            variable = Checkbutton1,
                            onvalue = 1,
                            offvalue = 0,
                            height = 2,
                            width = 10)

        Button2 = tk.Checkbutton(self.window, text = "Definida",
                            variable = Checkbutton2,
                            onvalue = 1,
                            offvalue = 0,
                            height = 2,
                            width = 10)


        # function to be called when button-2 of mouse is pressed
        def pressed2(event):
            ## Variáveis a serem utilizadas
            print('Button-2 pressed at x = % d, y = % d'%(event.x, event.y))

        # function to be called when button-3 of mouse is pressed
        def pressed3(event):
            print('Button-3 pressed at x = % d, y = % d'%(event.x, event.y))

        ## function to be called when button-1 is double clocked
        def double_click(event):
            global ordem
            ordem.set(ordem.get()+1)
            
            if ordem.get() == 1:
                name = name_var.set("A")
            if ordem.get() == 2:
                name = name_var.set("B")
            if ordem.get() == 3:
                name = name_var.set("C")
            if ordem.get() == 4:
                name = name_var.set("D")
            if ordem.get() == 5:
                name = name_var.set("E")
            if ordem.get() == 6:
                name = name_var.set("F")
            if ordem.get() == 7:
                name = name_var.set("G")
            if ordem.get() == 8:
                name = name_var.set("H")
            
            idc   = ordem_var.set(ordem.get())
            lon   = lon_var.set(event.x)
            lat   = lat_var.set(event.y)
            print('Double clicked at x = % d, y = % d'%(event.x, event.y))
            

        frame1 = tk.Frame(self.window, height = 800, width = 600, bg="white", bd = 4)

        # these lines are binding mouse buttons with the Frame widget
        # window.bind('<Button-2>', pressed2)
        # window.bind('<Button-3>', pressed3)
        frame1.bind('<Double 1>', double_click)
        frame1.grid(row = 12, column = 1, columnspan=4)


        def openfilename():
            # open file dialog box to select image the dialogue box has a title "Open"
            filename = filedialog.askopenfilename(title ='Open')
            return filename

        def open_img():
            # Select the Imagename from a folder
            x = openfilename()

            # opens the image
            img = Image.open(x)
            
            # resize the image and apply a high-quality down sampling filter
            img = img.resize((800, 600), Image.ANTIALIAS)

            # PhotoImage class is used to add image to widgets, icons etc
            img = ImageTk.PhotoImage(img)

            # create a label
            panel = tk.Label(frame1, image = img)
            
            # set the image as img
            panel.image = img
            panel.bind('<Double 1>', double_click)
            panel.grid()

        # Create a button and place it into the window using grid layout
        btnOpenImage = tk.Button(self.window, text ='Abrir imagem', command = open_img)
        btnOpenImage.grid(row = 4, column = 4)


        
            

        # ordem_cities using widget Label
        title_label = tk.Label(self.window, text = 'Cidades:', font=('calibre',12, 'bold'))
            
        # creating a label for ordem_cities using widget Label
        ordem_label = tk.Label(self.window, text = 'Ordem', font=('calibre',10, 'bold'))

        # creating a entry for input city name using widget Entry
        ordem_entry = tk.Entry(self.window,textvariable = ordem_var, font=('calibre',10,'normal'))

        # creating a label for name using widget Label
        name_label = tk.Label(self.window, text = 'Cidade', font=('calibre',10, 'bold'))

        # creating a entry for input name using widget Entry
        name_entry = tk.Entry(self.window,textvariable = name_var, font=('calibre',10,'normal'))

        # creating a label for password
        lon_label = tk.Label(self.window, text = 'Longitude', font = ('calibre',10,'bold'))

        # entrando com as coordenadas
        lon_entry =tk.Entry(self.window, textvariable = lon_var, font = ('calibre',10,'normal'))

        # creating a label for password
        lat_label = tk.Label(self.window, text = 'Latitude', font = ('calibre',10,'bold'))

        # entrando com as coordenadas
        lat_entry =tk.Entry(self.window, textvariable = lat_var, font = ('calibre',10,'normal'))


        # creating a button using the widget Button that will call the submit function
        self.sub_btn=tk.Button(self.window,text = 'Salvar Dados', command = submit)
        self.window.bind("<Return>", (lambda event: submit()))

        # placing the position using grid method
        self.label1.grid(row=0,column=0)
        title_label.grid(row=3,column=0)

        self.label2.grid(row=1,column=1)
        Button1.grid(row=1,column=2)
        Button2.grid(row=1,column=3)

        ordem_label.grid(row=4,column=0)
        ordem_entry.grid(row=4,column=1)
        name_label.grid(row=4,column=2)
        name_entry.grid(row=4,column=3)
        lon_label.grid(row=5,column=0)
        lon_entry.grid(row=5,column=1)
        lat_label.grid(row=5,column=2)
        lat_entry.grid(row=5,column=3)
        self.sub_btn.grid(row=5,column=4)
        button.grid(row=6,column=0)


    def start(self):
        self.window.mainloop()


# performing an infinite loop for the window to display
Application().start()