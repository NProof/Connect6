def des(re, dir, len):
	dif = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
	return (re[0] + dif[dir][0] * len,re[1] + dif[dir][1] * len)
	
def inrange(des, limit = (-10, -10, 10, 10)):
	return limit[0] < des[0] and limit[2] > des[0] and limit[1] < des[1] and limit[3] > des[1]
	
# store = {(re, dir, len) : des(re,dir,len) \
	# for len in range(1,6) \
		# for dir in range(0,8) \
			# for re in allpos \
				# if des(re,dir,len) not in allpos}

for re in allpos:
	for dir in range(0,8):
		for len in range(1,6):
			dst = des(re,dir,len)
			if dst not in allpos and inrange(dst):
				store[(re, dir, len)] = dst
			
# for x, y in store.items():
	# print(x, "=>", y)
