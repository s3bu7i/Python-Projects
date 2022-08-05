
y=int(input("Enter the number :"))

class mathclass:
    def __init__(self,x):
        self.x=x
        self.y=1
        
    def factorial(self):
        if self.x == 0:
            print("O factorial equal 1")
        elif self.x < 0:
            print("Negative numbers are not factored")
        else:
            for i in range(1, self.x +1):
                self.y=self.y*i
        return self.y
    

    def absolute(self):
        return abs(self.x)
    
MathClass=mathclass(y)
print("This number is :",MathClass.x)
print(MathClass.factorial())
print(MathClass.absolute())
        
