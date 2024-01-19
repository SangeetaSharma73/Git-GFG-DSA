# Given an array, rotate the array by one position in clock-wise direction.
 

# Example 1:

# Input:
# N = 5
# A[] = {1, 2, 3, 4, 5}
# Output:
# 5 1 2 3 4
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)
arr=[1,2,3,4,5]
last=arr.pop()
arr.insert(0,last)
print(arr)
    
