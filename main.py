import tkinter as tk
from car import Car
from direction import Direction

def create_directions(canvas):
    left_to_right = Direction(10, 110, canvas.winfo_height() / 2 - 60, canvas.winfo_height() / 2 - 10, 5, 0)
    right_to_left = Direction(canvas.winfo_width() - 110, canvas.winfo_width() - 10, canvas.winfo_height() / 2 + 10, canvas.winfo_height() / 2 + 60, -5, 0)
    top_to_bottom = Direction(canvas.winfo_width()/2 - 60, canvas.winfo_width()/2 - 10, 10, 110, 0, 5)
    bottom_to_top = Direction(canvas.winfo_width()/2 + 10, canvas.winfo_width()/2 + 60, canvas.winfo_height() - 110, canvas.winfo_height() - 10, 0, -5)    
    return [left_to_right, right_to_left, top_to_bottom, bottom_to_top]


def initialize_window():
    root = tk.Tk()
    frame = tk.Frame(root, padx=50,pady=50)
    frame.pack()
    canvas = tk.Canvas(frame, width=800, height=600, bg="white")
    canvas.pack()
    canvas.update()
    return root, frame, canvas

def main():
    root, frame, canvas = initialize_window()

    directions = create_directions(canvas)

    car = Car(canvas, directions[0])
    car.start()

    car2 = Car(canvas, directions[1])
    car2.start()

    car3 = Car(canvas, directions[2])
    car3.start()
    
    car4 = Car(canvas, directions[3])
    car4.start()

    root.mainloop()

if __name__ == "__main__":
    main()