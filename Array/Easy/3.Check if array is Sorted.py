#User function Template for python3
''' Brute Force:
    Using two loops take each element from the arr and check if any element right to the array is greater,if it is then return False after two loops return True
    Time Complexity of this approach is O(n^2)
    Space Complexity--O(1)'''

''' OPTIMAL SOLUTION'''
class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        for i in range(n-1):
            if arr[i]>arr[i+1]:
                return 0
        return 1
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
        ans = ob.arraySortedOrNot(arr, n)
        if ans:
            print(1)
        else:
            print(0)
        tc -= 1

# } Driver Code Ends
