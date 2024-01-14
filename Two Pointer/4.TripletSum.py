#4.Given an array of distinct elements. The task is to find triplets in the array whose sum is zero.
# Examples : 
# Input: arr[] = {0, -1, 2, -3, 1}
# Output: (0 -1 1), (2 -3 1)
arr=[0, -1, 2, -3, 1]
found=False
#Brute Force- T.c=O(n^3)
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        for k in range(i+2,len(arr)):
            if arr[i]+arr[j]+arr[k]==0:
                print(arr[i],arr[j],arr[k])
                found=True
            
if found==False:
    print('not exist')

# Using set-T.c=O(n^2)
found=False
n=len(arr)
for i in range(n-1):
    s=set()
    for j in range(i+1,n):
        x=-(arr[i]+arr[j])
        if x in s:
            print(x,arr[i],arr[j])
            found=True
        else:
            s.add(arr[j])
    if found==False:
        print('No triplet Found')
#two pointer-T.c=O(n^2)
arr = [0, -1, 2, -3, 1]
n = len(arr)
found=False
arr.sort()
for i in range(n-1):
    l=i+1
    r=n-1
    x=arr[i]
    while l<r:
        if (x+arr[l]+arr[r]==0):
            print(x,arr[l],arr[r])
            l+=1
            r-=1
            found=True
        # If sum of three elements is less
        # than zero then increment in left
        elif (x+arr[l]+arr[r]<0):
            l+=1
        else:
            r-=1
    if found==False:
        print('No Triplet Found')