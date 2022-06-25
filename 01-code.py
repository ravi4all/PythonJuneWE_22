x = 4
y = 21
z = x + y
div = x / y
print(z)
print("Sum is",z)

print("Sum of", x, "and", y, "is", z)

print("Sum is {}".format(z))
print("Sum of {} and {} is {}".format(x,y,z))
print("Sum of {1} and {2} is {0}".format(z,x,y))

print("Div of {} and {} is {:.3f}".format(x,y,div))
print(round(div,2))

#f-strings - format string
print(f"Sum of {x} and {y} is {z}")

print(f"Div of {x} and {y} is {div:.3f}")

print(f"Div of {x} and {y} is {round(div,2)}")






