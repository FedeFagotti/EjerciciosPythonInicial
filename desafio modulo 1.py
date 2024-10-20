#Ejercicio 1

nota_uno = 10
nota_dos = 6
nota_tres = 8

promedio = (nota_uno + nota_dos + nota_tres) / 3
print("El promedio es:", promedio)


#Ejercicio 2
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Sos mayor de edad")

else:
    print("Sos menor de edad")


#Ejercicio 3
sueldo_total = 300 * 6 + 500 * 4 + 700 * 2
sueldo_prom = sueldo_total / 12

print("El sueldo promedio es:", sueldo_prom)

if sueldo_prom < 300:
    print("Esta cobrando un sueldo bajo")

elif sueldo_prom < 900:
        print("Su sueldo es normal")

else:
    print("Su sueldo es mejor de lo normal")