class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b #Changed the return result from b - a to a - b

    def multiply(self, a, b):
        result = 0
        for i in range(abs(b)):
            result = self.add(result, a)

        if b < 0:
            result = -result

        return result

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        result = 0
        negative = (a < 0) != (b < 0)

        a = abs(a)
        b = abs(b)

        while a >= b:
            a = self.subtract(a, b)
            result += 1

        if negative:
            result = -result

        return result
    
    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot modulo by zero")

        negative = a < 0
        a = abs(a)
        b = abs(b)

        while a >= b:
            a = self.subtract(a, b)

        if negative:
            a = -a

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

    print("Example: modulo: ", calc.modulo(-5, 4))