#User function Template for python3
''' Brute Force:
Make the array having only unique elements using set and sort the array and return last second element of the array
Its Time Complexity--O(nlogn) and Space Complexity--O(1)'''
class Solution:

	def print2largest(self,arr, n):
		# code here
		max1,max2=-1,-1
		for i in range(n):
		    if arr[i]>max1:
		        max2=max1
		        max1=arr[i]
		    elif arr[i]<max1 and arr[i]>max2:
		        max2=arr[i]
		return max2
''' Time Complexity--O(n)
    Space Complexity--O(1)'''

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends
