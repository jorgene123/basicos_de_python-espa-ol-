# funciones.py
def calcular_area_rectangulo(base, altura):
    return base * altura

def es_par(num):
    return num % 2 == 0

area = calcular_area_rectangulo(5, 3)
print(f"Área del rectángulo: {area}")

num = 7
print(f"¿El número {num} es par? {es_par(num)}")
