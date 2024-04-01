enter = input("In what measurement do you want to convert your temperature? Input 'C' for celsius or'F' for fahrenheit: ")
if enter.lower() == "c" :
    fahrenheit = int(input("Enter the temperature in fahrenheit: "))
    celsius = (fahrenheit - 32)/1.8
    print(celsius)

else:
    celsius = int(input("Enter the temperature in celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    print(fahrenheit)

