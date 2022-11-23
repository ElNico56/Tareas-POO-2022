## Made for Python 3.10.X
class Fraction:
    ## Atributos ##
    ##  Metodos  ##
    def __gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a if a > 0 else -a

    def __init__(self, numer=0, denom=1, reduce=True):
        if reduce:
            gcd = self.__gcd(numer, denom)
            numer = int(numer / gcd)
            denom = int(denom / gcd)

        self.numer = numer  # numerador
        self.denom = denom  # denominador
        if denom == 0:
            raise ZeroDivisionError("El numerador no puede ser 0!")

    def __str__(self):
        numer = self.numer
        denom = self.denom
        return f"{numer}/{denom}"

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return type(self)(numer, denom)

    def __sub__(self, other):
        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        return type(self)(numer, denom)

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return type(self)(numer, denom)

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        return type(self)(numer, denom)


if __name__ == "__main__":
    while True:
        in_numer = int(input("Numerador fraccion A \n> "))
        in_denom = int(input("Denominador fraccion A \n> "))

        A = Fraction(in_numer, in_denom)
        print("\nFraccion A: " + str(A) + "\n")

        in_numer = int(input("Numerador fraccion B \n> "))
        in_denom = int(input("Denominador fraccion B \n> "))

        B = Fraction(in_numer, in_denom)
        print("\nFraccion B: " + str(B) + "\n")

        operator = input("Operación? + - * / \n> ")

        if operator == "+":
            C = A + B
            print("\nA + B = " + str(C) + "")
        elif operator == "-":
            C = A - B
            print("\nA - B = " + str(C) + "")
        elif operator == "*":
            C = A * B
            print("\nA * B = " + str(C) + "")
        elif operator == "/":
            C = A / B
            print("\nA / B = " + str(C) + "")
        else:
            print("\nOperacion invalida")

        if input("\nContinuar? Y/N \n> ").upper() == "N":
            break
