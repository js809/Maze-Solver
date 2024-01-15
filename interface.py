import tkinter as tk


class Window:
    def __init__(self, width, height):
        self.__root = tk.Tk()
        self.__root.title("Maze Solver")
        self.__canvas = tk.Canvas(self.__root, height=height, width=width, bg="white")
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window Closed")

    def close(self):
        self.__running = False