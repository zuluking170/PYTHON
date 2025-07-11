#Control statements  

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    print(num1, "Is greater than" , num2)
elif num2 > num1: 
    print(num2, "Is greater than" , num1)    
else: 
    print("Both numbers are equal") 
