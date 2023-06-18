import random
import threading
from direction import Direction
from car import Car

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
        self.lower = 250
        self.higher = 500 
        self.car_speed = 0.01

    def generate(self):
        direction = self.directions[random.randint(0, 3)]
        car = Car(self.canvas, direction, self.cars, self.semaphore, self.car_speed)
        car.start()

        self.cars.append(car)
        if self.is_running is True:
            self.canvas.after(random.randint(self.lower, self.higher), self.generate)


    def enable(self):
        if self.is_running is True:
            self.is_running = False
        else:
            self.is_running = True
            self.generate()

    def set_intencity(self, value):
        if value == "5":
            self.lower = 200
            self.higher = 300
        if value == "4":
            self.lower = 250
            self.higher = 500
        if value == "3":
            self.lower = 300
            self.higher = 750
        if value == "2":
            self.lower = 500
            self.higher = 1000
        if value == "1":
            self.lower = 750
            self.higher = 1500

    def set_speed(self, value):
        if value == "5":
            self.car_speed = 0.005
        if value == "4":
            self.car_speed = 0.007
        if value == "3":
            self.car_speed = 0.01
        if value == "2":
            self.car_speed = 0.03
        if value == "1":
            self.car_speed = 0.05
