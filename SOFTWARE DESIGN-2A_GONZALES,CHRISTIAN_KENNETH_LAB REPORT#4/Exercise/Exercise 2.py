def MinRec(val, n):
     
    # if size = 0 means whole array
    # has been traversed
    if (n == 1):
        return val[0]
    return min(val[n - 1], MinRec(val, n - 1))
 
# Driver Code
if __name__ == '__main__':
    val = [1, 4, 45, 6, -50, 10, 2]
    n = len(val)
    print(MinRec(val, n))

def MaxRec(val, n):
 
    # if n = 0 means whole array
    # has been traversed
    if (n == 1):
        return val[0]
    return max(val[n - 1], MaxRec(val, n - 1))
 
# Driver Code
if __name__ == "__main__":
     
    val = [1, 4, 45, 6, -50, 10, 2]
    n = len(val)
    print(MaxRec(val, n))

