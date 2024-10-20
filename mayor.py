# Ejercicio
# Ingresar dos numeros, en dos inputs, y luego compararlos y ver cual es el mayor, o si son iguales.

numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese otro numero: "))

if numero_1 > numero_2:
    print("El mayor es:", numero_1)

elif numero_1 == numero_2:
    print("Los numeros son iguales")

else:
    print("El mayor es:", numero_2)

print("Fin del programa")