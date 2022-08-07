# Create a Class for addition
class Addition:
    first = 0
    second = 0
    answer = 0

    # Parameterised constructor
    def __init__(self,f,s):
        self.first = f
        self.second = s

    def calculate(self):
        self.answer = self.first + self.second

    def display(self):
        print("First Number is " + str(self.first))
        print("Second Number is " + str(self.second))
        print("Addition of the two number is " + str(self.answer))

try:
    obj = Addition(float(input("Please enter a first num ")),float(input("Please enter a second num ")))
    obj.calculate()
    obj.display()
except ValueError:
    print("Invalid input. Please enter a number")