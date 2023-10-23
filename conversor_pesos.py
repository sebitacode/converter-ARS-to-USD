print ("conversor de pesos a dolares")
print("escriba los pesos que desee convertir:")
pesos = input()
pesos = float(pesos)
valor_dolar = 1200
dolar = pesos / valor_dolar
dolar= round(dolar,2)
dolar = str(dolar)
print("tienes:" + dolar + "USD")
