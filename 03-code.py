x = 12
y = 33

#z = x + y
#print("Sum is",z)

# walrus operator
#print("Sum is",z := x + y)
#print("Value of z is",z)

#Variable Init + Print
print(f"""
Sum is {(a := x+y)}
Sub is {(b := x-y)}
Div is {(c := x/y):.2f}
Mul is {(d := x*y)}
""")
