# Given an array (or string), the task is to reverse the array/string.
# Examples : 
# Input  : arr[] = {1, 2, 3}
# Output : arr[] = {3, 2, 1}

# Input :  arr[] = {4, 5, 1, 2}
# Output : arr[] = {2, 1, 5, 4}

#using two pointer- T.c=O(N) and S.c=O(1)
arr=[4, 5, 1, 2]
i=0
j=len(arr)-1
while i<j:
    arr[i],arr[j]=arr[j],arr[i]
    i+=1
    j-=1
print(arr)

# #using slicing- T.c=O(n)
print(arr[::-1])

#using Recursion- T.c=O(n) & S.c=O(n)
def reverse(arr,start,end):
    if start>=end:
        return 
    arr[start],arr[end]=arr[end],arr[start]
    reverse(arr,start+1,end-1)
reverse(arr,0,len(arr)-1)
print(arr)

#another way writing code of recursion 
def reverse(arr,start,end):
    if start>=end:
        return arr
    arr[start],arr[end]=arr[end],arr[start]
    return reverse(arr,start+1,end-1)
ans=reverse(arr,0,len(arr)-1)
print(ans)
        