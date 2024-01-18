#3. Given an array arr[] and an integer K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.
# Note :-  l and r denotes the starting and ending index of the array.
# Example 1:
# Input:
# N = 6
# arr[] = 7 10 4 3 20 15
# K = 3
# L=0 R=5

#kth smallest: T.c=O(nlogn)
arr=[7 ,10, 4, 3, 20, 15]
k=3
arr.sort()
print(arr[k-1])

#kth largest: T.c=O(nlogn)
arr=[7 ,10, 4, 3, 20, 15]
k=3
arr.sort()
print(arr[len(arr)-k])

