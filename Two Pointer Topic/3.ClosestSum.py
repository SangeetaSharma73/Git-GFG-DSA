# 3.Given a sorted array and a number x, find a pair in an array whose sum is closest to x.
# Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
# Output: 22 and 30
arr=[10,22,28,29,30,40]
x=54
# Brute Force-Tc=O(n^2)
prv=0
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]<=x and prv<arr[i]+arr[j]:
            left=i
            right=j
            prv=arr[i]+arr[j]
        #   if abs(arr[i] + arr[j] - x) < temp:  #Another option/way
        #     res_l = i 
        #     res_r = j 
        #     temp = abs(arr[i] + arr[j] - x)      
print(arr[left],arr[right]) # 22 30

#two pointer- T.c=O(n)
i=0
j=len(arr)-1
diff=float('inf')
while i<j:
    if abs(arr[i]+arr[j]-x)<diff:
        diff=abs(arr[i]+arr[j]-x)
        l=i
        r=j
    elif arr[i]+arr[j]<x:
        i+=1
    else:
        j-=1
print(arr[l],arr[r])