Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Pen()
t.shape("turtle")
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.reset()
for i in range(4):
    t.forward(200)
    t.left(90)

    
t.reset()
for i in range(40):
    t.forward(200)
    t.left(90)

    
t.reset()
for i in range(40):
    t.forward(5 * i)
    t.left(45)

    
t.reset()
for i in range(40):
    t.forward(5 * i)
    t.left(90)

    
t.reset()
for i in range(40):
    print(i)
    t.circle(6*i)
    t.left(90)

    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
Traceback (most recent call last):
  File "<pyshell#27>", line 3, in <module>
    t.circle(6*i)
  File "C:\Python310\lib\turtle.py", line 1993, in circle
    self.speed(0)
  File "C:\Python310\lib\turtle.py", line 2175, in speed
    self.pen(speed=speed)
  File "C:\Python310\lib\turtle.py", line 2460, in pen
    self._update()
  File "C:\Python310\lib\turtle.py", line 2664, in _update
    screen._delay(screen._delayvalue) # TurtleScreenBase
  File "C:\Python310\lib\turtle.py", line 565, in _delay
    self.cv.after(delay)
  File "C:\Python310\lib\tkinter\__init__.py", line 834, in after
    self.tk.call('after', ms)
KeyboardInterrupt
t.reset()
t.speed(0)
for i in range(40):
    print(i)
    t.circle(6*i)
    t.left(90)

    
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
