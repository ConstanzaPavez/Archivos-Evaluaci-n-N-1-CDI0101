# Script 1: Imprimir texto y nombres
print("Evaluación N°1 CCNA DEVNET")
print("Pavez")
print("Aguayo")

# Script 2: Solicitar información
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
codigo_seccion = input("Ingrese su Código-sección: ")
sede = input("Ingrese su sede: ")

# Script 3: Verificar tipo de ACL
numero_acl = int(input("Ingrese el número de ACL IPv4: "))

if numero_acl >= 1 and numero_acl <= 99:
  print("ACL Estándar")
elif numero_acl >= 100 and numero_acl <= 199:
  print("ACL Extendida")
else:
  print("El número no corresponde a una lista de acceso")