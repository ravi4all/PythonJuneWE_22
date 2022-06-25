Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = 5
y = 7
x + y
12
x - y
-2
x * y
35
x / y
0.7142857142857143
20 / 5
4.0
20 % 5
0
15 % 2
1
5 * 5 * 5 * 5 * 5
3125
5 ** 2
25
5 ** 3
125
5 ** 4
625
5 ** 5
3125
21 / 8
2.625
21 // 8
2
22 / 7
3.142857142857143
22 // 7
3
x = 10
print(x)
10
x += 10
print(x)
20
z += 10
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    z += 10
NameError: name 'z' is not defined
x -= 10
x /= 10
x
1.0
x %= 9
x
1.0
x = 120
y = 23
x > y
True
x < y
False
x == y
False
y = 120
x > y
False
x < y
False
x == y
True
x >= y
True
x <= y
True
x != y
False
x = 45
y = 13
z = 100
x > y
True
x > z
False
x > y and x > z
False
y > x and y > z
False
z > x and z > y
True
x > y and x > z and y > x and y > z and z > x and z > y
False
x > y or x > z
True
(x > y and x > z) or (y > x and y > z) or (z > y and z > x)
True
not (x > y and x > z) or (y > x and y > z) or (z > y and z > x)
True
not( (x > y and x > z) or (y > x and y > z) or (z > y and z > x))
False
msg = "Hello Ram How are you...?"
name = "Ram"
name in msg
True
name not in msg
False
names = ["Ram", "Shyam", "Virat", "Rohit", "Sumit"]
"Rohit" in names
True
x = 10
y = 10
z = x
x == 10
True
y == 10
True
x == y
True
x is y
True
x = "Hello How are you ?"
y = "Hello How are you ?"
x == y
True
x is y
False
id(x)
1790490377984
id(y)
1790490497056
x is not y
True
