'''
10001
01010
00100
01010
10001
'''
rows = 5
cols = 5
# i = 1,2,3,4,5
for i in range(1,rows+1):
    # j = 1,2,3,4,5
    for j in range(1,cols+1):
        if i == j or j == (cols + 1) - i:
            print("1", end="")
        else:
            print("0", end="")
    print()