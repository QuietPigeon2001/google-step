import numpy, sys, time

if (len(sys.argv) != 2):
    print("usage: python %s N" % sys.argv[0])
    quit()

n = int(sys.argv[1])
a = numpy.zeros((n, n)) # Matrix A
b = numpy.zeros((n, n)) # Matrix B
c = numpy.zeros((n, n)) # Matrix C

# Initialize the matrices to some values.
for i in range(n):
    for j in range(n):
        a[i, j] = i * n + j
        b[i, j] = j * n + i
        c[i, j] = 0

begin = time.time()

######################################################
# Write code to calculate C = A * B                  #
# (without using numpy librarlies e.g., numpy.dot()) #

def rowColSum(matrix1, matrix2, row, col):
    """
    Adds the elements in respective rows and columns
    :type matrix1, matrix2: n-d matrix
    :type row, col: int
    :rtype: int
    """
    res = 0
    for i in range(n):
        res += matrix1[row, i] * matrix2[i, col]
    return res

def dotProd(a,b,c):
    """
    Returns the dot product of matrices a and b
    :type a, b: n-d matrix
    :rtype: n-d matrix
    """
    for i in range(n):
        for j in range(n):
            c[i, j] = rowColSum(a, b, i, j)
    return c
print(c[i])

# Assigns new value to C 
c = dotProd(a,b,c)

######################################################

end = time.time()
print("time: %.6f sec" % (end - begin))

# Print C for debugging. Comment out the print before measuring the execution time.
total = 0
for i in range(n):
    for j in range(n):
        # print c[i, j]
        total += c[i, j]
# Print out the sum of all values in C.
# This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
print("sum: %.6f" % total)
