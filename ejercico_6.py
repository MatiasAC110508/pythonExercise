"""6. Parqueadero “RapidCar” — Tarifa escalonada

Tarifa:

    0 a 5 horas: $2.000 x hora

        5 horas: $2.000 x hora + multa fija de $5.000

Validar horas:

    No permitir números negativos.

Mostrar valor total."""



try: 

    tiempo = int(input("¿Cuántas horas deseas ocupar nuestro parqueadero?: "))

    precio_h = 2000

    if tiempo < 0:
        print("Elige una cantidad de horas validas")
    elif tiempo < 5:

        total = precio_h * tiempo

        print(f"El valor a pagar es ${total:.0f}.")
    else:

        total = precio_h * tiempo + 5000
    
        print(f"El valor a pagar es ${total:.0f}.")

except ValueError:
    print("Porfavor utilice números")