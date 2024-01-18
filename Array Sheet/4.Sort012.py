#4. Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
# Example 1:
# Input: 
# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.
arr=[0,2,1,2,0]
n=len(arr)
# using bubble sort-T.c=O(n^2)
for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)
#using selection-T.c=O(n^2)
for i in range(n):
    mini=i
    for j in range(i+1,n):
        if arr[mini]>arr[j]:
            mini=j
    arr[mini],arr[i]=arr[i],arr[mini]
print(arr)
#using sort method-T.c=O(nlog)
arr.sort()
print(arr)