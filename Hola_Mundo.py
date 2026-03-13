#Comenzamos con python
print("Hola Mundo de Python")


for i in range(0,5):
    print(i,"hola")

myBoolena = True
if myBoolena:
    print("Verdad")

# this is a comment

#Potencia de un numero
power = 4**4
print(power)

#Division entera
division_entera = 16//5
print(division_entera)

#Operacion Modulo
modulo = 7%2
print(modulo)

#Operadores de asignacion
numero1 = 5
numero1 +=7
print(numero1)

# ejemplo con Print()
print((3-2)*5+(2**4)/16)

# ejemplo de como evitar el error en el calculo con numeros flotantes
ex1 = 1.23 + 2.80
print("Con error flotante:", ex1)
ex2 = (123 + 280) / 100
print("Sin error flotante:", ex2)
ex3 = 1.23 + 2.80
print("Sin error usando round():",round(ex3,2))
print((1090 + 21105)/100)


#aqui ponemos otro comentaio y borramos el anterior