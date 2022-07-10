'''
1
2 3
4 5 6
7 8 9 10
'''
k = 0
for i in range(5):
    for j in range(i + 1):
        k += 1
        print(k, end=' ')
    print()

print('=' * 50)

'''
    *
   ***
  *****
 *******
*********
'''
for i in range(5):
    for j in range(5-i):
        print(' ', end='')
    for k in range(2*i + 1):
        print('*', end='')
    print()

print("=" * 50)

'''
     1
    2 3
   4 5 6
  7 8 9 10
11 12 13 14 15
'''
k = 0
for i in range(5):
    for j in range(i + 1):
        k += 1
        print(k, end=' ')
    print()

print('=' * 50)























