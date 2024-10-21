matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
print(matriz)
fila = int(input("Ingrese el numero de fila: "))
columna = int(input("Ingrese el numero de columna: "))
if fila < len(matriz):
    if columna < len(matriz[fila]):
        print("El resultado es: ", matriz[fila][columna])
    else:
        print("Error en las columnas")
else:
    print("Error en las filas")
