import numpy as np

A = np.array([[4,-1,2,3],[0,-2,7,-4],[0,0,6,5],[0,0,0,3]])
B = np.array([20,-7,4,6])
X = np.array([1,1,1,1])
n = 3
X[n] = B[n]/A[n,n]

for k in reversed(range(3)):
    sigma = 0
    for j in range(k+1,n+1):
        sigma = sigma + (A[k,j] * X[j])
        #print(sigma)
    X[k] = (B[k] - sigma)/A[k,k]

print("Maka Keseluruhan Titiknya adalah : ")

for i in range (0,4):
    print(X[i])