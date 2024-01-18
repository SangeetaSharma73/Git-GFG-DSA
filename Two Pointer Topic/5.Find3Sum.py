#5.3Sum
# Given an array arr[] of size n and an integer X. Find if there’s a triplet in the array which sums up to the given integer X.
# Input: array = {12, 3, 4, 1, 6, 9}, sum = 24; 
# Output: 12, 3, 9 
arr=[12, 3, 4, 1, 6, 9]
Sum=24
#Brute Force Approach-O(n^3)
def Find3Numbers(arr,sum):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(i+2,len(arr)):
                if arr[i]+arr[j]+arr[k]==Sum:
                    print('Triplet is',arr[i],arr[j],arr[k])
                    return True
    return False
Find3Numbers(arr,Sum)

#two pointer-O(n^2)
def find3Numbers(arr,n,sum):
    arr.sort()
    for i in range(0,n-2):
        l=i+1
        r=n-1
        while l<r:
            if arr[i]+arr[l]+arr[r]==sum:
                print('Triplet is',arr[i],arr[l],arr[r])
                return True
            elif arr[i]+arr[l]+arr[r]<sum:
                l+=1
            else:
                r-=1
    return False
find3Numbers(arr,len(arr),Sum)

#Using set=>T.C-O(n^2)
def find3Numbers(arr, sum):
    # Fix the first element as arr[i]
    for i in range(len(arr) - 2):
        # Create a set to store potential second elements that complement the desired sum
        s = set() 
        # Calculate the current sum needed to reach the target sum
        curr_sum = sum - arr[i] 
        # Iterate through the subarray arr[i+1:]
        for j in range(i + 1, len(arr)): 
            # Calculate the required value for the second element
            required_value = curr_sum - arr[j]
            # Check if the required value is present in the set
            if required_value in s: 
                # Triplet is found; print the triplet elements
                print(f"Triplet is {arr[i]}, {arr[j]}, {required_value}")
                return True 
            # Add the current element to the set for future complement checks
            s.add(arr[j]) 
    # If no triplet is found, return False
    return False 
# Driver program to test above function
if __name__ == "__main__":
    arr = [1, 4, 45, 6, 10, 8]
    target_sum = 22
    # Call the find3Numbers function to find and print the triplet, if it exists
    if not find3Numbers(arr, target_sum):
        print("No triplet found.")
    