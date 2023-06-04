import tkinter as tk
from car_generator import CarGenerator
from intersection import Intersection

def initialize_window():
    root = tk.Tk()
    frame = tk.Frame(root, padx = 50, pady = 10)
    frame.pack()

    intersection = Intersection(frame)

    return root, frame, intersection

def main():
    root, frame, intersection = initialize_window()

    cg = CarGenerator(intersection.get_canvas())
    button = tk.Button(root, text = "Enable/Disable", command = cg.enable)
    button.pack(pady = 10)
    cg.generate()

    root.mainloop()

if __name__ == "__main__":
    main()