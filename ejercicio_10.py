"""10. Club “Noche Estelar” — Acceso + validación documento
Pedir edad y documento.
Reglas:
Edad ≥ 18 → puede entrar solo si tiene documento.
Si la edad < 18 → "Entrada denegada"
Si tiene 18 o más pero no tiene documento → "Debe presentar documento" """


edad = int(input("Ingrese su edad: "))
tiene_documento = input("¿Tiene documento? (si/no): ").strip().casefold()

if edad < 18:
    print("Entrada denegada.")
elif edad >= 18 and tiene_documento == "si":
    print("Puede entrar.")
else:
    print("Debe presentar documento.")