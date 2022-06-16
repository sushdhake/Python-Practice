Python 3.10.1 (tags/v3.10.1:2cd268a, Dec  6 2021, 19:10:37) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Hello World")
Hello World
print("Hello Sushma" + " " + "Dhake")
Hello Sushma Dhake
firstname = input("Please enter your first name:")
Please enter your first name:Sushma
surname = input("Please enter your surname:")
Please enter your surname:Dhake
print ("Hello" ,firstname ,surname)
Hello Sushma Dhake
print("Hello" + " " + firstname + " " + lastname)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print("Hello" + " " + firstname + " " + lastname)
NameError: name 'lastname' is not defined. Did you mean: 'firstname'?
print("Hello" + " " + firstname +" " + surname)
Hello Sushma Dhake
number1 = float(input("Please enter the first number: "))
Please enter the first number: 22
number1
22.0
number2 = float(input("Please enter the second number: "))
Please enter the second number: 23
answer = number1 + number2
print(number1, "+" , number2, "=" answer)
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print(number1, "+", number2, "=", answer)
22.0 + 23.0 = 45.0
