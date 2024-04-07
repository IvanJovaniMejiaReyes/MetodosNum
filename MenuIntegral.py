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
    open_program("Simpson Compuesta")