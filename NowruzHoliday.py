a, b, c = [int(x) for x in input().split()]
def maximum(a, b, c):
	list = [a, b, c]
	return max(list)
def minimum(a,b,c):
	list = [a, b, c]
	return min(list)
print(maximum(a,b,c)-minimum(a,b,c))