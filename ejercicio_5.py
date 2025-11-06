"""5. Librería “El Saber” — Descuento estudiante + cupón

Libro cuesta $25.000.

    Si es estudiante → 15% descuento
    Si además tiene cupón "LIBRO10" → 10% adicional sobre el valor ya descontado

Validar:

    Si no es estudiante, el cupón no aplica.
    Si ingresa cupón incorrecto, ignorarlo.

Mostrar total."""




des_est = input("¿Eres estudiante?: ").casefold()

libro = 25000

if des_est == "si":

    total = libro * 0.85

    des_cup = input("Excelente, tienes un descuento del 15%, si tines cupón ingresa el codigo aquí si no solo escribe no: ")

    if des_cup =="LIBRO10":

        total = libro * 0.85 * 0.90

        print(f"Excelente, ahora tienes un descuento del 25%. El libro le costara ${total:.0f}.")


    elif des_cup == "no":
        print(f"Okay, el libro te cotara ${total:.0f}")
    else: 
        print(f"Cupon invalido, el libro te costara ${libro:.0f}.")
else:
    print(f"No tines descuentos, el libro le costara ${libro:.0f}.")