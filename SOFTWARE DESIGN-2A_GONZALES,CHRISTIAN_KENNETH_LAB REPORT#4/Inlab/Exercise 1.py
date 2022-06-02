from re import M


def product( m , n ):
  
    if m < n:
        return product(n, m)
   
    elif n != 0:
        return (m + product(m, n - 1))
     

    else:
        return 0

m = int(input("The first value:"))
n = int(input("The second number:"))
print( product(m, n))