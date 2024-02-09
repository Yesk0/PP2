class shape:
    class square:
        lenght = int(input())
    
    def area(self):
        print(self.square.lenght ** 2)

x = shape()
x.area()

