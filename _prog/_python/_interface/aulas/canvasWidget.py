import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window, bg='#ffffff', width=300, height=300)
canvas.pack()

canvas.create_oval((0, 0, 300, 300), fill='#ffff00')

canvas.create_arc((50, 100, 100, 150), extent=180, fill='#000000')
canvas.create_arc((200, 100, 250, 150), extent=180, fill='#000000')

canvas.create_line((50, 200, 110, 240), width=5, fill='#ff0000')
canvas.create_line((110, 240, 190, 240), width=5, fill='#ff0000')
canvas.create_line((190, 240, 250, 200), width=5, fill='#ff0000')

window.mainloop()