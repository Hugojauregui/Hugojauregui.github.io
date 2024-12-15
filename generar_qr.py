import qrcode

# Base URL para los pases
base_url = "https://hugojauregui.github.io/index.html?invitado="

# Cargar la lista de invitados desde un archivo
with open("invitados.txt", "r") as file:
    invitados = file.readlines()

# Crear códigos QR
for invitado in invitados:
    id_invitado, nombre, _ = invitado.strip().split(" - ")
    
    # Generar la URL personalizada
    url = f"{base_url}{id_invitado}"
    
    # Crear el QR con la URL
    qr = qrcode.make(url)
    
    # Guardar el QR
    filename = f"{id_invitado}_{nombre.replace(' ', '_')}.png"
    qr.save(filename)
    print(f"Código QR generado para {nombre}: {filename}")

print("¡Todos los códigos QR han sido generados!")
