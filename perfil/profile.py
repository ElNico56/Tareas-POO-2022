class Profile:
    _current_id = 0

    def __init__(self, nick, mail, password, avatar="default.png", level=0):
        self._id = type(self)._current_id
        type(self)._current_id += 1
        self._nick = nick
        self._mail = mail
        self._password = password
        self._avatar = avatar
        self._level = level

    def change_pass(self, old_pass, new_pass, confirm_pass):
        if self._password != old_pass:
            print("Contraseña incorrecta!")
            return False
        if new_pass != confirm_pass:
            print("Las contraseñas no coinciden")
            return False
        print("Contraseña cambiada con exito")
        self._password = new_pass
        return True

    def print(self):
        print(f"\nNickname: {self._nick}")
        print(f"Correo: {self._mail}")
        print(f"Contraseña: {self._password}")
        print(f"Nivel: {self._level}")
