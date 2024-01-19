# Given an array Arr[] of N integers. Find the contiguous sub-array(containing at least one number) which has the maximum sum and return its sum.


# Example 1:

# Input:
# N = 5
# Arr[] = {1,2,3,-2,5}
# Output:
# 9
# Expected Time Complexity: O(N)
# Expected Auxiliary Space: O(1)
arr=[1,2,3,-2,5]
maxi_sum=float('-inf')
s=0
for i in range(len(arr)):
    s+=arr[i]
    if s>maxi_sum:
        maxi_sum=s
    if s<0:
        s=0
print(maxi_sum)