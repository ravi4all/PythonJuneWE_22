# If Else Ladder
a = 12
b = 21
c = 30

if a > b and a > c:
    print("A is greatest...")
elif b > a and b > c:
    print("B is greatest...")
else:
    print("C is greatest...")

result = "A" if a > b and a > c else "B" if b > a and b > c else "C"
print(result,"is greatest...")
