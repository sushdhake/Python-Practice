number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

print(number1)
print(number2)
print(round_number)

#Testing the int() function for a string. Gives error, as expected.
#print ("Hello write your name:")

#name = "Sushma"
#number = int(name)
#print (type(name))