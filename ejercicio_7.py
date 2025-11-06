"""7. Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA

Menú: $12.000

Opciones bebida:

    sí → $3.000
    no → $0

Luego aplicar IVA del 8% al total final.
Mostrar valor con IVA incluido."""


menu_precio = 12000
bebida_precio = 3000
iva = 0.08

menu = input("¿Quieres el menú del día?: ").casefold()

if menu not in ["si", "no"]:
    print('Responde "si" o "no"')
elif menu == "si":

    total = menu_precio * (1 + iva)

    bebida = input("¿Quieres una bebida?: ").casefold()
    if bebida not in ["si", "no"]:
        print('Responde "si" o "no"')
    else:
        if bebida == "si":

            total += bebida_precio * (1 + iva)

        print(f"El valor a pagar es ${total:.0f}.")
else:
    print("Gracias por visitarnos. Vuelva pronto.")
        


                    
    






    