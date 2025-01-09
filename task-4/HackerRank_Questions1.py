n = int(input())

A = list(map(int, input().strip().split()))

m = int(input())

B = list(map(int, input().strip().split()))

c_A = {}
for i in A:
    if i in c_A:
        c_A[i] += 1
    else:
        c_A[i] = 1

c_B = {}
for j in B:
    if j in c_B:
        c_B[j] += 1
    else:
        c_B[j] = 1

miss_number = []
for k in c_B:
    if c_B[k] > c_A.get(k, 0):
        miss_number.append(k)

for i in sorted(miss_number):
    print(i,end=" ")
