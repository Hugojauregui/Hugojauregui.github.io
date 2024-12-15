import qrcode

# Cargar la lista de invitados desde un archivo
with open("invitados.txt", "r") as file:
    invitados = file.readlines()

# Crear códigos QR
for invitado in invitados:
    try:
        # Separar los datos: ID, nombre, detalles
        id_invitado, nombre, detalles = invitado.strip().split(" - ")
        
        # Contenido del QR: formato estructurado
        contenido = (
            "*********** INVITACIÓN ***********\n"
            f"ID: {id_invitado}\n"
            f"Nombre: {nombre}\n"
            f"Evento: XV Años de Ana\n"
            f"Fecha: 20 de diciembre de 2024\n"
            f"Hora: 7:00 PM\n"
            f"Lugar: Salón Las Rosas\n"
            f"Detalles: {detalles}\n"
            "**********************************"
        )
        
        # Generar el código QR
        qr = qrcode.make(contenido)
        
        # Guardar la imagen del QR con el nombre del invitado
        filename = f"{id_invitado}_{nombre.replace(' ', '_')}.png"
        qr.save(filename)
        print(f"Código QR generado para {nombre}: {filename}")
    
    except ValueError:
        print(f"Formato incorrecto en la línea: {invitado.strip()}")

print("¡Todos los códigos QR han sido generados!")
