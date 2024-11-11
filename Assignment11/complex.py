class Complex :
    def __init__ (self, real , image):
        self.real = real
        self.image = image 

    def show(self) :
        print(self.real , "+" , "i" , self.image)

    def sum(self , x):
        real = self.real + x.real
        img = self.image + x.image
        return Complex(real , img)

    def sub(self , x):
        real = self.real - x.real
        img = self.image - x.image
        return Complex(real , img)
    
    def mul(self , x):
        real = real = self.real * x.real - self.image * x.image
        img = self.real * x.image + self.image * x.real
        return Complex(real , img)

a = Complex(5 , 8)
b = Complex(4 , 5)
x = a.sub(b)
x.show()