import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
	n = int(input())
	arr = [int(j) for j in input().split()]

	count = 0
	for x in arr:
		if abs(x) > 1:
			count += 1

	if count >= 2:
		print("no")
		continue

	neg1, pos1, zero, count = 0, 0, 0, 0
	for x in arr:
		if x == -1:
			neg1 += 1
		elif x == 1:
			pos1 += 1
		elif x == 0:
			zero += 1
		else:
			count = x

	arr = [-1]*min(neg1, 2) + [1]*min(pos1, 2) + [0]*min(zero, 2)
	if count != 0:
		arr += [count]
	
	s = set(arr)

	flag = 0
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if arr[i]*arr[j] not in s:
				flag = 1

	if flag == 1:
		print("no")
	else:
		print("yes")

