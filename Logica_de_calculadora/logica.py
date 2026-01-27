

class Calculos:


    def __init__(self):
        pass
    
    def suma(self, numero1, numero2):
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
    
    
    def resta(self, numero1, numero2):
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
    
    def division (self, numero1, numero2):
        # Función que divide los dos numeros
        
        if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
            return "Error: Los numeros deben ser enteros o decimales"
        
        resultado = numero1 / numero2
        return resultado
    
    
    def multiplicacion (self, numero1, numero2):
        #Funcion que multiplicas los dos numeros

        if not isinstance(numero1, (int, float)) or not isinstance(numero2, (int, float)):
            return "Errpr: Los numeros deben ser enteros o decimales"
        
        resultado = numero1 * numero2
        return resultado