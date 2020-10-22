valor_compra = float(input("digite el valor de la compra: "))
#crear la variable porcentaje descuento y leer el valor
descuento = valor_compra*0.1 #hay un descuento del 10%
valor_a_pagar = valor_compra - descuento
print("El valor a pagar es: " + str(valor_a_pagar))
print('Tu ahorro fue de: ' + str(descuento))