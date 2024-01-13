#1.Two sum
#Brute Force -T.c=O(n^2),S.c=O(1)
a=[1,2,3,4,5,6,7]
target=7
ans='No'
# for i in range(len(a)):
#     for j in range(i+1,len(a)):
#         if a[i]+a[j]==target:
#             ans='Yes'
#             break
# print(ans)
#Two pointer Approach-T.c=O(n)
# i=0
# j=len(a)-1
# while i<j:
#     if a[i]+a[j]==target:
#         ans='Yes'
#         break
#     elif a[i]+a[j]<target:
#         i+=1
#     else:
#         j-=2
# print(ans)

#2.Find the closest pair from two sorted arrays
a1=[1,4,5,7]
a2=[10,20,30,40]
x=32
# Brute force-T.c=O(n^2)
# ans=[]
# curr_max=0
# for i in range(len(a1)):
#     for j in range(len(a2)):
#         if a1[i]+a2[j]>curr_max and a1[i]+a2[j]<=x:
#             curr_max=a1[i]+a2[j]
#             ans=[a1[i],a2[j]]
# print(curr_max,ans)
#two pointer-T.c=O(n)
# m=len(a1)
# n=len(a2)
# l=0
# r=n-1
# diff=float('inf')
# while l<m and r>=0:
#     if abs(a1[l]+a2[r]-x)<diff:
#         res_l=l
#         res_r=r
#         diff=abs(a1[l]+a2[r]-x)
#     elif a1[l]+a2[r]<x:
#         l+=1
#     else:
#         r-=1
# print(a1[res_l],a2[res_r])#1,30

# 3.Given a sorted array and a number x, find a pair in an array whose sum is closest to x.
# Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
# Output: 22 and 30
arr=[10,22,28,29,30,40]
x=54
# Brute Force
# prv=0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         if arr[i]+arr[j]<=x and prv<arr[i]+arr[j]:
#             left=i
#             right=j
#             prv=arr[i]+arr[j]
#             # if abs(arr[i] + arr[j] - x) < temp: 
#             #     res_l = i 
#             #     res_r = j 
#             #     temp = abs(arr[i] + arr[j] - x) 
      
# print(arr[left],arr[right]) # 22 30
# #two pointer 
# i=0
# j=len(arr)-1
# diff=float('inf')
# while i<j:
#     if abs(arr[i]+arr[j]-x)<diff:
#         diff=abs(arr[i]+arr[j]-x)
#         l=i
#         r=j
#     elif arr[i]+arr[j]<x:
#         i+=1
#     else:
#         j-=1
# print(arr[l],arr[r])

#4.Given an array of distinct elements. The task is to find triplets in the array whose sum is zero.
# Examples : 
# Input: arr[] = {0, -1, 2, -3, 1}
# Output: (0 -1 1), (2 -3 1)
arr=[0, -1, 2, -3, 1]
found=False
#Brute Force- T.c=O(n^3)
# for i in range(len(arr)-1):
#     for j in range(i+1,len(arr)):
#         for k in range(i+2,len(arr)):
#             if arr[i]+arr[j]+arr[k]==0:
#                 print(arr[i],arr[j],arr[k])
#                 found=True
#             
# if found==False:
#     print('not exist')

#Using set-T.c=O(n^2)
# found=False
# n=len(arr)
# for i in range(n-1):
#     s=set()
#     for j in range(i+1,n):
#         x=-(arr[i]+arr[j])
#         if x in s:
#             print(x,arr[i],arr[j])
#             found=True
#         else:
#             s.add(arr[j])
#     if found==False:
#         print('No triplet Found')

#two pointer-T.c=O(n^2)
# arr = [0, -1, 2, -3, 1]
# n = len(arr)
# found=False
# arr.sort()
# for i in range(n-1):
#     l=i+1
#     r=n-1
#     x=arr[i]
#     while l<r:
#         if (x+arr[l]+arr[r]==0):
#             print(x,arr[l],arr[r])
#             l+=1
#             r-=1
#             found=True
#         # If sum of three elements is less
#         # than zero then increment in left
#         elif (x+arr[l]+arr[r]<0):
#             l+=1
#         else:
#             r-=1
#     if found==False:
#         print('No Triplet Found')


#5.3Sum
# Given an array arr[] of size n and an integer X. Find if there’s a triplet in the array which sums up to the given integer X.
# Input: array = {12, 3, 4, 1, 6, 9}, sum = 24; 
# Output: 12, 3, 9 
       







                
            
