## Made for Python 3.10.x
class Vector3d:
    ##    Methods    ##
    ### Constructor ###
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def __str__(self):
        return f"({self._x}, {self._y}, {self._z})"

    def __add__(self, other):
        x = self._x + other._x
        y = self._y + other._y
        z = self._z + other._z
        return type(self)(x, y, z)

    def __sub__(self, other):
        x = self._x - other._x
        y = self._y - other._y
        z = self._z - other._z
        return type(self)(x, y, z)

    def __mul__(self, num):
        x = self._x * num
        y = self._y * num
        z = self._z * num
        return type(self)(x, y, z)

    def __truediv__(self, num):
        x = self._x / num
        y = self._y / num
        z = self._z / num
        return type(self)(x, y, z)

    def dot(self, other):
        a = self._x * other._x
        b = self._y * other._y
        c = self._z * other._z
        return a + b + c

    def cross(self, other):
        x = self._y * other._z - self._z * other._y
        y = self._z * other._x - self._x * other._z
        z = self._x * other._y - self._y * other._x
        return type(self)(x, y, z)


if __name__ == "__main__":
    while True:
        print("Componentes vector A")
        in_x = float(input("X > "))
        in_y = float(input("Y > "))
        in_z = float(input("Z > "))

        vec_A = Vector3d(in_x, in_y, in_z)
        print(f"\nVector A: {vec_A}\n")

        print("Componentes vector B")
        in_x = float(input("X> "))
        in_y = float(input("Y> "))
        in_z = float(input("Z> "))

        vec_B = Vector3d(in_x, in_y, in_z)
        print(f"\nVector B: {vec_B}\n")

        operator = input("Operación? + - . x\n> ")

        if operator == "+":
            vec_C = vec_A + vec_B
            print(f"\nA + B = {vec_C}")

        elif operator == "-":
            vec_C = vec_A - vec_B
            print(f"\nA - B = {vec_C}")

        elif operator == ".":
            vec_C = vec_A.dot(vec_B)
            print(f"\nA . B = {vec_C}")

        elif operator == "x":
            vec_C = vec_A.cross(vec_B)
            print(f"\nA x B = {vec_C}")

        else:
            print("\nOperacion invalida")

        if input("\nContinuar? (Y/N) \n> ").upper() == "N":
            break
