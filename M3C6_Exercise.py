class Usuario:
    def __init__(self, nombre_usuario, contrasena):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena

usuarioUno = Usuario("jfvelez2", "miContraseña123")

print(usuarioUno.nombre_usuario)
print(usuarioUno.contrasena)