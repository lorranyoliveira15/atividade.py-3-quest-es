pesoS:float; gm:float; pesoF:float

pesoS=float(input("Digite o peso do saco de ração: "))

gm=float(input("Digite a quantidade de ração dada para cada gato: "))

pesoF=pesoS-(gm*2)/24

print(f"Apoś 5 dias sobrará {round(pesoF,2)}kg")