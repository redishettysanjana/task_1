# Sum of two numbers
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
sum = num1+num2
print(f"The sum of two numbers is:{sum}")

# Odd or Even Checker
num = int(input("Enter the number:"))
if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is a odd number")

# Factorial calculation
number=int(input("Enter the number:"))
factorial=1
for i in range(1,number+1):
    factorial *=i
print(f"The Factorial of {number} is: {factorial}")

# Fibonacci Sequence
n = int(input("Enter a number: "))
a, b = 0, 1
print("Fibonacci sequence is:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# String reverse
string=input("Enter a text:")
a=string[::-1]
print(f"The reversed String is:{a}")

# Palindrome check
x = input("Enter a word:")
if x == x[::-1]:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")

# Leap year chack
year = int(input("Enter the year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a leap year")
else:
    print("it's not a leap year")

#Armstrong number
num = int(input("\nEnter a number: "))
order = len(str(num))
sum_val = sum(int(digit) ** order for digit in str(num))
if num == sum_val:
    print("It is an armstrong number")
else:
    print("It is not an Armstrong number")
