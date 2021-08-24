import re 
"""Autor: Aguilar Plascencia Laura Fabiola
	Progrma que lee solo los números de un archivo, los suma y muestra el resultado"""
name = input("Ingresa el nombre del archivo:")
if len(name) <1 :
	name = "expRegulares.txt"
text= open(name,"r")
numbers = re.findall("[0-9]+",text.read())
inumbers = list()
for number in numbers:
	inumbers.append(int(number))

suma = sum(inumbers)
print(suma)
