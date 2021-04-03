from tkinter import *
from core import *

city_radius  = 15
current_path = []
best_path    = []
text_items   = []


class GraphicalInterface:
    def __init__(self, width, height, num_all_possible_paths):
        self.master = create_context()
        self.canvas = create_canvas(self.master, width, height)
        self.num_all_possible_paths = num_all_possible_paths

    def draw(self, cities, is_best_path, progress):
        draw_cities(self.canvas, cities)
        draw_current_path(self.canvas, cities)
        if is_best_path:
            draw_best_path(self.canvas, cities)
        write_screen(self.canvas, self.num_all_possible_paths, progress)
        self.master.update_idletasks()
        self.master.update()

    def freeze(self):
        self.master.mainloop()


def create_context():
    master = Tk()
    master.wm_title('Simulação Caixeiro Viajante - TSP')
    return master


def create_canvas(master, width, height):
    canvas = Canvas(master, width=width, height=height)
    canvas.configure(background="black")
    canvas.pack()
    return canvas


def write_screen(canvas, num_all_possible_paths, progress):
    clear_text_items(canvas)
    percent_calculated = progress / num_all_possible_paths * 100
    text = "Caminhos Possíves: Fatorial(n-1)/2="+ str(num_all_possible_paths) + "\nCalculado:" + str(progress) + round_digits(percent_calculated) + " %"
    text_items.append(canvas.create_text(150, 30, fill="white", font="Mono 12", text=text))


def round_digits(number):
    return "{:10.2f}".format(number)


def clear_text_items(canvas):
    for text in text_items:
        canvas.delete(text)


def draw_end_state(canvas, cities):
    clear_path(canvas, current_path)


def clear_path(canvas, stored_lines):
    for line in stored_lines:
        canvas.delete(line)


def draw_cities(canvas, cities):
    for city in cities:
        start = (city.pos[0] - city_radius, city.pos[1] - city_radius)
        end   = (city.pos[0] + city_radius, city.pos[1] + city_radius)
        canvas.create_oval(start[0], start[1], end[0], end[1], fill="white")
        # canvas.create_text(city.pos[0], city.pos[1]) #não havia no original
        
def draw_current_path(canvas, cities):
    clear_path(canvas, current_path)
    draw_path(canvas, cities, "white", current_path)


def draw_best_path(canvas, cities):
    clear_path(canvas, best_path)
    draw_path(canvas, cities, "red", best_path)


def draw_path(canvas, cities, color, stored_lines):
    for i in range(0, len(cities) - 1):
        stored_lines.append(draw_line(canvas, cities, (i, i + 1), color))
    stored_lines.append(draw_line(canvas, cities, (len(cities) - 1, 0), color))  # Draws the last path to the first city


def draw_line(canvas, cities, index_tuple, color):
    start = cities[index_tuple[0]].pos
    end = cities[index_tuple[1]].pos
    return canvas.create_line(start[0], start[1], end[0], end[1], fill=color)