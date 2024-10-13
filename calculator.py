print("!!!!!!!!!!!!!!Calcualtor!!!!!!!!!!!!")
#creating the calcualtor program

#Taking input from the users
num1=float(input("Enter the first number : "))
num2=float(input("Enter the second number: "))
print("You can perform +,-,*,/,%, operations on the numbers ")
#taking input of what operation they want to perform
op=input("Enter the operation you wnat to perform on numbers: ")
# using the if-else ladder instead of switch case statement because python does not have "built-in swicth statement"
if op == '+':
    print(f"{num1}+{num2}={num1+num2}")
elif op == '-':
    print(f"{num1}-{num2}={num1-num2}")
elif op == '*':
    print(f"{num1}*{num2}={num1*num2}")
elif op == '/':
    if num2!=0:
        print(f"{num1}/{num2}={num1/num2}")
    else:
        print(" Divide by zero is not possible")    
elif op == '%':
    print(f"{num1}%{num2}={num1%num2}")
else:
    print("invalid operation")           

