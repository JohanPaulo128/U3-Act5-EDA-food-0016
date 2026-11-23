import pandas as pd
import matplotlib.pyplot as plt
# Johan Paulo Aros Reveles
# 1. Leer el archivo CSV comida pais India
df_food_india = pd.read_csv('indian_food.csv')
print("\n--- DATOS LEÍDOS DESDE CSV 0016 ---")
print(df_food_india)
print("\n--- Mostrando nomre, comida + ingrdientes 0016 ---")
recetas = df_food_india[['name', 'ingredients']]
print(recetas)
print("\n--- tiempo de cocinado mostrar 10 ingrdientes con head 0016 ---")
nombre_y_hora = df_food_india[['name', 'cook_time']].head(10)
print(nombre_y_hora)