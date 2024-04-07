import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def euler_metodo(f, y0, t0, tn, h):

    t_values = [t0]
    y_values = [y0]
    t = t0
    y = y0
    while t < tn:
        y += h * f(t, y)
        t += h
        t_values.append(t)
        y_values.append(y)
    return t_values, y_values

def solve_euler():
    #obtenemos valores ingresados
    y0 = float(entry_y0.get())
    t0 = float(entry_t0.get())
    tn = float(entry_tn.get())
    h = float(entry_h.get())
    
    def f(t,y):
        return y
    
    #Resolvemos la EDO
    t_values, y_values = euler_metodo(f, y0, t0, tn, h)

    #Visualisamos resultados
    fig, ax = plt.subplots()
    ax.plot(t_values,y_values, label = 'Solución numérica Euler')
    ax.set_xlabel('t')
    ax.set_ylabel('y')
    ax.set_title('Solución de la EDO dy/dt = y con el método de Euler')
    ax.legend()
    ax.grid(True)

    #Crear lienzo de matplotlib
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

#Ventana principal
window = tk.Tk()
window.title("Método de Euler")

#Interfaz Grafica
label_y0 = tk.Label(window, text="Condición inicial de y (y0):")
label_y0.pack()
entry_y0 = tk.Entry(window)
entry_y0.pack()

label_t0 = tk.Label(window, text="Valor inicial de t (t0):")
label_t0.pack()
entry_t0 = tk.Entry(window)
entry_t0.pack()

label_tn = tk.Label(window, text="Valor final de t (tn):")
label_tn.pack()
entry_tn = tk.Entry(window)
entry_tn.pack()

label_h = tk.Label(window, text="tamañp del paso (h):")
label_h.pack()
entry_h = tk.Entry(window)
entry_h.pack()

solve_button = tk.Button(window, text="Resolver", command=solve_euler)
solve_button.pack()

#bucle de la ventana

window.mainloop()

