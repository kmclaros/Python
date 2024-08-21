# Solicitar al usuario un número entero positivo
tope = int(input("Ingrese un número entero positivo como tope: "))

# Inicializar la variable para la sumatoria
suma_total = 0

# Sumar todos los números desde 1 hasta el tope
for i in range(1, tope + 1):
    suma_total += i

# Imprimir el resultado final
print(f"La sumatoria de los números desde 1 hasta {tope} es: {suma_total}")
