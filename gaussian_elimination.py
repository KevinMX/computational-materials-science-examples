import numpy as np

def gs_linsolve(a, b):
    ndim = a.shape[0]
    A = np.hstack((a, b.reshape((-1, 1))))
    for k in range(ndim-1):
        elMax = abs(A[k,k])
        idMax = k
        for i in range(k+1, ndim):
            if(abs(A[i, k]) > elMax):
                idMax = i
                elMax = abs(A[i,k])
        A[[k, idMax], :] = A[[idMax, k], :]
        for i in range(k+1, ndim):
            for j in range(k+1, ndim+1):
                A[i,j]=A[i,j]-A[i,k]/A[k,k]*A[k,j]
            A[i,k] = 0.
    x = np.zeros(ndim)
    for i in range(ndim-1, -1, -1):
        sum =0.
        for k in range(i+1, ndim):
            sum+=A[i,k]*x[k]
        x[i] = (A[i, ndim] - sum)/A[i,i]
    return x

a=np.array([[130,9,5,3,1.5,1],
    [10,110,8,5,2.1,2.5],
    [25,25,100,10,2.5,3],
    [4,6,15,150,23,8],
    [6,8,10,20,130,25],
    [8,10,12,10,25,105]])
b=np.array([0.185,0.2995,0.4455,0.8244,0.9320,0.8590])
print(gs_linsolve(a,b))

