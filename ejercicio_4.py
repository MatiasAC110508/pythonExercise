"""4. Heladería “Frosty” — Sabor y topping
Sabores y precios:
    chocolate → $4.000
    vainilla → $3.500
Opcional: topping cuesta $1.000.
Si el usuario ingresa un sabor que no existe, mostrar "Sabor no disponible".
Si el sabor es válido, preguntar si quiere topping y calcular total."""


sabores = {"chocolate" : 4000, "vainilla" : 3500}

sabor = input("¿Qué sabor deseas?, tengo chocolate y vainilla: ").casefold()


if sabor not in sabores:
        print("Sabor no disponible.")
else:

    topping = input("¿Quieres agregar un topping?: ").casefold()

    total = sabores[sabor]

    if topping == "si":

        total = total + 1000

    print(f"Total a pagar: ${total}") 

