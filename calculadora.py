from Logica_de_calculadora.logica import Calculos as cl



# 2. MENÚ INTERACTIVO
# ====================================================

print("\n" + "=" * 50)
print("MODO INTERACTIVO - SELECCIONA UNA OPERACIÓN")
print("=" * 50)

try:
    # Solicitar entrada al usuario
    numero1 = float(input("\nIngrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    
    print("\n" + "-" * 50)
    print("OPERACIONES DISPONIBLES:")
    print("-" * 50)
    print("1. SUMA")
    print("2. RESTA")
    print("3. Division")
    print("4. Multiplicacion")
    print("-" * 50)
    operaciones = cl()
    opcion = input("\n¿Qué operación desea realizar? (1/2): ").strip()
    
    # Procesar la selección del usuario

    match opcion:

        case "1":
            resultado = operaciones.suma(numero1, numero2)
            operacion_texto = "+"
            print(f"\n✓ Resultado: {numero1} {operacion_texto} {numero2} = {resultado}")

        case "2":
            resultado = operaciones.resta(numero1, numero2)
            operacion_texto = "-"
            print(f"\n✓ Resultado: {numero1} {operacion_texto} {numero2} = {resultado}")

        case "3":
            resultado = operaciones.division(numero1, numero2)
            operacion_texto = "/"
            print(f"\n✓ Resultado: {numero1} {operacion_texto} {numero2} = {resultado}")

        case "4":
            resultado = operaciones.multiplicacion(numero1, numero2)
            operacion_texto = "*"
            print(f"\n✓ Resultado: {numero1} {operacion_texto} {numero2} = {resultado}")
        case _:
            print("\n✗ Error: Debe seleccionar 1 o 2")
            
except ValueError:
    print("\n✗ Error: Debe ingresar números válidos")

print("\n" + "=" * 50)
print("¡Gracias por usar la calculadora!")
print("=" * 50)


        
