def remDuplicate(A):
    n=len(A)
    if (n==0 or n==1) :
        return n
    else:
        j=0
        i=0
        for x in A:
            if(x!=A[j]):
                j=j+1
                A[j]=x
                # i=i+1
        
        del A[j+1:n]

        return A,j+1

print(remDuplicate([1,1,2,2,3,4]))
print(remDuplicate([ 1, 1, 2, 2, 3,4,4 ]))
print(remDuplicate([ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ]))