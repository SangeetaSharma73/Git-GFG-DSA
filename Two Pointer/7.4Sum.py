# Given an array of integers, find all combination of four elements in the array whose sum is equal to a given value X. 
# Example:
# Input: array = {10, 2, 3, 4, 5, 9, 7, 8}, X = 23
# Output: 3 5 7 8
# Explanation: Sum of output is equal to 23, i.e. 3 + 5 + 7 + 8 = 23.
# Input: array = {1, 2, 3, 4, 5, 9, 7, 8}, X = 16
# Output: 1 3 5 7
# Explanation: Sum of output is equal to 16, i.e. 1 + 3 + 5 + 7 = 16.

# Brute Force-T.c=O(n^4)
#Python 3 implementation of above approach

# A naive solution to print all combination
# of 4 elements in A[] with sum equal to X 
def findFourElements(A, n, X):
	
	# Fix the first element and find 
	# other three
	for i in range(0,n-3):
		
		# Fix the second element and 
		# find other two
		for j in range(i+1,n-2):
			
			# Fix the third element 
			# and find the fourth
			for k in range(j+1,n-1):
				
				# find the fourth
				for l in range(k+1,n):
					
					if A[i] + A[j] + A[k] + A[l] == X:
						print ("%d, %d, %d, %d"
						%( A[i], A[j], A[k], A[l]))

# Driver program to test above function
A = [10, 2, 3, 4, 5, 9, 7, 8]
n = len(A)
X = 23
findFourElements (A, n, X)

#4Sum using Sorting-T.c=O(n^3)

# A sorting based solution to print all combination 
# of 4 elements in A[] with sum equal to X 
def find4Numbers(A, n, X):

	# Sort the array in increasing order, 
	# using library function for quick sort
	A.sort()

	# Now fix the first 2 elements one by 
	# one and find the other two elements 
	for i in range(n - 3):
		for j in range(i + 1, n - 2):
			
			# Initialize two variables as indexes 
			# of the first and last elements in 
			# the remaining elements
			l = j + 1
			r = n - 1

			# To find the remaining two elements, 
			# move the index variables (l & r)
			# toward each other.
			while (l < r):
				if(A[i] + A[j] + A[l] + A[r] == X):
					print(A[i], ",", A[j], ",", 
						A[l], ",", A[r])
					l += 1
					r -= 1
				
				elif (A[i] + A[j] + A[l] + A[r] < X):
					l += 1
				else: # A[i] + A[j] + A[l] + A[r] > X
					r -= 1

# Driver Code
if __name__ == "__main__":
	
	A = [1, 4, 45, 6, 10, 12]
	X = 21
	n = len(A)
	find4Numbers(A, n, X)
 