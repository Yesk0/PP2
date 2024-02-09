class shape:
    class triangle:
        length , width = map(int, input().split())

    def area(self):
        print((self.triangle.length * self.triangle.width) / 2)


x = shape()
x.area()

