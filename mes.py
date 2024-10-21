# Ejercicio
# Definir una lista con los meses del año. Luego pedir al usuario que ingrese un num de mes, del 1 al 12, y luego se tiene que mostrar
# el mes correspondiente a ese numero ingresado.
import sys

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
mes = int(input("Ingrese el numero de mes: "))
if mes < 1 or mes > 12:
    print("Solo se aceptan numeros entre 1 y 12.")
    sys.exit()

print("El mes es: ", meses[mes - 1])
