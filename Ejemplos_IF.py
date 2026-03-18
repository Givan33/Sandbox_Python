from random import *
# Ejemplo con IF/ELSE sobre las calificaciones de una materia
'''
grade = float(input("What is the grade ? "))

if grade >= 90:
    print("You get an A")
else:
    if grade >= 80:
        print("You get an B")
    else:
        if grade >= 70:
            print("You get an C")
        else:
            if grade >= 60:
                print("You get an D")
            else:
                print("You get an F")
'''
print("\n")
rand_val = randint(1,10)
print("Random value generate is: "+ str(rand_val))


if rand_val == 1:
    print("Number " + str(rand_val) + " is I in roman number")
elif rand_val == 2:    
    print("Number " + str(rand_val) + " is II in roman number")
elif rand_val == 3:    
    print("Number " + str(rand_val) + " is III in roman number")
elif rand_val == 4:    
    print("Number " + str(rand_val) + " is IV in roman number")
elif rand_val == 5:    
    print("Number " + str(rand_val) + " is V in roman number")
elif rand_val == 6:    
    print("Number " + str(rand_val) + " is VI in roman number")
elif rand_val == 7:    
    print("Number " + str(rand_val) + " is VII in roman number")
elif rand_val == 8:    
    print("Number " + str(rand_val) + " is VIII in roman number")
elif rand_val == 9:    
    print("Number " + str(rand_val) + " is IX in roman number")
else:    
    print("Number " + str(rand_val) + " is X in roman number")
print("\n")

