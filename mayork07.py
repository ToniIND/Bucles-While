#Coding: UTF8

x=float(input("Indiqui el valor limit: "))
i=0
suma=0

while (x<=0):
	print ("El numero debe ser mayor a 0.")
	x=float(input("Indiqui el limit de nou: "))
while (suma<x):

	aux=float(input("Intodueix un nou: "))

 	suma=aux+suma

print "Has superat el limit, la suma dels numeros es: ",suma,"."
print "Final"
