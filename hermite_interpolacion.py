import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def hermite_interpolacion(x, y, dy):
    n = len(x)
    def H(i, t):
        result = 1
        for j in range(n):
            if j !=i:
                result *=(t - x[j]) / (x[i] - x[j])
        return result
    def L(i, t):
        return sum(1 / (x[i] - x[j]) for j in range(n) if j !=i)
    def interpolant (t):
        result = 0
        for i in range (n):
            result += y [i] * (1 - 2 * L(i, t) * (t - x[i])) * H(i, t) ** 2
            result += dy[i] * (t - x[i]) * H(i, t) ** 2
        return result
    return interpolant

def plot_hermite_interpolacion(x, y, dy):
    interpolant = hermite_interpolacion(x, y, dy)
    x_values = np.linspace(min(x), max(x), 1000)
    y_values = [interpolant(t) for t in x_values]
    plt.scatter(x, y, color='red', label='Puntos de datos')
    plt.plot(x_values, y_values, label='Interpolación de Hermite')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Interpolación de Hermite')
    plt. legend()
    plt.grid(True)
    plt.show()

def add_point():
    points_x.append(float(entry_x.get()))
    points_y.append(float(entry_y.get()))
    points_dy.append(float(entry_dy.get()))
    update_points_list()

def update_points_list():
    text = "\n".join(f"({x}, {y}, {dy})" for x, y, dy in zip(points_x, points_y, points_dy))
    points_list.config(state=tk.NORMAL)
    points_list.delete('1.0', tk.END)
    points_list.insert(tk.END, text)
    points_list.config(state=tk.DISABLED)

def plot_interpolation():
    plot_hermite_interpolacion(points_x, points_y, points_dy)

window = tk.Tk()
window.title("Interpolación de Hermite")

points_x, points_y, points_dy = [],[],[]

label_x = tk.Label(window, text="x:")
label_x.grid(row=0, column=0)
entry_x = tk.Entry(window)
entry_x.grid(row=0, column=1)

label_y = tk.Label(window, text="y:")
label_y.grid(row=1, column=0)
entry_y = tk.Entry(window)
entry_y.grid(row=1, column=1)

label_dy = tk.Label(window, text="dy:")
label_dy.grid(row=2, column=0)
entry_dy = tk.Entry(window)
entry_dy.grid(row=2, column=1)

add_button = tk.Button(window, text="Agregar Punto", command=add_point)
add_button.grid(row=3, column=0, columnspan=2)

plot_button = tk.Button(window, text="Graficar Interpolación", command=plot_interpolation)
plot_button.grid(row=4, column=0, columnspan=2)

points_list = tk.Text(window, height=10, width=30)
points_list.grid(row=5, column=0, columnspan=2)
points_list.config(state=tk.DISABLED)

window.mainloop()