#2.Find the closest pair from two sorted arrays
a1=[1,4,5,7]
a2=[10,20,30,40]
x=32
# Brute force-T.c=O(n^2)
ans=[]
curr_max=0
for i in range(len(a1)):
    for j in range(len(a2)):
        if a1[i]+a2[j]>curr_max and a1[i]+a2[j]<=x:
            curr_max=a1[i]+a2[j]
            ans=[a1[i],a2[j]]
print(curr_max,ans)
#two pointer-T.c=O(n)
m=len(a1)
n=len(a2)
l=0
r=n-1
diff=float('inf')
while l<m and r>=0:
    if abs(a1[l]+a2[r]-x)<diff:
        res_l=l
        res_r=r
        diff=abs(a1[l]+a2[r]-x)
    elif a1[l]+a2[r]<x:
        l+=1
    else:
        r-=1
print(a1[res_l],a2[res_r])#1,30
