import tkinter as tk
from car_generator import CarGenerator
from intersection import Intersection

def initialize_window():
    root = tk.Tk()
    root.title("Symulator skrzyzowania")
    frame = tk.Frame(root, padx = 50, pady = 10)
    frame.pack()
    intersection = Intersection(frame)

    return root, frame, intersection

def main():
    root, _, intersection = initialize_window()
    global cg
    cg = CarGenerator(intersection.get_canvas())

    tk.Label(root, text="Intensity: ").pack()
    intensity_scale = tk.Scale(root, from_ = 1, to = 5, orient = "horizontal", command = cg.set_intencity)
    intensity_scale.set(3)
    intensity_scale.pack()
    tk.Label(root, text="Speed: ").pack()
    speed_scale = tk.Scale(root, from_ = 1, to = 5, orient = "horizontal", command = cg.set_speed)
    speed_scale.set(3)
    speed_scale.pack()


    button = tk.Button(root, text = "Enable/Disable", command = cg.enable)
    button.pack(pady = 10)
    cg.generate()

    root.mainloop()

if __name__ == "__main__":
    main()