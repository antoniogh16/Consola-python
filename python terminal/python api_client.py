import requests

# Definir directamente el token Bearer
TOKEN = "1|Mdq1ojbeDeZ5LFdI2gSKDzUokgEOGJ7qwdWV4Wnb1212812a"

# URL base de la API
BASE_URL_BOOKS = "https://bibliotecagg.bibliotecatilinos.istigen23.com/api/books"        # Endpoint para libros
BASE_URL_GENRES = "https://bibliotecagg.bibliotecatilinos.istigen23.com/api/genres"      # Endpoint para géneros
BASE_URL_CLIENTES = "https://bibliotecagg.bibliotecatilinos.istigen23.com/api/clientes"  # Endpoint para clientes
BASE_URL_LOANS = "https://bibliotecagg.bibliotecatilinos.istigen23.com/api/loans"        # Endpoint para préstamos
BASE_URL_PERSONAL = "https://bibliotecagg.bibliotecatilinos.istigen23.com/api/personals"  # Endpoint para personal

# Encabezados para la autenticación
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

# ----------------------------- #
#       Funciones de Books      #
# ----------------------------- #

def obtener_libros():
    """Obtiene y muestra todos los libros de la API."""
    try:
        respuesta = requests.get(BASE_URL_BOOKS, headers=headers)
        respuesta.raise_for_status()
        libros = respuesta.json()
        print("\nLibros obtenidos exitosamente:")
        if libros:
            for libro in libros:
                print(libro)
        else:
            print("No se encontraron libros.")
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud GET de libros: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

def crear_libro(nombre, isbn, genre_id, paginas, image_path=None):
    """Crea un nuevo libro con los datos proporcionados."""
    payload = {
        "name": nombre,
        "isbn": isbn,
        "genre_id": genre_id,
        "pages": paginas,
        "image_path": image_path
    }
    try:
        respuesta = requests.post(BASE_URL_BOOKS, headers=headers, json=payload)
        respuesta.raise_for_status()
        libro_creado = respuesta.json()
        print("\nLibro creado exitosamente:")
        print(libro_creado)
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud POST de libros: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

def eliminar_libro(book_id):
    """Elimina un libro específico por su ID."""
    url_eliminar = f"{BASE_URL_BOOKS}/{book_id}"
    try:
        respuesta = requests.delete(url_eliminar, headers=headers)
        if respuesta.status_code == 204:
            print(f"\nLibro con ID {book_id} eliminado exitosamente.")
        elif respuesta.status_code == 404:
            print(f"\nLibro con ID {book_id} no encontrado.")
        else:
            print(f"\nFallo al eliminar el libro. Estado: {respuesta.status_code}")
            print(f"Detalles: {respuesta.text}")
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud DELETE de libros: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

def actualizar_libro(book_id, datos_actualizados):
    """Actualiza los datos de un libro existente."""
    url_actualizar = f"{BASE_URL_BOOKS}/{book_id}"
    try:
        respuesta = requests.put(url_actualizar, headers=headers, json=datos_actualizados)
        respuesta.raise_for_status()
        libro_actualizado = respuesta.json()
        print("\nLibro actualizado exitosamente:")
        print(libro_actualizado)
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud PUT de libros: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

# ----------------------------- #
#       Funciones de Genres     #
# ----------------------------- #

def obtener_generos():
    """Obtiene y muestra todos los géneros de la API."""
    try:
        respuesta = requests.get(BASE_URL_GENRES, headers=headers)
        respuesta.raise_for_status()
        generos = respuesta.json()
        print("\nGéneros obtenidos exitosamente:")
        if generos:
            for genero in generos:
                print(genero)
        else:
            print("No se encontraron géneros.")
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud GET de géneros: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

def crear_genero(nombre):
    """Crea un nuevo género con el nombre proporcionado."""
    payload = {
        "name": nombre
    }
    try:
        respuesta = requests.post(BASE_URL_GENRES, headers=headers, json=payload)
        respuesta.raise_for_status()
        genero_creado = respuesta.json()
        print("\nGénero creado exitosamente:")
        print(genero_creado)
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud POST de géneros: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

