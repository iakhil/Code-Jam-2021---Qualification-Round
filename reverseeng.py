def secondOp(n, p):
    if p < n - 1:
        return []
    l = []
    k = 0 
    c = 1
    for i in range(n - 1, 0, -1):
        c += 1

        if k + c + i - 1 >= p:
            r = p - k - i + 1
            l.append(r)
            for k in range(i - 1):
                l.append(1)
            k = p
            break

        k += c 
        l.append(c)
    if k < p:
        return []
    return l

def firstOp(l, res_list):
    length = len(res_list)
    for i in range(length):
        t = len(l) - (i + 2)
        sp = t + res_list[i]
        l = l[:t]+ list(reversed(l[t:sp])) + l[sp:]
    return l 

t = int(input())
for tt in range(t):
    n, p = map(int, input().split())
    l = list(range(1, n + 1))
    res_list = secondOp(n,p)
    l = firstOp(l, res_list)
    result = " "
    if res_list:
        for m in l:
            result += str(m) + " "
        print("Case #{}:".format(tt + 1), end = " ") 
        print(result)
    else:
        print("Case #{}:".format(tt + 1), end = " ")
        print("IMPOSSIBLE")
 






