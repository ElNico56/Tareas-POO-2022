## Made for Python 3.10.x
class Vector3d:
    ##  Metodos  ##
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        x = self.x
        y = self.y
        z = self.z
        return f"({x}, {y}, {z})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return type(self)(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return type(self)(x, y, z)

    def __mul__(self, num):
        x = self.x * num
        y = self.y * num
        z = self.z * num
        return type(self)(x, y, z)

    def __truediv__(self, num):
        x = self.x / num
        y = self.y / num
        z = self.z / num
        return type(self)(x, y, z)

    def dot(self, other):
        a = self.x * other.x
        b = self.y * other.y
        c = self.z * other.z
        return a + b + c

    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return type(self)(x, y, z)


if __name__ == "__main__":
    while True:
        in_x = float(input("Componente X vector A \n> "))
        in_y = float(input("Componente Y vector A \n> "))
        in_z = float(input("Componente Z vector A \n> "))

        A = Vector3d(in_x, in_y, in_z)
        print(f"\nVector A: {A}\n")

        in_x = float(input("Componente X vector B \n> "))
        in_y = float(input("Componente Y vector B \n> "))
        in_z = float(input("Componente Z vector B \n> "))

        B = Vector3d(in_x, in_y, in_z)
        print(f"\nVector B: {B}\n")

        operator = input("Operación? + - . x\n> ")

        if operator == "+":
            C = A + B
            print(f"\nA + B = {C}")

        elif operator == "-":
            C = A - B
            print(f"\nA - B = {C}")

        elif operator == ".":
            C = A.dot(B)
            print(f"\nA . B = {C}")

        elif operator == "x":
            C = A.cross(B)
            print(f"\nA x B = {C}")

        else:
            print("\nOperacion invalida")

        if input("\nContinuar? (Y/N) \n> ").upper() == "N":
            break
