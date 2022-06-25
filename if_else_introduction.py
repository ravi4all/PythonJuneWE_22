num = int(input("Enter a number : "))

#indentation - by default 4 spaces (standard)
if num % 2 == 0:
    print("Number is even...")
else:
    print("Number is odd...")
    

if num % 2 == 0:print("Number is even...")
else:print("Number is odd...")

# If Else Expression
result = "Even" if num % 2 == 0 else "Odd"
print("Number is",result)
