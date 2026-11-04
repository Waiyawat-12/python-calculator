class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b #Changed the return result from b - a to a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b): #replaced the range (b+1) with range (b) because range start from 0 not 1
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        result = 0
        while a+1 > b:
            a = self.subtract(a, b)
            result += 1
        return result
    
    def modulo(self, a, b):
        while b <= a:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))