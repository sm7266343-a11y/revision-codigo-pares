
def sumar(a, b):
    return a - b  # Error: debería sumar

def restar(a, b):
    return a + b  # Error: debería restar

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b  # Error: no controla división entre cero

def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)  # Error: lista vacía

def es_mayor_de_edad(edad):
    return edad > 18  # Error: no incluye los 18 años


print("Suma:", sumar(10, 5))
print("Resta:", restar(10, 5))
print("Multiplicación:", multiplicar(10, 5))
print("División:", dividir(10, 0))
print("Promedio:", calcular_promedio([]))
print("¿Mayor de edad?:", es_mayor_de_edad(18))
