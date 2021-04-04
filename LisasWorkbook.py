n, k = map(int, input().split())
lst = list(map(int, input().split()))
copylst = lst.copy()
prob = []
for i in range(n):
    l, r = 1, 0
    while (lst[i] >= 0):
        if (k < lst[i]):
            r += k
        else:
            r += lst[i]
        prob.append([l, r + 1])
        l += k
        lst[i] -= k
        if (r == copylst[i]):
            break
#print(prob)
count = 0
for i in range(len(prob)):
    if (i + 1 in range(prob[i][0], prob[i][1])):
        count += 1
        #print(i + 1)
print(count)
