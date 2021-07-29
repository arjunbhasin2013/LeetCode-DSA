'''
sorted array pairsum - two pointers approach
'''

def pair_sum(A, N, X):
	i = 0
	j = N - 1

	while(i < j):
	
		# If we find a pair
		if (A[i] + A[j] == X):
			return True
		elif(A[i] + A[j] < X):
			i += 1
		else:
			j -= 1
	return 0

arr = [3, 5, 9, 2, 8, 10, 11]
val = 17

print(pair_sum(arr, len(arr), val))