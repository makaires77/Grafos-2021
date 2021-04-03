import tkinter as tk
# import os
# from random import choice, randrange


class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.mem = {}

    def label(self, text, r, c):
        "Creates a label with a text and row and column as arguments"
        self.label = tk.Label(
            self.root,
            text=text)
        self.label.grid(row=r, column=c)
        return self.label

    def entry(self, r, c):
        "Creates an input entry for the user"
        self.v = tk.StringVar()
        self.e = tk.Entry(
            self.root,
            textvariable=self.v)
        self.e.grid(row=r, column=c, sticky="w")
        return self.e

    def textarea(self, r, c):
        "Creates an input entry for the user"
        # self.v = tk.StringVar()
        self.t = tk.Text(
            self.root, height=10)
        self.t.grid(row=r, column=c, columnspan=2)
        return self.t

    def memorize(self, key, data):
        self.mem[key] = data
        print(self.mem)

    def number_of_students(self):
        "Creates the input of number of students using methods label and entry"
        label = w.label("Number of students", 0, 0)
        entry = w.entry(0, 1)
        entry.focus()
        entry.bind(
            "<Return>", lambda x: w.memorize(label["text"], self.v.get()))

    def template(self):
        "Creates the template for the test"
        ta = w.textarea(1, 0)
        example = "Sapendo che i costi diretti corrispondono al {}% del prezzo, calcola il prezzo con costi diretti pari a {}€."
        ta.insert("0.0", example)
        ta.bind(
            "<Return>", lambda x: w.create_exercise("template", ta.get("0.0", tk.END)))

    def create_exercise(self, key, data):
        self.memorize(key, data)
        x = self.mem["template"].count("{}")
        if x > 0:
            self.mem["ndata"] = x
            print(self.mem)
            for n in range(x):
                self.entry(n + 2, 0)
        else:
            print("There are no {}, add some if you want random data.")


def main():
    "Show the widgets"
    w.number_of_students()
    w.template()


# ============ Launch the app
w = Window()
main()
w.root.mainloop()


def old_code():
    data = [d[x] for x in d]
    name = [x for x in d]
    data2 = zip(name, data)

    template = ": Sapendo che i costi diretti corrispondono al {}% del prezzo, calcola il prezzo con costi diretti pari a {}€."

    # valori assoluti (choice)
    costi_diretti_euro = [20, 30, 35, 40, 45]
    # percentuali (randrange)
    start, stop, step = 30, 150, 10

    tracce = ""
    sol = ""
    for alunno in d:
        a = choice(costi_diretti_euro)
        b = randrange(start, stop, step)
        template2 = template.format(a, b)
        tracce += alunno + template2 + "\n"
        sol += alunno + template2 + "SOL: {}\n".format(b/a*100)


    file_alunni = "tracce.txt"
    file_docente = "soluzione.txt"

    with open(file_alunni, "w") as file:
        file.write(tracce)
    with open(file_docente, "w") as file:
        file.write(sol)

    os.startfile("soluzione.txt")
    os.startfile("tracce.txt")