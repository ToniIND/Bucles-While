#coding: UTF8

num1=int(input("escriba un numero: "))

num2=int(input("escriba un numero mayor que:"))

while (num1<num2):

	num1=num2

	num2=int(input("Intentalo de nuevo: "+str(num1)+": "))

print "Los numeros que has elejido són:",num1,",",num2
