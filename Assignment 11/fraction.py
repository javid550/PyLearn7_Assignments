class Fracton :
    def __init__(self,ss,mm) :
        # properties
        self.s = ss
        self.m = mm

    # methods
    def sum(self, f2) :
        # self.s
        # self.m

        s = self.s * f2.m + self.m * f2.s
        m = self.m * f2.m
        x = Fracton(s , m)
        return x

    def mul(self , f1) :
        result_s = f1.s * self.s
        result_m = f1.m * self.m
        x = Fracton(result_s , result_m)
        return x 

    def sub(self,f2) :
        s = self.s * f2.m - self.m * f2.s
        m = self.m * f2.m
        x = Fracton(s , m)
        return x

    def div(self,f2) :
        s = self.s * f2.m
        m = self.m * f2.m
        x = Fracton(s , m)
        return x

    def fraction_to_number(self) :
        return self.s / self.m 
    
    def simplify(self):
        for i in range(1 , self.m+1) :
            if self.s % i == 0 and self.m % i == 0 :
                BMMM = i

        self.s = self.s / BMMM
        self.m = self.m / BMMM
        self.show()

    def show(self):
        print(self.s , "/" , self.m)



a = Fracton(5 , 10)
a.show()

b = Fracton(9 , 3)
b.show()

x = b.mul(a)
x.show()

y = a.div(b)
y.show()   

a.simplify()
