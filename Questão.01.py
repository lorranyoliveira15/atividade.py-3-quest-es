pe:float
jarda:float 
milha:float
pole:float


pe = float(input("Informe a medida em pe: "))

pole = pe*12
jarda = pe/12
milha = jarda/760

print(f"Sua medida em jardas: {round(jarda,2)}, Em polegadas: {round(pole,2)}, Em milhas: {round(milha,2)}.")