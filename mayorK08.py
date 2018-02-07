#Coding: UTF8

x=int(input("Escrigui un numero parell: "))
	
while x%2 != 0:
	x=int(input("Escrigui un numero parell: "))
resp=raw_input("Vols escriure un altre per? (S/N) ")
while resp == "S" or resp == "s":
	x=int(input("Escrigui un numero parell: "))
	while x%2 != 0:
		x=int(input("Escrigui un numero parell: "))
	resp=raw_input("Vols escriure un altre per? (S/N) ")
while resp == "N" or resp == "n":
	print "fi"


