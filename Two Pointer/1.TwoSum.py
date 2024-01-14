#1.Two sum
#Brute Force -T.c=O(n^2),S.c=O(1)
a=[1,2,3,4,5,6,7]
target=7
ans='No'
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==target:
            ans='Yes'
            break
print(ans)
#Two pointer Approach-T.c=O(n)
i=0
j=len(a)-1
while i<j:
    if a[i]+a[j]==target:
        ans='Yes'
        break
    elif a[i]+a[j]<target:
        i+=1
    else:
        j-=2
print(ans)
















                
            
