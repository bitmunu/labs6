with open('infile.txt', 'r', encoding="utf-8") as f:
    A = []

    for line in f:
        s = line.rstrip("\n")
        a, b, c = s.split()
        c = int(c)
        A.append((a, b, c))

A = sorted(A, key=lambda x: x[2])
max = A[0][2]
maxindex = 0
minindex = 0
min = 10

for i in range(0, len(A)):
    if A[i][2] > max:
        max = A[i][2]
        maxindex = i

    if A[i][2] < min:
        min = A[i][2]
        minindex = i

with open('ou1.txt', 'w', encoding="utf-8") as f:
    print(A[minindex], file=f)

with open('ou2.txt', 'w', encoding="utf-8") as f:
    print(A[maxindex], file=f)
