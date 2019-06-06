import numpy, sys, time
import matplotlib.pyplot as plt

def Product(N):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                c[i, j] += a[i,k]*b[k,j]

def Initialize(N):

    for i in range(N):
        for j in range(N):
            a[i, j] = i * N + j
            b[i, j] = j * N + i
            c[i, j] = 0



Num = int(input())
timelist = []

for n in range(Num):
    a = numpy.zeros((n, n)) # Matrix A
    b = numpy.zeros((n, n)) # Matrix B
    c = numpy.zeros((n, n)) # Matrix C


    # Initialize the matrices to some values.
    Initialize(n)

    begin = time.time()

    ######################################################
    Product(n)
    ######################################################

    end = time.time()
    if n == 0:
        timelist.append(end-end)
    else:
        timelist.append(end-begin)
        print("time: %.6f sec" % (end - begin))



# Print C for debugging. Comment out the print before measuring the execution time.
#total = 0
# for i in range(n):
    # for j in range(n):
        # print(c[i, j])
        # total += c[i, j]
# Print out the sum of all values in C.
# This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
#print("sum: %.6f" % total)
print(timelist)
x = numpy.arange(0, Num, 1)
# 計算式
y = 0.00000071*(x**3)
plt.plot(x, y)
plt.plot(list(range(len(timelist))), timelist, linestyle="dotted")
#plt.plot(x, y)
plt.show()