import random
n = 25
matrix = []
for x in range(n):
    matrix.append([0] * n)



for x in range(n):
    for y in range(0,x):
        val = random.randint(1,1000)
        matrix[x][y] = val
        matrix[y][x] = val
print("====================")
print(matrix)
print("====================")
for x in range(n):
    for y in range(n):
        print(str(matrix[x][y]) + ",", end = '')
    print("")
print("====================")