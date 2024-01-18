# Given an array of integers, you have to find three numbers such that the sum of two elements equals the third element.
# Examples: 
# Input : {5, 32, 1, 7, 10, 50, 19, 21, 2}
# Output : 21, 2, 19
# Input : {5, 32, 1, 7, 10, 50, 19, 21, 0}
# Output : no such triplet exist

#1.Brute Force-T.c=O(n^3)
def findTriplet(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]==arr[k] or arr[i]+arr[k]==arr[j] or arr[j]+arr[k]==arr[i]:
                    print('Numbers are:',arr[i],arr[j],arr[k])
                    return 
    print("No such triplet exists")
arr = [5, 32, 1, 7, 10, 50, 19, 21, 2] 
n = len(arr) 
findTriplet(arr,n)

#2.Two pointer- T.c=O(n^2)
def findTriplet(arr,n):
    arr.sort()
    i=n-1
    while i>=0:
        j=0
        k=i-1
        while j<k:
            if arr[i]==arr[j]+arr[k]:
                print('numbers are',arr[i],arr[j],arr[k])
                return 
            elif arr[i]>arr[j]+arr[k]:
                j+=1
            else:
                k-=1
        i-=1
    print('No such triplet exists')
arr = [ 5, 32, 1, 7, 10, 50, 19, 21, 2 ] 
n = len(arr) 
findTriplet(arr, n) 

#3.using binary search-O(n^2logn)

# Python program to find three numbers 
# such that sum of two makes the 
# third element in array 
from functools import cmp_to_key 
def mycmp(a, b): 
	return a - b 
def search(sum, start, end, arr): 
	while (start <= end): 
		mid = (start + end) // 2
		if (arr[mid] == sum): 
			return True
		elif (arr[mid] > sum): 
			end = mid - 1
		else: 
			start = mid + 1

	return False

# Utility function for finding 
# triplet in array 
def findTriplet(arr, n): 
	# sort the array 
	arr.sort(key = cmp_to_key(mycmp)) 
	# initialising nested loops 
	for i in range(n): 
		for j in range(i + 1,n): 
			if (search((arr[i] + arr[j]), j, n - 1, arr)): 
				print(f"numbers are {arr[i]} {arr[j]} {( arr[i] + arr[j] )}") 
				return
	# No such triplet is found in array 
	print("No such triplet exists") 
# driver program 
arr = [ 5, 32, 1, 7, 10, 50, 19, 21, 2 ] 
n = len(arr) 
findTriplet(arr, n) 

                    