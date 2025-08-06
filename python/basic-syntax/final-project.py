#Sistema de Gestión de Biblioteca
libros = []
Usuarios = {}

def registrar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    publicacion = input("Ingrese el año de publicacioón: ")
    genero = input("Ingrese el genero del libro: ")

    libro = {
        "Título": titulo,
        "Autor": autor,
        "Publicación": publicacion,
        "Genero": genero
    }

    libros.append(libro)
    print("Libro añadido.")

def buscar_libros():
    titulo_libro_buscar = input("Ingrese el título del libro a buscar: ")
    autor_libro_buscar = input("Ingrese el autor del libro a buscar: ")
    
    for libro in libros:
        if libro['Título'] == titulo_libro_buscar and libro['Autor'] == autor_libro_buscar:
            print(f"Libro {titulo_libro_buscar} encontrado.")
            print(f"Título: {titulo_libro_buscar}\nAutor: {autor_libro_buscar}\nPublicación: {libro['Publicación']}\nGenero: {libro['Genero']}")
        
        else:
            print("Libro no encontrado.")

def Actualizar_info_libro():
    for i, libro in enumerate(libros):
        print(f"{i} Título: {libro['Título']}, Autor: {libro['Autor']}, Publicación: {libro['Publicación']}, Genero: {libro['Genero']}")

    seleccion = input("Seleccione el indíce del libro: ")
    if seleccion.isdigit() and 0 <= int(seleccion) < len(libros):
        libro_seleccionado = libros[int(seleccion)]
        while True:
            clave_a_modificar = input("Ingrese la clave que desee modificar: ")
            if clave_a_modificar in libro_seleccionado:
                valor_a_modificar = input("Modifique el nuevo valor: ")
                libro_seleccionado[clave_a_modificar] = valor_a_modificar
                print("Valor modificado.")
                break
            else:
                print("Error: Clave no encontrada.")
                continue
    else:
        print("Error: índice fuera de rango.")
            
def eliminar_libro():
    for i, libro in enumerate(libros):
        print(f"{i} Título: {libro['Título']}, Autor: {libro['Autor']}, Publicación: {libro['Publicación']}, Genero: {libro['Genero']}")
    
    libro_seleccion = input("Seleccione el libro a eliminar: ")
    if libro_seleccion.isdigit() and 0 <= int(libro_seleccion) < len(libros):
        libros.pop(int(libro_seleccion))
        print("Libro eliminado.")
    else:
        print("Error: índice fuera de rango o libro inexistente.")

def listar_libros():
    print("\nLista de libros:")
    for i, libro in enumerate(libros):
        print(f"{i} Título: {libro['Título']}, Autor: {libro['Autor']}, Publicación: {libro['Publicación']}, Genero: {libro['Genero']}.\n")

def registrar_usuario():
    usuario = input("Cree un usuario: ")
    contraseña = input("Cree una contraseña: ")

    Usuarios[usuario] = contraseña
    print("Usuario registrado.")

def login(Usuario, Contraseña):

    for usuario, contraseña in Usuarios.items():
        if usuario == Usuario and contraseña == Contraseña:
            return True
        else:
            return False
        
def gestionar_usuarios():
    print("\nLista de usuarios:")
    for i in enumerate(Usuarios):
        for usuario, contraseña in Usuarios.items():
            print(f"{i} User: {usuario} Password: {contraseña}\n")
    while True:
        print("1. Eliminar usuario")
        print("2. Salir")
        seleccion = input("Selección: ")
        if seleccion == "1":
            usuario_eliminar = input("Ingrese el usuario a eliminar: ")
            if usuario_eliminar in Usuarios:
                Usuarios.pop(usuario_eliminar)
                print("\nUsuario eliminado.\n")
                break
            else:
                print("Usuario no encontrado.")
                continue
        elif seleccion == "2":
            print("Saliste del gestionador de usuarios.")
            break

def Estadisticas():
    print("Total de libros en la biblioteca:")
    print(len(libros))

def biblioteca_main():
    
    try:
        registrar_usuario()
        while True:
            Usuario = input("Ingrese su usuario: ")
            Contraseña = input("Ingrese su contraseña: ")
            Acceso = login(Usuario, Contraseña)
            if Acceso == True:
                print("Acceso concedido.")
                break
            else:
                print("Acceso denegado.")
                continue

        while True:
            print("\nBIENVENIDO AL MECANISMO DE GESTIÓN DE BIBLIOTECA")
            print("1. Registrar libro")
            print("2. Buscar libro")
            print("3. Modificar libro")
            print("4. Eliminar libro")
            print("5. Listar libros")
            print("6. Salir\n")
            for usuario in Usuarios:
                if usuario == "Admin":
                    print("7. Gestionar usuarios")
            
            seleccion = input("Selecciona una opción: ")

            if seleccion == "1":
                registrar_libro()
            
            elif seleccion == "2":
                buscar_libros()

            elif seleccion == "3":
                Actualizar_info_libro()

            elif seleccion == "4":
                eliminar_libro()

            elif seleccion == "5":
                listar_libros()

            elif seleccion == "6":
                print("Saliendo del programa...")
                print("Saliste del gestionador.")
                break

            elif seleccion == "7":
                gestionar_usuarios()

            else:
                print("Selección no válida.")
        
    except ValueError:
        print("Error: valor no válido.")
    
if __name__ == "__main__":
    biblioteca_main()

