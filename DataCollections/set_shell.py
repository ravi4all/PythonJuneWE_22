Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = {3,2,4,5,78,9,5,3,3,5,6,8,8,23,34,7}
x
{2, 3, 4, 5, 6, 34, 8, 9, 7, 78, 23}
y = {1,2,3,4,32,2,4,6,78,19,16,43,3,6}
y
{32, 1, 2, 3, 4, 6, 43, 78, 16, 19}
x & y
{2, 3, 4, 6, 78}
x.intersection(y)
{2, 3, 4, 6, 78}
x | y
{1, 2, 3, 4, 5, 6, 7, 8, 9, 78, 16, 19, 23, 32, 34, 43}
x.union(y)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 78, 16, 19, 23, 32, 34, 43}
x - y
{34, 5, 7, 8, 9, 23}
x.difference(y)
{34, 5, 7, 8, 9, 23}
y - x
{32, 1, 43, 16, 19}
