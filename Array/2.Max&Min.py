# Given an array of size N. The task is to find the maximum and the minimum element of the array using the minimum number of comparisons.

# Examples:

# Input: arr[] = {3, 5, 4, 1, 9}
# Output: Minimum element is: 1
#         Maximum element is: 9

# Input: arr[] = {22, 14, 8, 17, 35, 3}
# Output:  Minimum element is: 3
#          Maximum element is: 35
arr=[22, 14, 8, 17, 35, 3]
#using method - T.c=O(n) & S.c=O(1)
print(max(arr))
print(min(arr))

#using loop- T.c=O(n)
minimum=float('inf')
maximum=float('-inf')
for i in range(len(arr)):
    if minimum>arr[i]:
        minimum=arr[i]
    if maximum<arr[i]:
        maximum=arr[i]
print(maximum)
print(minimum)

#using sort- Tc=O(nlogn)
def min_max(arr):
    arr.sort()
    return arr[0],arr[-1]
minimum,maximum=min_max(arr)
print(minimum,maximum)


