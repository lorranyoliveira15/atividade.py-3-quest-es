degrau:float; altura:float; altF:float

degrau=float(input("Digite a altura de cada degrau: "))

altura=float(input("Digite a altura que você deseja chegar: "))

altF=altura/degrau

print(f"Você necessitará subir {round(altF,2)} degraus")