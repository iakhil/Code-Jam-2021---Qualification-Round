# import itertools
# import math 
# t = int(input())
# for tt in range(t):
# 		x, y, s = map(str, input().split())
# 		x, y = int(x), int(y) 
# 		list_s = list(s)
# 		nums = s.count('?') 
# 		if nums == 0:
# 			cost = x * s.count('CJ') + y * s.count('JC')
# 			print("Case #{}:".format(tt + 1), end = " ")
# 			print(cost) 
# 		elif nums == len(s):
# 			print("Case #{}:".format(tt + 1), end = " ")
# 			print(0)
# 		else:
# 			chars = ['C', 'J']
# 			ind = [pos for pos, char in enumerate(s) if char == '?']
# 			cart_len = 2 ** nums
# 			cost = math.inf
# 			for ite in range(cart_len):
# 				perms = [p for p in itertools.product(chars, repeat = nums)][ite] 
# 				for j in range(len(ind)):
# 					s = s[0 : ind[j]] + perms[j] + s[ind[j] + 1 : len(s)]
# 				x_occ, y_occ = s.count('CJ'), s.count('JC') 
			
# 				new_cost = x_occ * x + y_occ * y 
# 				print(perms, new_cost)
				
# 				if new_cost < cost:
# 					cost = new_cost 
			#print("Case #{}:".format(tt + 1), end = " ")
			#print(cost) 

#print(ind)
#print(s)
#print("Perms:", perms)
# s = "CJCJ"
# x, y = 4, 2
#list_s[ind[j]]	 = perms[i][j]
#s2 = s[0 : ind[j]] + perms[1] + s[ind[j] + 1 : len(s)]
				#ss = ''.join(list_s)
				#print("Cost s:", s.count('CJ') * x + s.count('JC') * y)
				#print("Cost ss:", ss.count('CJ') * x + ss.count('JC') * y)
				#print("SS:", ss)
				#print(ss.count('CJ') * x + ss.count('JC') * y)
				# print(x_occ, y_occ)
				#s = s_old
				#print(s)
				#print("Cost is: ", cost)
#print("New cost:", new_cost)
	#x_occ2, y_occ2 = s2.count('CJ')

# def countcost(s, x, y):
#     cost = 0t
#     cost = s.count("CJ")*x + s.count("JC")*y
#     return cost

t = int(input())
for tt in range(t):
	x, y, s = map(str, input().split())
	x, y = int(x), int(y)
	cost = s.count('CJ') * x + s.count('JC') * y
	char = ['CJ', 'JC']
	if s.count('?') == 0:
		print("Case #{}:".format(tt + 1), end = " ")
		print(cost)
	elif s.count('?') == len(s):
		print("Case #{}:".format(u + 1), end = " ")
		print(0)
	else:

	    ind = [pos for pos, char in enumerate(s) if char == '?']
	    #print(ind)
	    ind_i = 0 
	    i = 0 
	    while i < len(ind):
	    	if ind[i] == len(s) - 1:
	    		break 
	    	else:
		    	if ind[i] == 0:
		    		f = s[ind[i + 1]] 
		    	else:
		    		if ind[i] + 1 < len(s):
			    		f = s[ind[i] - 1] + s[ind[i] + 1]
			    		#print(f)
			    		if f == "CJ":
			    			cost += x 
			    		elif f == "JC":
			    			cost += y 
		    	i += 1
	    print("Case #{}:".format(tt + 1), end = " ")
		#print("Case #{}:".format(tt + 1), end = " ")
	    print(cost)
        # m =""
        # if i > 0 and s[i] == "?":
        #     m = s[i-1] 

        # while s[i] == "?":
        #     if i < (length-1):
        #         i = i+1

            # else:
            #     break
       	#print("m:", m)
       	# if ind_i == len(ind):
       	# 	break 
       	# else:
	       #  f = m + s[ind_i + 1]
	       #  ind_i += 1 
	       #  print(f)
	       #  if f == "CJ":
	       #          cost += x 
	       #  elif f == "JC":
	       #          cost += y
	       #  i+=1

    
