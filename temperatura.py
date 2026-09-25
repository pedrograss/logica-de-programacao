temperatura = float(input("Digite a temperatura: "))

if temperatura < 15:
    print("Muito frio")

elif temperatura >= 15 and temperatura <= 20:
    print("Frio")

elif temperatura >= 21 and temperatura <= 30:
    print("Agradável")

elif temperatura >= 31 and temperatura <= 40:
    print("Quente")

else:
    print("Muito quente")