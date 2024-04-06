import tkinter as tk

def neville_interpolacion (x, y, target):
    n = len(x)
    Q = [[0] * n for _ in range(n)]

    for i in range(n):
            Q[i][0] = y [i]
    
    for i in range (1, n):
        for j in range (1, i + 1):
            Q[i][j] = ((target - x [i - j]) * Q [i][j - 1] - (target - x[i]) * Q[i - 1][j - 1]) / (x[i] - x[i - j])

    return Q [n - 1][n - 1]

def interpolate():
    x_values = [float (entry_x[i].get()) for i in range(len(entry_x))]
    y_values = [float (entry_y[i].get()) for i in range(len(entry_y))]
    target_value = float(entry_target.get())
    interpolate_value = neville_interpolacion(x_values, y_values, target_value)
    label_result.config(text=f"El valor interpolado en x = {target_value} es: {interpolate_value:.4f}")

def open_interpolation_window():
    window = tk.Toplevel(root)
    window.title("Interpolación Neville")

    label_points = tk.Label(window, text= "Número de puntos de datos:")
    label_points.pack()

    global entry_x, entry_y
    entry_x = []
    entry_y = []

    n = int(entry_points.get())
    for i in range(n):
        label_x = tk.Label(window, text=f"Valor de x{i}:")
        label_x.pack()
        entry_x.append(tk.Entry(window))
        entry_x[-1].pack()

        label_y = tk.Label(window, text=f"Valor de y{i}:")
        label_y.pack()
        entry_y.append(tk.Entry(window))
        entry_y[-1].pack()

    label_target = tk.Label(window, text="Ingrese el valor de x para la interpolación:")
    label_target.pack()
    global entry_target
    entry_target = tk.Entry(window)
    entry_target.pack()

    button_interpolate = tk.Button(window, text="Interpolar", command=interpolate)
    button_interpolate.pack()

    global label_result
    label_result = tk.Label(window, text="")
    label_result.pack()

root = tk.Tk()
root.title("Interpolación Neville")

label_points = tk.Label(root, text="Número de puntos de datos:")
label_points.pack()

entry_points = tk.Entry(root)
entry_points.pack()

button_open = tk.Button(root, text="Abrir ventana de interpolación", command=open_interpolation_window)
button_open.pack()

root.mainloop()