def sumar(a, b):
    """Suma dos números"""
    return a + b


def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b

def dividir(a, b):
    """Divide dos números"""
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

def potencia(a, b):
    """Calcula a elevado a b"""
    return a ** b

def raiz_cuadrada(a):
    """Calcula la raíz cuadrada"""
    if a < 0:
        return "Error: No se puede calcular raíz de número negativo"
    return a ** 0.5

# Menú interactivo
def calculadora():
    print("=== CALCULADORA ===")
    print("1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Potencia\n6. Raíz Cuadrada\n7. Salir")
    
    while True:
        opcion = input("\nSelecciona una operación (1-7): ")
        
        if opcion == "7":
            print("¡Hasta luego!")
            break
        
        if opcion == "6":
            num = float(input("Ingresa el número: "))
            print(f"Resultado: {raiz_cuadrada(num)}")
        elif opcion in ["1", "2", "3", "4", "5"]:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
            
            if opcion == "1":
                print(f"Resultado: {sumar(num1, num2)}")
            elif opcion == "2":
                print(f"Resultado: {restar(num1, num2)}")
            elif opcion == "3":
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif opcion == "4":
                print(f"Resultado: {dividir(num1, num2)}")
            elif opcion == "5":
                print(f"Resultado: {potencia(num1, num2)}")
        else:
            print("Opción inválida")

if __name__ == "__main__":
    calculadora()