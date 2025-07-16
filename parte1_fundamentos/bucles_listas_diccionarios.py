# bucles_listas_diccionarios.py

#lista
materias = ["biología", "procesamiento de bioseñales", "anatomía humana", "circuitos eléctricos"]
materias.append("embebidos")
materias.remove("procesamiento de bioseñales")

print("Materias:", materias)

#diccionario
yo = {
    "nombre": "Juanito",
    "edad": 78,
    "ciudad": "Tangamandapio",
    "carrera": "Licenciado en videojuegos"
}

print(f"Carrera: {yo['carrera']}")
yo["fav"] = "python"
yo["ciudad"] = "Zapopan"

print("Datos actualizados:", yo)

#bucle for
for i in range(1, 6):
    print(f"Cuadrado de {i} es {i**2}")

frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

contador = 0
while contador < 5:
    print(contador)
    contador += 1


