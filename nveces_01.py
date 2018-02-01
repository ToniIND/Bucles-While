#Coding: UTF8

x=input("Introdueix un numero: ")
i=0
suma=0

while (i<x):

	aux=input("Indtodueix un numero nou: ")

	if aux>0:

		i+=1
		suma=aux+suma

print suma
print "Programa acavat"

