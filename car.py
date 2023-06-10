import time
import threading
import random
import os

class Car:
    def __init__(self, canvas, direction, cars):
        self.canvas = canvas
        self.direction = direction
        self.cars = cars

        random_color = get_random_color()

        self.car = canvas.create_rectangle(direction.x1, direction.y1, direction.x2, direction.y2, fill=random_color)

        self.move_thread = None
        self.x_speed = direction.x_speed
        self.y_speed = direction.y_speed
        self.is_running = True
        self.is_on_intersection = False

    def start(self):
        self.move_thread = threading.Thread(target=self.move)
        self.move_thread.start()

    def move(self):
        try:
            while self.is_running:
                x1, y1, x2, y2 = self.canvas.coords(self.car)

                if self.is_off_map(x1, x2, y1, y2):
                    break
                
                if self.any_car_on_intersection():
                    if self.is_on_intersection:
                        self.canvas.move(self.car, self.x_speed, self.y_speed)
                        if not self.check_if_on_intersection(x1, x2, y1, y2):
                            self.is_on_intersection = False
                    else:
                        cars_on_intersection = [car for car in self.cars if car.is_on_intersection]
                        if not any(car for car in cars_on_intersection if car.direction.orientation != self.direction.orientation):
                            self.canvas.move(self.car, self.x_speed, self.y_speed)
                        
                elif self.check_if_on_intersection(x1, x2, y1, y2):
                    self.is_on_intersection = True
                    self.canvas.move(self.car, self.x_speed, self.y_speed)

                else:
                    self.canvas.move(self.car, self.x_speed, self.y_speed)

                time.sleep(0.01)
        finally:
            self.is_running = False
            self.canvas.delete(self.car)
            self.cars.remove(self)

            os.system("cls")
            print(f"Number of cars on the intersection: {len([car for car in self.cars if car.is_running])}")

    def is_off_map(self, x1, x2, y1, y2):
        return x1 <= 0 or y1 <= 0 or x2 >= self.canvas.winfo_width() or y2 >= self.canvas.winfo_height()
    def check_if_on_intersection(self, x1, x2, y1, y2):
        return x1 <= 450 and x2 >= 350 and y1 <= 350 and y2 >= 250;
    def any_car_on_intersection(self):
        return any([car for car in self.cars if car.is_on_intersection])
    
    
def get_random_color():
    de = ("%02x" % random.randint(0, 255))
    re = ("%02x" % random.randint(0, 255))
    we = ("%02x" % random.randint(0, 255))
    ge = "#"
    return ge + de + re + we
