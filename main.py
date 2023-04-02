import tkinter as tk
from car_generator import CarGenerator

def initialize_window():
    root = tk.Tk()
    frame = tk.Frame(root, padx = 50, pady = 50)
    frame.pack()
    canvas = tk.Canvas(frame, width=800, height = 600, bg = "white")
    canvas.pack()
    canvas.update()
    return root, frame, canvas

def main():
    root, frame, canvas = initialize_window()

    CarGenerator(canvas)
    root.mainloop()

if __name__ == "__main__":
    main()