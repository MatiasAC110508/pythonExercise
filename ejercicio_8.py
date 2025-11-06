"""8. Empresa “TecnoPlus” — Evaluación compuesta

El usuario ingresa dos notas (0.0 - 5.0):

    Prueba técnica (70%)
    Prueba lógica (30%)

Cálculo: nota_final = (tecnica * 0.7) + (logica * 0.3)

Condiciones:

    nota_final ≥ 3 → “Aprobado”
    2 ≤ nota_final < 3 → “Revisión”
    < 2 → “Reprobado”
    
Validar que las notas estén en rango."""


print("BIENVENIDO A LA CALCULADORA DE EVALUACIONES")
try:
    
    nota_1 = float(input("Ingresa aquí la nota número 1: "))

    nota_2 = float(input("Ingresa aquí la nota númro 2: "))

    if not (1.0 <= nota_1 <= 5.0) or not (1.0 <= nota_2 <= 5.0):
        rint("Porfavor ingrese un número entre 1.0 y 5.0.")
    else:

        nota = (nota_1 * 0.7) + (nota_2 * 0.3)

        if 3 > nota > 2:
            print(f"Estas en revisión por sacar {nota:.1f}.")
        elif nota >= 3:
            print(f"Has aprobado por sacar {nota:.1f}")
        else:
            print(f"Has reprobado por sacar {nota:.1f}.")

except ValueError:
    print("Porfavor ingresa un numero decimal.")


