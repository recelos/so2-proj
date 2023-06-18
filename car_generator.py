import random
import os
from direction import Direction
from car import Car

def create_directions(canvas):
    left_to_right = Direction(canvas.winfo_width() - 60, canvas.winfo_width() - 10, canvas.winfo_height() / 2 - 40, canvas.winfo_height() / 2 - 10, random.randint(-4, -1), 0, "Horizontal")
    right_to_left = Direction(10, 60, canvas.winfo_height() / 2 + 10, canvas.winfo_height() / 2 + 40, random.randint(1, 4), 0, "Horizontal")
    top_to_bottom = Direction(canvas.winfo_width()/2 - 40, canvas.winfo_width()/2 - 10, 10, 60, 0, random.randint(1, 4), "Vertical")
    bottom_to_top = Direction(canvas.winfo_width()/2 + 10, canvas.winfo_width()/2 + 40, canvas.winfo_height() - 60, canvas.winfo_height() - 10, 0, random.randint(-4, 1), "Vertical")
    return [left_to_right, right_to_left, top_to_bottom, bottom_to_top]

class CarGenerator:
    def __init__(self, canvas):
        self.canvas = canvas
        self.cars = []
        self.directions = create_directions(self.canvas)
        self.is_running = True

    def generate(self):
        direction = self.directions[random.randint(0, 3)]
        car = Car(self.canvas, direction, self.cars)
        car.start()

        self.cars.append(car)
        os.system("cls")
        print(f"Number of cars on the intersection: { len([car for car in self.cars if car.is_running]) }")
        if self.is_running is True:
            self.canvas.after(random.randint(500, 1500), self.generate)


    def enable(self):
        if self.is_running is True:
            self.is_running = False
        else:
            self.is_running = True
            self.generate()