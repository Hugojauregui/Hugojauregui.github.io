import qrcode
import csv

# Cargar la lista de invitados
with open("lista_validacion.csv", "r") as file:
    lista_invitados = [line.strip().split(",") for line in file]

def validar_qr(id_invitado):
    for invitado in lista_invitados:
        if invitado[0] == id_invitado:
            if invitado[2] == "No usado":
                invitado[2] = "Usado"
                print(f"Acceso permitido: {invitado[1]}")
                return True
            else:
                print("Este QR ya fue usado.")
                return False
    print("ID no válido.")
    return False

# Simulación de escaneo
qr_escaneado = "ID: 001"  # Este sería el contenido del QR
id_invitado = qr_escaneado.split(": ")[1].strip()
validar_qr(id_invitado)

# Guardar cambios en la lista
with open("lista_validacion.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(lista_invitados)
