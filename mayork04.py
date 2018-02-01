#Coding: UTF8

x=input("Introdueix un numero: ")
i=0
ZB=0

while (i<x):
	aux=input("Intodueix un nou: ")
	ZB+=1
	if aux>0:
		i+=1
print "Has escrit",ZB,"numeros",",",i,"de ellos positivos."
print "Final"
