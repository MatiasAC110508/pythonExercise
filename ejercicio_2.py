"""2. Cine “La Estrella” — Tarifas por edad
Pedir la edad del cliente:
Edad 	     Precio
< 5 años 	 Entrada gratis
5 a 11   	 $5.000
12 a 59 	 $8.000
≥ 60         $4.000 (descuento adulto mayor)
Mostrar el precio.
Si la edad es negativa, mostrar error."""


precio = 8000

try:

    edad = int(input("¿Qué edad tienes?: "))

    if edad < 0:
        print("Edad inválida")
    else:
        # Calcular tarifa según la edad
        if edad < 5:
            tarifa = 0
        elif 5 <= edad <= 11:
            tarifa = 5000
        elif 12 <= edad <= 59:
            tarifa = 8000
        else:  # edad >= 60
            tarifa = 8000 - 4000
        
        print(f"Total a pagar: ${tarifa}")
        
except ValueError:
    print("Por favor, ingresa un número válido")