import tkinter as tk

# Dashboard Settings
LADO_CASILLA = 80
COLOR_CASILLA_CLARA = '#FFFFFF'
COLOR_CASILLA_OSCURA = '#808080'

# Create main window
ventana = tk.Tk()
ventana.title("Tablero de Ajedrez")

# Create canvas
lienzo = tk.Canvas(ventana, width=8 * LADO_CASILLA, height=8 * LADO_CASILLA)
lienzo.pack()
