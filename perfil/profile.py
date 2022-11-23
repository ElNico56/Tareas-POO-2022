class Profile:
    current_id = 0
    def __init__(self, nick, mail, password, avatar = "default.png", level = 0):
        self.id = type(self).current_id
        type(self).current_id += 1
        self.nick = nick
        self.mail = mail
        self.password = password
        self.avatar = avatar
        self.level = level
    def change_pass(self, old_pass, new_pass, confirm_pass):
        if (self.password != old_pass):
            print("Contraseña incorrecta!")
            return False
        if (new_pass != confirm_pass):
            print("Las contraseñas no coinciden")
            return False
        print("Contraseña cambiada con exito")
        self.password = new_pass
        return True
