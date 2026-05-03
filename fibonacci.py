def fibonacci(n):

	# write the code..
	if n <= 1:
		return n
	else:

		return fibonacci( n-1  )+fibonacci(n-2)

"""
n = int(input())
for i in range(1, n + 1):
	print(fibonacci(i), end=" ")
"""
pos=int(input())
if pos==0:
	print("0")
else:
	for i in range(pos):
		print(fibonacci(i),end=" ")