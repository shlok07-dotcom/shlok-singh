import numpy as np
r,c = map(int,input().split())
lst = []
for n in range(r):
	lst.extend(map(int,input().split()))
arr = np.array(lst).reshape(r,c)
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)