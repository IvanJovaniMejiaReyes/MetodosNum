import tkinter as tk
import subprocess
from tkinter import messagebox

#abrir programa
def open_program(program_name):
    try:
        subprocess.Popen(["python", f"{program_name}.py"])
    except FileNotFoundError:
        messagebox.showerror("Error," f"Archivo del programa {program_name}.py no se encontró")

#Crear Ventana principal
window = tk.Tk()
window.title("Menú Integral")

# funcion para abrir cada programa

def open_simpson_compuesta_program():
    open_program("simpson_compuesta")

def open_neville_interpolacion_program():
    open_program("neville_interpolacion")

def open_euler_metodo_program():
    open_program("euler_metodo")

def open_hermite_interpolacion_program():
    open_program("hermite_interpolacion")

#botones para abrir los programas

button_simpson = tk.Button(window, text="Regla compuesta de Simpson", command=open_simpson_compuesta_program)
button_simpson.pack()

button_neville = tk.Button(window, text="Interpolación de Neville", command=open_neville_interpolacion_program)
button_neville.pack()

button_euler = tk.Button(window, text="Método de Euler", command=open_euler_metodo_program)
button_euler.pack()

button_hermite = tk.Button(window, text="Interpolación de Hermite", command=open_hermite_interpolacion_program)
button_hermite.pack()

window.mainloop()

