class Calculator:

    def add(self, a, b):
            return a + b


    def multiply(self, a, b):
        return a * b

    def subtract(self, a, b):
        return a - b

    def divide(self, a, b):
        if a != 0:
            return a / b

    def exposant(self, a,b):
        return a**b 
        

    def pourcent(self, a, b):
        if a <= 100 : 
            return (a/100)*b 
            

    def average(self, a,b):
        return (a+b)/2