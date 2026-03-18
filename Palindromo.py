my_string = "Eleven animals I slam in a net" 
#input("Write a sentence to check if is a palindromo: ")
my_string = my_string.replace(" ","")
my_string = my_string.lower()
len_my_string = len(my_string)
palindromo = True

for i in range(len_my_string//2):
    if ord(my_string[i]) == ord(my_string[len_my_string - i - 1]):
        continue
    else:
        palindromo = False
        break
        
if palindromo:
    print("It's a palindrome")
else:
    print("It's NOT a palindrome")

'''
otra version en codigo seria la siguiente
text = input("Enter text: ")

# Remove all spaces...
text = text.replace(' ','')

# ... and check if the word is equal to reversed itself
if len(text) > 1 and text.upper() == text[::-1].upper(): #esta linea esta chida porque usa la opcion de python para invertir una cadena usando el slicing 
	print("It's a palindrome")
else:
	print("It's not a palindrome")

'''