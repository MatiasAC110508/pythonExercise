"""1. Panadería de Don Pancho — Descuentos por cantidades
La panadería de Don Pancho vende pan a $300 cada uno.
Reglas:
    Si compra más de 20 panes → 10% descuento
    Si compra más de 50 panes → 20% descuento
    Si ingresa una cantidad negativa, mostrar "Cantidad inválida"
Calcular y mostrar el total."""


"""2. Cine “La Estrella” — Tarifas por edad
Pedir la edad del cliente:
Edad 	     Precio
< 5 años 	 Entrada gratis
5 a 11   	 $5.000
12 a 59 	 $8.000
≥ 60         $4.000 (descuento adulto mayor)
Mostrar el precio.
Si la edad es negativa, mostrar error."""


"""3. Gimnasio “Solo Leveling Fit” — Motivación + Bono
Pedir cuántos días entrenó esta semana.
    ≥ 4 días → "¡Excelente disciplina!" + gana 1 punto de energía
    2 o 3 → "Bien, pero puedes dar más"
    0 o 1 → "No aflojes, tú puedes mejorar"
Mostrar mensaje y si aplica, los puntos ganados."""


"""4. Heladería “Frosty” — Sabor y topping
Sabores y precios:
    chocolate → $4.000
    vainilla → $3.500
Opcional: topping cuesta $1.000.
Si el usuario ingresa un sabor que no existe, mostrar "Sabor no disponible".
Si el sabor es válido, preguntar si quiere topping y calcular total."""

"""5. Librería “El Saber” — Descuento estudiante + cupón

Libro cuesta $25.000.

    Si es estudiante → 15% descuento
    Si además tiene cupón "LIBRO10" → 10% adicional sobre el valor ya descontado

Validar:

    Si no es estudiante, el cupón no aplica.
    Si ingresa cupón incorrecto, ignorarlo.

Mostrar total."""


"""6. Parqueadero “RapidCar” — Tarifa escalonada

Tarifa:

    0 a 5 horas: $2.000 x hora

        5 horas: $2.000 x hora + multa fija de $5.000

Validar horas:

    No permitir números negativos.

Mostrar valor total."""


"""7. Restaurante “El Sabor Colombiano” — Menú + bebida opcional + IVA

Menú: $12.000

Opciones bebida:

    sí → $3.000
    no → $0

Luego aplicar IVA del 8% al total final.
Mostrar valor con IVA incluido."""

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

