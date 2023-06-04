import time
import threading
import random

class Car:
    def __init__(self, canvas, direction, cars):
        self.canvas = canvas
        self.direction = direction
        self.cars = cars

        random_color = self.get_random_color()

        self.car = canvas.create_rectangle(direction.x1, direction.y1, direction.x2, direction.y2, fill = random_color)

        self.move_thread = None
        self.x_speed = direction.x_speed
        self.y_speed = direction.y_speed
        self.is_running = True

    def start(self):
        self.move_thread = threading.Thread(target = self.move)
        self.move_thread.start()

    def move(self):
        try:
            while True:
                x1, y1, x2, y2 = self.canvas.coords(self.car)

                if x1 <= 0 or y1 <= 0:
                    break
                elif x2 >= self.canvas.winfo_width() or y2 >= self.canvas.winfo_height():                    
                    break
                elif self.is_running is False:
                    break
                self.canvas.move(self.car, self.x_speed, self.y_speed)
                time.sleep(0.01)
        finally:
            self.canvas.delete(self.car)
            self.is_running = False
            self.cars.remove(self)
    
    def get_random_color(self):
        de=("%02x" % random.randint(0,255))
        re=("%02x" % random.randint(0,255))
        we=("%02x" % random.randint(0,255))
        ge="#"
        return ge + de + re + we