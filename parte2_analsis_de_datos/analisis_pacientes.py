# analisis_pacientes.py
import pandas as pd

df = pd.read_csv("pacientes_avanzado.csv")

# Limpieza de datos
df["sintoma"] = df["sintoma"].fillna("no especificado")
df["temperatura"] = df["temperatura"].fillna(df["temperatura"].mean())
df["sexo"] = df["sexo"].fillna("no especificado")
df["edad"] = df["edad"].fillna(df["edad"].mean())
df["nombre"] = df["nombre"].fillna("no especificado")

# Estadísticas básicas
print("Número de pacientes:", df.shape[0])
print("Edad promedio por sexo:")
print(df.groupby("sexo")["edad"].mean())
print("Síntoma más común:")
print(df["sintoma"].value_counts())
print("Temperatura promedio por síntoma:")
print(df.groupby("sintoma")["temperatura"].mean())

# Filtrar pacientes sin síntomas y temperatura menor a 37
df_sin_sintomas = df[(df["sintoma"] == "ninguno") & (df["temperatura"] < 37)]
print("Pacientes sin síntomas y temperatura menor a 37:")
print(df_sin_sintomas.head())

# Guardar resultado
df_sin_sintomas.to_excel("pacientes_sin_sintomas.xlsx", index=False)
