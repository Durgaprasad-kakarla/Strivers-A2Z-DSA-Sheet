#User function Template for python3

def largest( arr, n):
    max1=0
    for i in arr:
        if max1<i:
            max1=i
    return max1
''' Time Complexity--O(n)
    Space Complexity--O(1)'''


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(largest(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends
