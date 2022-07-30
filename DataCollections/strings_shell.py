Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
text = "Hello How are you..??"
len(text)
21
text[0]
'H'
text[1]
'e'
text[2]
'l'
text[-1]
'?'
text[-2]
'?'
text[-3]
'.'
text[0:4]
'Hell'
text[6:10]
'How '
text[6:9]
'How'
text[0:5]
'Hello'
text[:]
'Hello How are you..??'
text[0:]
'Hello How are you..??'
text[6:]
'How are you..??'
text[:10]
'Hello How '
text[0:20:2]
'HloHwaeyu.'
text[0:20:3]
'HlH eo.'
text[10:0]
''
text[10:0:-1]
'a woH olle'
text[10::-1]
'a woH olleH'
text[::-1]
'??..uoy era woH olleH'
dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
text.upper()
'HELLO HOW ARE YOU..??'
text.lower()
'hello how are you..??'
text.title()
'Hello How Are You..??'
text.swapcase()
'hELLO hOW ARE YOU..??'
text.capitalize()
'Hello how are you..??'
text.count('o')
3
text.count('a')
1
text.index('o')
4
text.index('o',0)
4
text.index('o',5)
7
text.index('o',8)
15
text.index('o',16)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    text.index('o',16)
ValueError: substring not found
text.index('how',16)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    text.index('how',16)
ValueError: substring not found
text.index('how')
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    text.index('how')
ValueError: substring not found
text.index('are')
10
text
'Hello How are you..??'
text.index('z')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    text.index('z')
ValueError: substring not found
text.find('z')
-1
text.find('h')
-1
text.find('a')
10
text
'Hello How are you..??'
