from profile import Account


def main():
    name = input("Ingrese su nombre\n> ")
    run = input("Ingrese su RUN\n> ")
    mail = input("Ingrese su correo\n> ")
    password = input("Ingrese su contraseña\n> ")
    if password != input("Confirme su contraseña\n> "):
        print("Las contraseñas no coinciden")
        return False

    user = Account(name, run, mail, password)
    user.print()
    while True:
        if input("Quiere depositar a su cuenta? (Y/N)\n> ").upper() == "N":
            break
        ammount = int(input("Ingrese la cantidad a depositar\n> "))
        user.deposit(ammount)
        user.print()


if __name__ == "__main__":
    main()
