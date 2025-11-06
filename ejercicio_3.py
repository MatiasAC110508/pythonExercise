"""3. Gimnasio “Solo Leveling Fit” — Motivación + Bono
Pedir cuántos días entrenó esta semana.
    ≥ 4 días → "¡Excelente disciplina!" + gana 1 punto de energía
    2 o 3 → "Bien, pero puedes dar más"
    0 o 1 → "No aflojes, tú puedes mejorar"
Mostrar mensaje y si aplica, los puntos ganados."""

try:
    dias = int(input("¿Cuántos días has entrenado esta semana?: "))
    
    if dias < 0:
        print("Ingresa un número válido.")
    else:
        
        puntos = 0
        
        if dias >= 4:
            print("¡Excelente disciplina!")
            puntos = 1
        elif 2 <= dias <= 3:
            print("Bien, pero puedes dar más.")
        else: 
            print("No aflojes, tú puedes mejorar.")
        
        print(f"Has ganado un total de {puntos} puntos.")

except ValueError:
    print("Por favor, ingresa un número válido")
