class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, newx, newy):
        self.x = newx
        self.y = newy

    def show(self):
        print(self.x, self.y)

    def dist(self):
        print(self.y - self.x)


b = Coordinates(0, 0)
b.move(1, 2)
b.show()
b.dist()

