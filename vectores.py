## Made for Python 3.10.x
class Vector3d:
    ##  Methods  ##
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

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
