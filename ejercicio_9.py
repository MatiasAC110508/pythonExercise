"""9. Supermercado “AhorroMax” — Descuentos y envío
Cada producto cuesta $2.000.
Reglas:
30 unidades → 15% descuento
10 unidades → 5% descuento
Si el total después del descuento es < $50.000 → agregar $5.000 de envío
Calcular total final."""


precio_unitario = 2000

unidades = int(input("Ingrese la cantidad de unidades: "))

subtotal = unidades * precio_unitario

if unidades >= 30:
    descuento = 0.15
elif unidades >= 10:
    descuento = 0.05
else:
    descuento = 0

total_descuento = subtotal * (1 - descuento)

if total_descuento < 50000:
    total_final = total_descuento + 5000
else:
    total_final = total_descuento

print(f"Total final a pagar: ${total_final:,.0f}")