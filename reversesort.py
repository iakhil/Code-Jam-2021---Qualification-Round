t = int(input())
for tt in range(t):
	n = int(input())
	L = list(map(int, input().split()))
	cost = 0 
	for i in range(n - 1):
		arr = L[i: n] 
		ind = L.index(min(arr)) + 1
		temp = L[i: ind]  
		L[i: ind] = temp[:: -1] 
		cost = cost + ind - i  
	print("Case #{}:".format(tt + 1), end = " ")
	print(cost) 



# L = [7, 6, 5, 4, 3, 2, 1] 
#L = [1, 5, 2, 3, 4]
#M = sorted(L)
#L = [4, 2, 1, 3]
n = len(L)

	#print("L:", L)
	#print(cost)




	# arr = L[i : n]
	# print(arr)
	# ind = L.index(min(arr))
	# print(ind)
	# temp = L[i : ind] 
	# #print(temp)
	# L[i: ind] = temp[::-1] 
	# cost += ind - i + 2 

	# for k in range(i, n):
	# 	t = L[k : n]
	# 	ind = L.index(min(t))
	# 	cost += ind - i + 1 
	# 	temp = L[i: ind] 
	# 	temp.sort(reverse = True)
	# 	L[i:ind] = temp 
	# 	print(L)
		# L[i: n] = 
		# temp = L[i: n] 
		# if len(temp) == 0:
		# 	break
		# else:
		# 	print(temp)
		# 	j = temp.index(min(temp))
		# 	cost += j - i + 1 
		# 	temp.sort(reverse = True) 
		# 	L = temp


