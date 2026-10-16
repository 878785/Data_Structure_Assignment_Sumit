# Program to multiply two matrices

n = int(input("Enter the matrix size : "))
a = []
b = []
result = []

print("Enter the first matrix :")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    a.append(row)

print("Enter the second matrix : ")
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input()))
    b.append(row)

for i in range(n):
    row = []
    for j in range(n):
        total = 0
        for k in range(n):
            total = total + a[i][k] * b[k][j]
        row.append(total)
    result.append(row)

print("Product of matrices :")
for row in result:
    print(row)