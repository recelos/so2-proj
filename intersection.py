import tkinter as tk

class Intersection:
    def __init__(self, frame):
        self.canvas = tk.Canvas(frame, width = 800, height = 600, bg = "white")
        self.draw_intersection(self.canvas)

    def draw_intersection(self, canvas):
        # Southern road
        canvas.create_line(350, 600, 350, 350, fill="black", width=1)
        canvas.create_line(450, 600, 450, 350, fill="black", width=1)
        canvas.create_line(400, 600, 400, 350, fill="grey", width=1, dash=(5, 3))

        #Northern road
        canvas.create_line(350, 0, 350, 250, fill="black", width=1)
        canvas.create_line(450, 0, 450, 250, fill="black", width=1)
        canvas.create_line(400, 0, 400, 250, fill="grey", width=1, dash=(5, 3))
        
        #Western road
        canvas.create_line(0, 250, 350, 250, fill="black", width=1)
        canvas.create_line(0, 350, 350, 350, fill="black", width=1)
        canvas.create_line(0, 300, 350, 300, fill="grey", width=1, dash=(5, 3))

        #Eastern road
        canvas.create_line(800, 250, 450, 250, fill="black", width=1)
        canvas.create_line(800, 350, 450, 350, fill="black", width=1)
        canvas.create_line(800, 300, 450, 300, fill="grey", width=1, dash=(5, 3))
        canvas.pack()
        canvas.update()
    def get_canvas(self):
        return self.canvas