def eliminar_genero(genero_id):
    """Elimina un género específico por su ID."""
    url_eliminar = f"{BASE_URL_GENRES}/{genero_id}"
    try:
        respuesta = requests.delete(url_eliminar, headers=headers)
        if respuesta.status_code == 204:
            print(f"\nGénero con ID {genero_id} eliminado exitosamente.")
        elif respuesta.status_code == 404:
            print(f"\nGénero con ID {genero_id} no encontrado.")
        else:
            print(f"\nFallo al eliminar el género. Estado: {respuesta.status_code}")
            print(f"Detalles: {respuesta.text}")
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud DELETE de géneros: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

# ----------------------------- #
#      Funciones de Clientes    #
# ----------------------------- #

def obtener_clientes():
    """Obtiene y muestra todos los clientes de la API."""
    try:
        respuesta = requests.get(BASE_URL_CLIENTES, headers=headers)
        respuesta.raise_for_status()
        clientes = respuesta.json()
        print("\nClientes obtenidos exitosamente:")
        if clientes:
            for cliente in clientes:
                print(cliente)
        else:
            print("No se encontraron clientes.")
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud GET de clientes: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

def crear_cliente(nombre, apellido, correo, telefono=None, direccion=None):
    """Crea un nuevo cliente con los datos proporcionados."""
    payload = {
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "telefono": telefono,
        "direccion": direccion
    }
    try:
        respuesta = requests.post(BASE_URL_CLIENTES, headers=headers, json=payload)
        respuesta.raise_for_status()
        cliente_creado = respuesta.json()
        print("\nCliente creado exitosamente:")
        print(cliente_creado)
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud POST de clientes: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

def eliminar_cliente(cliente_id):
    """Elimina un cliente específico por su ID."""
    url_eliminar = f"{BASE_URL_CLIENTES}/{cliente_id}"
    try:
        respuesta = requests.delete(url_eliminar, headers=headers)
        if respuesta.status_code == 204:
            print(f"\nCliente con ID {cliente_id} eliminado exitosamente.")
        elif respuesta.status_code == 404:
            print(f"\nCliente con ID {cliente_id} no encontrado.")
        else:
            print(f"\nFallo al eliminar el cliente. Estado: {respuesta.status_code}")
            print(f"Detalles: {respuesta.text}")
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud DELETE de clientes: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

def actualizar_cliente(cliente_id, datos_actualizados):
    """Actualiza los datos de un cliente existente."""
    url_actualizar = f"{BASE_URL_CLIENTES}/{cliente_id}"
    try:
        respuesta = requests.put(url_actualizar, headers=headers, json=datos_actualizados)
        respuesta.raise_for_status()
        cliente_actualizado = respuesta.json()
        print("\nCliente actualizado exitosamente:")
        print(cliente_actualizado)
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud PUT de clientes: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

# ----------------------------- #
#      Funciones de Loans       #
# ----------------------------- #

def obtener_prestamos():
    """Obtiene y muestra todos los préstamos de la API."""
    try:
        respuesta = requests.get(BASE_URL_LOANS, headers=headers)
        respuesta.raise_for_status()
        prestamos = respuesta.json()
        print("\nPréstamos obtenidos exitosamente:")
        if prestamos:
            for prestamo in prestamos:
                print(prestamo)
        else:
            print("No se encontraron préstamos.")
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud GET de préstamos: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

def crear_prestamo(libro_id, cliente_id, fecha_prestamo, fecha_devolucion=None, estado='activo'):
    """Crea un nuevo préstamo con los datos proporcionados."""
    payload = {
        "libro_id": libro_id,
        "cliente_id": cliente_id,
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion": fecha_devolucion,
        "estado": estado
    }
    try:
        respuesta = requests.post(BASE_URL_LOANS, headers=headers, json=payload)
        respuesta.raise_for_status()
        prestamo_creado = respuesta.json()
        print("\nPréstamo creado exitosamente:")
        print(prestamo_creado)
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud POST de préstamos: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

def eliminar_prestamo(prestamo_id):
    """Elimina un préstamo específico por su ID."""
    url_eliminar = f"{BASE_URL_LOANS}/{prestamo_id}"
    try:
        respuesta = requests.delete(url_eliminar, headers=headers)
        if respuesta.status_code == 204:
            print(f"\nPréstamo con ID {prestamo_id} eliminado exitosamente.")
        elif respuesta.status_code == 404:
            print(f"\nPréstamo con ID {prestamo_id} no encontrado.")
        else:
            print(f"\nFallo al eliminar el préstamo. Estado: {respuesta.status_code}")
            print(f"Detalles: {respuesta.text}")
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud DELETE de préstamos: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

