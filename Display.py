import tkinter as tk

class Display():

    def __init__(self,data):

        self.data = data
        self.root = tk.Tk()
        self.root.title('Données expérience')
        self.elements, self.elements1 = [], []
        self.l = tk.LabelFrame(self.root, text="Mesures en temps réel")
        self.l1 = tk.LabelFrame(self.root, text = "Données")

        def element(text) : return tk.Label(self.l, text=text)
        def element2(text) : return tk.Label(self.l1, text=text)
        self.elements1.append(element2(f"Masse = {self.data.masse} g"))
        self.elements1.append(element2(""))
        self.elements1.append(element2(f"Volume = {self.data.volume} mL"))
        self.elements.append(element("CO2"))
        self.elements.append(element(""))
        self.elements.append(element("time"))
        self.elements.append(element(""))
        self.elements.append(element("temperature"))
        self.elements.append(element(""))
        self.elements.append(element("humidity"))
        self.l.pack();self.l1.pack()
        self.display()

    def update(self, value, max, min):
        self.elements[0]['text'] = f"CO2 = {value[1]} ppm (min : {max[0]} | max : {min[0]})"
        self.elements[2]['text'] = f"time = {value[0]} secondes"
        self.elements[4]['text'] = f"température = {value[2]}°C (min : {max[1]} | max : {min[1]})"
        self.elements[6]['text'] = f"humidity = {value[3]} (min : {max[2]} | max : {min[2]})"
        self.display()

    def display(self):
        for e in self.elements : e.pack()
        for e in self.elements1 : e.pack()
        self.root.update()


