def verifySorted(A):
    for i in range(len(A)-1):
        if A[i] > A[i+1]:
            print(f"A[{i}]=={A[i]} is greater than A[{i+1}]=={A[i+1]}")
            return
    print("Array is sorted!")


# Input:
#  array A from which to find a pivot
# Return:
#  value of the pivot
def pickPivot(A):
    return(A[-1]) # always use the last value of the array A


# Input:
#   A is the array to be partitioned
#   pivotvalue is the value around which to pivot (assumes at least one element
#     has value not less than pivotvalue)
# Return:
#   returns an index in A
#   A has been reordered such that every element below the index is less than
#      the pivotvalue, every element above the index is not less than the
#      pivotvalue, and there are no elements in A that are less than the element
#      at the index that are not less than the pivotvalue
def partitionInPlace(A,pivotvalue):
    #Storage
    left = []
    right = []
    #Go through loop and move items less than (or equal to) the pivot to the left, and items greater than the pivot to the right
    for x in A:
        if x <= pivotvalue:
            left.append(x)
        else:
            right.append(x)
    
    #Rejoin the left and the right
    A[:] = list(left + right)
    #return where the pivot is in the list (always at the end of left since the pivot is the last item in the array)
    return len(left)-1


# Input:
#   an array A to be sorted
# Returns:
#   A has been sorted
def quicksort(A):
    # manual sort for small arrays
    if len(A) < 3:
        if len(A) == 2:
            if A[0] > A[1]:
                A[0], A[1] = A[1], A[0]
        return
    # set up recursions
    pivotvalue = pickPivot(A)
    partitionindex = partitionInPlace(A,pivotvalue)
    quicksort(A[:partitionindex])
    quicksort(A[partitionindex+1:])






### Driver
def main():
    # create
    import numpy.random
    numpy.random.seed(0)
    A = numpy.random.randint(0,100,100)

    #Smaller test stuff for debugging
    #import numpy as np
    #B = np.array([5,2,1,4,3,7,6])

    # sort
    quicksort(A)

    # verify
    print(A)
    verifySorted(A)
    

if __name__ == "__main__":
    main()
