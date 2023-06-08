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

# Draw the board
for fila in range(8):
    for columna in range(8):
        x1 = columna * LADO_CASILLA
        y1 = fila * LADO_CASILLA
        x2 = x1 + LADO_CASILLA
        y2 = y1 + LADO_CASILLA
        color = COLOR_CASILLA_CLARA if (fila + columna) % 2 == 0 else COLOR_CASILLA_OSCURA
        lienzo.create_rectangle(x1, y1, x2, y2, fill=color)

# Draw the tiles
fichas = {
    'r': '♜',
    'n': '♞',
    'b': '♝',
    'q': '♛',
    'k': '♚',
    'p': '♟',
    'R': '♖',
    'N': '♘',
    'B': '♗',
    'Q': '♕',
    'K': '♔',
    'P': '♙'
}

posiciones_iniciales = {
    'r': [(0, 0), (0, 7)],
    'n': [(0, 1), (0, 6)],
    'b': [(0, 2), (0, 5)],
    'q': [(0, 3)],
    'k': [(0, 4)],
    'p': [(1, i) for i in range(8)],
    'R': [(7, 0), (7, 7)],
    'N': [(7, 1), (7, 6)],
    'B': [(7, 2), (7, 5)],
    'Q': [(7, 3)],
    'K': [(7, 4)],
    'P': [(6, i) for i in range(8)]
}
