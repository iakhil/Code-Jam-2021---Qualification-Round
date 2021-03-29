t = int(input())
for tt in range(t):
    x, y, s = map(str, input().split())
    x, y = int(x), int(y)
    cost = s.count('CJ') * x + s.count('JC') * y
    i = 0
    while i < len(s):
        m = ""
        if i > 0 and s[i] == "?":
            m = s[i-1] 
        while s[i] == "?":
            if i < (len(s) - 1):
                i += 1

            else:
                break
       
        f = m + s[i]
        if f == "CJ":
                cost += x 
        elif f == "JC":
                cost += y
        i += 1
    print("Case #{}:".format(tt + 1), end = " ")
    print(cost)
