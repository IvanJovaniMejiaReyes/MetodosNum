import tkinter as tk
import math

def simpson_compuesta(a, b, n):
    h = (b - a) / n
    sumatoria = 0
    for i in range (n + 1):
        x = a + i *h
        fx = math.sin(x)
        if i == 0 or i == n:
            sumatoria += fx
        elif i % 2 == 0:
            sumatoria += 2 * fx
        else:
            sumatoria += 4 * fx
    return (h / 3) * sumatoria

def handle_simpson():
    a = float(entry_a.get())
    b = float(entry_b.get())
    n = int(entry_n.get())
    result_simpson = simpson_compuesta(a, b, n)
    result_label.config(text="Resultado del algoritmo de Simpson Compuesta" + str (result_simpson))

def main():
    global entry_a, entry_b, entry_n, result_label

    root = tk.Tk()
    root.title("Calculadora de Método de Simpson Compuesta")
    
    input_frame = tk.Frame(root)
    input_frame.pack()

    entry_a_label = tk.Label(input_frame, text="Limite Inferior (a):")
    entry_a_label.grid(row=0, column=0)
    entry_a = tk.Entry(input_frame)
    entry_a.grid(row=0, column=1)

    entry_b_label = tk.Label(input_frame, text="Limite Inferior (b):")
    entry_b_label.grid(row=1, column=0)
    entry_b = tk.Entry(input_frame)
    entry_b.grid(row=1, column=1)
    
    entry_n_label = tk.Label(input_frame, text="Número de Subintervalos (n):")
    entry_n_label.grid(row=2, column=0)
    entry_n = tk.Entry(input_frame)
    entry_n.grid(row=2, column=1)

    result_label = tk.Label(root, text="")
    result_label.pack()

    button_calculate = tk.Button(root, text="Calcular",command=handle_simpson)
    button_calculate.pack()

    root.mainloop()

if __name__ == "__main__":
    main()

