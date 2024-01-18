#5. An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

# Examples : 

# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5
arr=[-12, 11, -13, -5, 6, -7, 5, -3, -6]

#1. sort method- T.c=O(nlogn)
arr.sort()
print(*arr)
#2.using loop-T.c=O(n)
arr=[-12, 11, -13, -5, 6, -7, 5, -3, -6]
j=0
for i in range(len(arr)):
    if arr[i]<0 :
        arr[j],arr[i]=arr[i],arr[j]
        j+=1
print(arr)
#3.Using two pointer-T.c=O(n)
arr=[-12, 11, -13, -5,6, -7, 5, -3, 11] 
left=0
right=len(arr)-1
while left<right:
    if arr[left]<0 and arr[right]<0:
        left+=1
    
    elif arr[left]>0 and arr[right]<0:
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
    elif arr[left]>0 and arr[right]>0:
        right-=1
    else:#if right had positive element
        left+=1
        right-=1
print(arr)
    