#Nested Loop
# - loop inside loop

'''
*****
*****
*****
*****
*****
'''
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()

print("=" * 50)


'''
12345
12345
12345
12345
12345
'''
for i in range(5):
    for j in range(5):
        print(j+1, end='')
    print()

print("=" * 50)


'''
*
**
***
****
*****
'''
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

print("=" * 50)

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
54321
5432
543
54
5
'''
for i in range(5):
    for j in range(5, i, -1):
        print(j, end='')
    print()

print("=" * 50)







