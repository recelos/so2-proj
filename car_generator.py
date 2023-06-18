import random
from direction import Direction
from car import Car
import threading

def create_directions(canvas):
    left_to_right = Direction("left_to_right", canvas.winfo_width() - 60, canvas.winfo_width() - 10, canvas.winfo_height() / 2 - 40, canvas.winfo_height() / 2 - 10, -2, 0, "Horizontal")
    right_to_left = Direction("right_to_left", 10, 60, canvas.winfo_height() / 2 + 10, canvas.winfo_height() / 2 + 40, 2, 0, "Horizontal")
    top_to_bottom = Direction("top_to_bottom" ,canvas.winfo_width()/2 - 40, canvas.winfo_width()/2 - 10, 10, 60, 0, 2, "Vertical")
    bottom_to_top = Direction("bottom_to_top" ,canvas.winfo_width()/2 + 10, canvas.winfo_width()/2 + 40, canvas.winfo_height() - 60, canvas.winfo_height() - 10, 0, -2, "Vertical")
    return [left_to_right, right_to_left, top_to_bottom, bottom_to_top]

class CarGenerator:
    def __init__(self, canvas):
        self.canvas = canvas
        self.cars = []
        self.directions = create_directions(self.canvas)
        self.is_running = True
        self.semaphore = threading.BoundedSemaphore(15) 

    def generate(self):
        direction = self.directions[random.randint(0, 3)]
        car = Car(self.canvas, direction, self.cars, self.semaphore)
        car.start()

        self.cars.append(car)
        if self.is_running is True:
                self.canvas.after(random.randint(250, 500), self.generate)


    def enable(self):
        if self.is_running is True:
            self.is_running = False
        else:
            self.is_running = True
            self.generate()