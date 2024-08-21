# Solicitar al usuario una cantidad en dólares
usd = float(input("Introduce la cantidad en dólares estadounidenses (USD): "))

# Tasa de conversión fija
tasa_conversion = 0.91

# Convertir a euros
eur = usd * tasa_conversion

# Mostrar el resultado con 4 decimales
print(f"$ {usd} dólares son {eur:.4f} euros")