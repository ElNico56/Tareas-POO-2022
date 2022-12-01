## Made for Python 3.10.X
class Fraction:
    ## Atributos ##
    ##  Metodos  ##
    @staticmethod
    def _gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a if a > 0 else -a

    def __init__(self, numer=0, denom=1, reduce=True):
        if reduce:
            gcd = self._gcd(numer, denom)
            numer = int(numer / gcd)
            denom = int(denom / gcd)

        self._numer = numer  # numerador
        self._denom = denom  # denominador
        if denom == 0:
            raise ZeroDivisionError("El numerador no puede ser 0!")

    def __str__(self):
        numer = self._numer
        denom = self._denom
        return f"{numer}/{denom}"

    def __add__(self, other):
        numer = self._numer * other._denom + other._numer * self._denom
        denom = self._denom * other._denom
        return type(self)(numer, denom)

    def __sub__(self, other):
        numer = self._numer * other._denom - other._numer * self._denom
        denom = self._denom * other._denom
        return type(self)(numer, denom)

    def __mul__(self, other):
        numer = self._numer * other._numer
        denom = self._denom * other._denom
        return type(self)(numer, denom)

    def __truediv__(self, other):
        numer = self._numer * other._denom
        denom = self._denom * other._numer
        return type(self)(numer, denom)


if __name__ == "__main__":
    while True:
        in_numer = int(input("Numerador fraccion A \n> "))
        in_denom = int(input("Denominador fraccion A \n> "))

        A = Fraction(in_numer, in_denom)
        print(f"\nFraccion A: {A}\n")

        in_numer = int(input("Numerador fraccion B \n> "))
        in_denom = int(input("Denominador fraccion B \n> "))

        B = Fraction(in_numer, in_denom)
        print(f"\nFraccion B: {B}\n")

        operator = input("Operación? + - * / \n> ")

        if operator == "+":
            C = A + B
            print(f"\nA + B = {C}")
        elif operator == "-":
            C = A - B
            print(f"\nA - B = {C}")
        elif operator == "*":
            C = A * B
            print(f"\nA * B = {C}")
        elif operator == "/":
            C = A / B
            print(f"\nA / B = {C}")
        else:
            print("\nOperacion invalida")

        if input("\nContinuar? (Y/N) \n> ").upper() == "N":
            break
