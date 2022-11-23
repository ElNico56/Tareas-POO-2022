from profile import Profile

def main():
    nick = input("Ingrese su nickname\n> ")
    mail = input("Ingrese su correo\n> ")
    password = input("Ingrese su contraseña\n> ")
    if (password != input("Confirme su contraseña\n> ")):
        print("Las contraseñas no coinciden")
        return False

    user = Profile(nick, mail, password)
    while True:
        if (input("Quiere cambiar su contraseña? (Y/N)\n> ").upper() == "N"):
            break
        old_pass = input("Ingrese su antigua contraseña\n> ")
        new_pass = input("Ingrese su nueva contraseña\n> ")
        confirm_pass = input("Confirme su nueva contraseña\n> ")
        user.change_pass(old_pass, new_pass, confirm_pass)

if (__name__ == "__main__"):
    main()
