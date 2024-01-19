# Given two arrays a[] and b[] of size n and m respectively. The task is to find the number of elements in the union between these two arrays.

# Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.

# Note : Elements are not necessarily distinct.

# Example 1:

# Input:
# 5 3
# 1 2 3 4 5
# 1 2 3
# Output: 
# 5
# Expected Time Complexity : O(n+m)
# Expected Auxilliary Space : O(n+m)
a=[1,2,3,4,5]
b=[1,2,3]
a.extend(b)
print(len(set(a)))