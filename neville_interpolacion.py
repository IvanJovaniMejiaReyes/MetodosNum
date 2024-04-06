import tkinter as tk
import subprocess

#Función que ejecuta mi programa de pyton

def open_program(open_program):
    try:
        subprocess.Popen(["pyton", f"{program_name}.py"])
    except FileExistsError:
        messagebox.showerror("Error," f"El archivo del programa {program_name}.py no se encontro.")

#Se crea la Ventana principal
