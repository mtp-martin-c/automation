# ====================================================
# TIPOS DE VARIABLES EN PYTHON Y CALCULADORA
# ====================================================

# 1. TIPOS DE VARIABLES
# ====================================================

def suma(numero1, numero2):
    """
    Función que suma dos números.
    
    Parámetros:
        numero1: primer número (int o float)
        numero2: segundo número (int o float)
    
    Retorna:
        La suma de los dos números (int o float)
    """
    if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
        return "Error: Los números deben ser enteros o decimales"
    
    resultado = numero1 + numero2
    return resultado


def resta(numero1, numero2):
    """
    Función que resta dos números.
    
    Parámetros:
        numero1: primer número (int o float)
        numero2: segundo número (int o float)
    
    Retorna:
        La resta de los dos números (int o float)
    """
    if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
        return "Error: Los números deben ser enteros o decimales"
    
    resultado = numero1 - numero2
    return resultado


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
    print("-" * 50)
    
    opcion = input("\n¿Qué operación desea realizar? (1/2): ").strip()
    
    # Procesar la selección del usuario
    if opcion == "1":
        resultado = suma(numero1, numero2)
        operacion_texto = "+"
        print(f"\n✓ Resultado: {numero1} {operacion_texto} {numero2} = {resultado}")
    
    elif opcion == "2":
        resultado = resta(numero1, numero2)
        operacion_texto = "-"
        print(f"\n✓ Resultado: {numero1} {operacion_texto} {numero2} = {resultado}")
    
    else:
        print("\n✗ Error: Debe seleccionar 1 o 2")
        
except ValueError:
    print("\n✗ Error: Debe ingresar números válidos")

print("\n" + "=" * 50)
print("¡Gracias por usar la calculadora!")
print("=" * 50)