"""1. Panadería de Don Pancho — Descuentos por cantidades
La panadería de Don Pancho vende pan a $300 cada uno.
Reglas:
    Si compra más de 20 panes → 10% descuento
    Si compra más de 50 panes → 20% descuento
    Si ingresa una cantidad negativa, mostrar "Cantidad inválida"
Calcular y mostrar el total."""


precio = 300

try:

    cantidad = int(input("¿Cuántos panes quieres comprar?: "))
    
    # Validar cantidad
    if cantidad < 0:
        print("Cantidad inválida")
    else:
        # Calcular el total sin descuento
        total = precio * cantidad
        
        # Aplicar descuentos
        if cantidad > 50:
            total = total * 0.8  # 20% de descuento
        elif cantidad > 20:
            total = total * 0.9  # 10% de descuento
        
        # Mostrar el total
        print(f"Total a pagar: ${total:.2f}")
        
except ValueError:
    print("Porfavor ingrese un número.")