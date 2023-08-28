a = input().split(", ")
a.sort()
len_a = int(len(a)/2)

small = []
big=[]

for i in range(len_a-1):
    small.append(a[i])
print(small)