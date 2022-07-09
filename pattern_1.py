'''
12345
12345
12345
12345
12345
'''
for i in range(5):
    for j in range(1,6):
        print(j, end='')
    print()
    
print('=' * 50)

'''
1
12
123
1234
12345
'''
for i in range(5):
    for j in range(i + 1):
        print(j + 1, end='')
    print()

print('=' * 50)

'''
*****
****
***
**
*
'''
for i in range(5):
    for j in range(5-i):
        print('*', end='')
    print()

print("=" * 50)


'''
12345
1234
123
12
1
'''
for i in range(5):
    for j in range(5-i):
        print(j+1, end='')
    print()

print("=" * 50)


'''
1
21
321
4321
54321
'''
for i in range(5):
    for j in range(i+1,0,-1):
        print(j, end='')
    print()

print("=" * 50)


'''
5
54
543
5432
54321
'''
for i in range(5):
    for j in range(5,4-i,-1):
        print(j, end='')
    print()

print("=" * 50)

