def actualizar_prestamo(prestamo_id, datos_actualizados):
    """Actualiza los datos de un préstamo existente."""
    url_actualizar = f"{BASE_URL_LOANS}/{prestamo_id}"
    try:
        respuesta = requests.put(url_actualizar, headers=headers, json=datos_actualizados)
        respuesta.raise_for_status()
        prestamo_actualizado = respuesta.json()
        print("\nPréstamo actualizado exitosamente:")
        print(prestamo_actualizado)
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud PUT de préstamos: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

# ----------------------------- #
#     Funciones de Personal     #
# ----------------------------- #

def obtener_personal():
    """Obtiene y muestra todo el personal de la API."""
    try:
        respuesta = requests.get(BASE_URL_PERSONAL, headers=headers)
        respuesta.raise_for_status()
        personal = respuesta.json()
        print("\nPersonal obtenido exitosamente:")
        if personal:
            for miembro in personal:
                print(miembro)
        else:
            print("No se encontraron miembros de personal.")
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud GET de personal: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

def crear_personal(nombre, apellido, correo, puesto, telefono=None, fecha_contratacion=None):
    """Crea un nuevo miembro de personal con los datos proporcionados."""
    payload = {
        "nombre": nombre,
        "apellido": apellido,
        "correo": correo,
        "puesto": puesto,
        "telefono": telefono,
        "fecha_contratacion": fecha_contratacion
    }
    try:
        respuesta = requests.post(BASE_URL_PERSONAL, headers=headers, json=payload)
        respuesta.raise_for_status()
        personal_creado = respuesta.json()
        print("\nMiembro de personal creado exitosamente:")
        print(personal_creado)
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud POST de personal: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

def eliminar_personal(personal_id):
    """Elimina un miembro de personal específico por su ID."""
    url_eliminar = f"{BASE_URL_PERSONAL}/{personal_id}"
    try:
        respuesta = requests.delete(url_eliminar, headers=headers)
        if respuesta.status_code == 204:
            print(f"\nMiembro de personal con ID {personal_id} eliminado exitosamente.")
        elif respuesta.status_code == 404:
            print(f"\nMiembro de personal con ID {personal_id} no encontrado.")
        else:
            print(f"\nFallo al eliminar el miembro de personal. Estado: {respuesta.status_code}")
            print(f"Detalles: {respuesta.text}")
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud DELETE de personal: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

def actualizar_personal(personal_id, datos_actualizados):
    """Actualiza los datos de un miembro de personal existente."""
    url_actualizar = f"{BASE_URL_PERSONAL}/{personal_id}"
    try:
        respuesta = requests.put(url_actualizar, headers=headers, json=datos_actualizados)
        respuesta.raise_for_status()
        personal_actualizado = respuesta.json()
        print("\nMiembro de personal actualizado exitosamente:")
        print(personal_actualizado)
    except requests.exceptions.HTTPError as err:
        print(f"\nError en la solicitud PUT de personal: {err}")
        print(f"Detalles: {respuesta.text}")
    except Exception as e:
        print(f"\nOcurrió un error: {e}")

# ----------------------------- #
#        Menú Interactivo       #
# ----------------------------- #

def mostrar_menu():
    """Muestra el menú interactivo al usuario."""
    print("\n--- Cliente de API de Biblioteca ---")
    print("1. Obtener todos los libros (GET)")
    print("2. Crear un nuevo libro (POST)")
    print("3. Actualizar un libro existente (PUT)")
    print("4. Eliminar un libro (DELETE)")
    print("5. Obtener todos los géneros (GET)")
    print("6. Crear un nuevo género (POST)")
    print("7. Eliminar un género (DELETE)")
    print("8. Obtener todos los clientes (GET)")
    print("9. Crear un nuevo cliente (POST)")
    print("10. Actualizar un cliente existente (PUT)")
    print("11. Eliminar un cliente (DELETE)")
    print("12. Obtener todos los préstamos (GET)")
    print("13. Crear un nuevo préstamo (POST)")
    print("14. Actualizar un préstamo existente (PUT)")
    print("15. Eliminar un préstamo (DELETE)")
    print("16. Obtener todo el personal (GET)")
    print("17. Crear un nuevo miembro de personal (POST)")
    print("18. Actualizar un miembro de personal existente (PUT)")
    print("19. Eliminar un miembro de personal (DELETE)")
    print("20. Salir")

def main():
    """Función principal que ejecuta el menú interactivo."""
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            obtener_libros()
        elif opcion == "2":
            nombre = input("Nombre del libro: ")
            isbn = input("ISBN: ")
            try:
                genre_id = int(input("ID del género: "))
                paginas = int(input("Número de páginas: "))
            except ValueError:
                print("\nEl ID del género y el número de páginas deben ser números enteros.")
                continue
            image_path = input("Ruta de la imagen (opcional): ") or None
            crear_libro(nombre, isbn, genre_id, paginas, image_path)
        elif opcion == "3":
            try:
                book_id = int(input("ID del libro a actualizar: "))
            except ValueError:
                print("\nEl ID del libro debe ser un número entero.")
                continue
            nombre = input("Nuevo nombre del libro (opcional): ")
            isbn = input("Nuevo ISBN (opcional): ")
            try:
                genre_id_input = input("Nuevo ID del género (opcional): ")
                genre_id = int(genre_id_input) if genre_id_input else None
                paginas_input = input("Nuevo número de páginas (opcional): ")
                paginas = int(paginas_input) if paginas_input else None
            except ValueError:
                print("\nEl ID del género y el número de páginas deben ser números enteros.")
                continue
            image_path = input("Nueva ruta de la imagen (opcional): ") or None

            # Construir el diccionario solo con los campos proporcionados
            datos = {}
            if nombre:
                datos["name"] = nombre
            if isbn:
                datos["isbn"] = isbn
            if genre_id is not None:
                datos["genre_id"] = genre_id
            if paginas is not None:
                datos["pages"] = paginas
            if image_path:
                datos["image_path"] = image_path

            if not datos:
                print("\nNo se proporcionaron datos para actualizar.")
                continue

            actualizar_libro(book_id, datos)
        elif opcion == "4":
            try:
                book_id = int(input("ID del libro a eliminar: "))
                eliminar_libro(book_id)
            except ValueError:
                print("\nEl ID del libro debe ser un número entero.")
        elif opcion == "5":
            obtener_generos()
        elif opcion == "6":
            nombre_genero = input("Nombre del género: ")
            crear_genero(nombre_genero)
        elif opcion == "7":
            try:
                genero_id = int(input("ID del género a eliminar: "))
                eliminar_genero(genero_id)
            except ValueError:
                print("\nEl ID del género debe ser un número entero.")
        elif opcion == "8":
            obtener_clientes()
        elif opcion == "9":
            nombre = input("Nombre del cliente: ")
            apellido = input("Apellido del cliente: ")
            correo = input("Correo del cliente: ")
            telefono = input("Teléfono del cliente (opcional): ") or None
            direccion = input("Dirección del cliente (opcional): ") or None
            crear_cliente(nombre, apellido, correo, telefono, direccion)
        elif opcion == "10":
            try:
                cliente_id = int(input("ID del cliente a actualizar: "))
            except ValueError:
                print("\nEl ID del cliente debe ser un número entero.")
                continue
            nombre = input("Nuevo nombre del cliente (opcional): ")
            apellido = input("Nuevo apellido del cliente (opcional): ")
            correo = input("Nuevo correo del cliente (opcional): ")
            telefono = input("Nuevo teléfono del cliente (opcional): ")
            direccion = input("Nueva dirección del cliente (opcional): ")

            # Construir el diccionario solo con los campos proporcionados
            datos = {}
            if nombre:
                datos["nombre"] = nombre
            if apellido:
                datos["apellido"] = apellido
            if correo:
                datos["correo"] = correo
            if telefono:
                datos["telefono"] = telefono
            if direccion:
                datos["direccion"] = direccion

            if not datos:
                print("\nNo se proporcionaron datos para actualizar.")
                continue

            actualizar_cliente(cliente_id, datos)
        elif opcion == "11":
            try:
                cliente_id = int(input("ID del cliente a eliminar: "))
                eliminar_cliente(cliente_id)
            except ValueError:
                print("\nEl ID del cliente debe ser un número entero.")
        elif opcion == "12":
            obtener_prestamos()
        elif opcion == "13":
            try:
                libro_id = int(input("ID del libro para el préstamo: "))
                cliente_id = int(input("ID del cliente para el préstamo: "))
            except ValueError:
                print("\nEl ID del libro y el ID del cliente deben ser números enteros.")
                continue
            fecha_prestamo = input("Fecha de préstamo (YYYY-MM-DD): ")
            fecha_devolucion = input("Fecha de devolución (opcional, YYYY-MM-DD): ") or None
            estado = input("Estado del préstamo (por defecto 'activo'): ") or 'activo'
            crear_prestamo(libro_id, cliente_id, fecha_prestamo, fecha_devolucion, estado)
        elif opcion == "14":
            try:
                prestamo_id = int(input("ID del préstamo a actualizar: "))
            except ValueError:
                print("\nEl ID del préstamo debe ser un número entero.")
                continue
            libro_id_input = input("Nuevo ID del libro para el préstamo (opcional): ")
            cliente_id_input = input("Nuevo ID del cliente para el préstamo (opcional): ")
            fecha_prestamo = input("Nueva fecha de préstamo (opcional, YYYY-MM-DD): ")
            fecha_devolucion = input("Nueva fecha de devolución (opcional, YYYY-MM-DD): ")
            estado = input("Nuevo estado del préstamo (opcional): ")
            
            # Construir el diccionario solo con los campos proporcionados
            datos = {}
            if libro_id_input:
                try:
                    datos["libro_id"] = int(libro_id_input)
                except ValueError:
                    print("\nEl ID del libro debe ser un número entero.")
                    continue
            if cliente_id_input:
                try:
                    datos["cliente_id"] = int(cliente_id_input)
                except ValueError:
                    print("\nEl ID del cliente debe ser un número entero.")
                    continue
            if fecha_prestamo:
                datos["fecha_prestamo"] = fecha_prestamo
            if fecha_devolucion:
                datos["fecha_devolucion"] = fecha_devolucion
            if estado:
                datos["estado"] = estado
            
            if not datos:
                print("\nNo se proporcionaron datos para actualizar.")
                continue
            
            actualizar_prestamo(prestamo_id, datos)
        elif opcion == "15":
            try:
                prestamo_id = int(input("ID del préstamo a eliminar: "))
                eliminar_prestamo(prestamo_id)
            except ValueError:
                print("\nEl ID del préstamo debe ser un número entero.")
        elif opcion == "16":
            obtener_personal()
        elif opcion == "17":
            nombre = input("Nombre del miembro de personal: ")
            apellido = input("Apellido del miembro de personal: ")
            correo = input("Correo del miembro de personal: ")
            puesto = input("Puesto del miembro de personal: ")
            telefono = input("Teléfono del miembro de personal (opcional): ") or None
            fecha_contratacion = input("Fecha de contratación (opcional, YYYY-MM-DD): ") or None
            crear_personal(nombre, apellido, correo, puesto, telefono, fecha_contratacion)
        elif opcion == "18":
            try:
                personal_id = int(input("ID del miembro de personal a actualizar: "))
            except ValueError:
                print("\nEl ID del miembro de personal debe ser un número entero.")
                continue
            nombre = input("Nuevo nombre del miembro de personal (opcional): ")
            apellido = input("Nuevo apellido del miembro de personal (opcional): ")
            correo = input("Nuevo correo del miembro de personal (opcional): ")
            puesto = input("Nuevo puesto del miembro de personal (opcional): ")
            telefono = input("Nuevo teléfono del miembro de personal (opcional): ")
            fecha_contratacion = input("Nueva fecha de contratación (opcional, YYYY-MM-DD): ")
            
            # Construir el diccionario solo con los campos proporcionados
            datos = {}
            if nombre:
                datos["nombre"] = nombre
            if apellido:
                datos["apellido"] = apellido
            if correo:
                datos["correo"] = correo
            if puesto:
                datos["puesto"] = puesto
            if telefono:
                datos["telefono"] = telefono
            if fecha_contratacion:
                datos["fecha_contratacion"] = fecha_contratacion
            
            if not datos:
                print("\nNo se proporcionaron datos para actualizar.")
                continue
            
            actualizar_personal(personal_id, datos)
        elif opcion == "19":
            try:
                personal_id = int(input("ID del miembro de personal a eliminar: "))
                eliminar_personal(personal_id)
            except ValueError:
                print("\nEl ID del miembro de personal debe ser un número entero.")
        elif opcion == "20":
            print("\nSaliendo...")
            break
        else:
            print("\nOpción inválida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
