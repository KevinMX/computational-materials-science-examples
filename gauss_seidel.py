import numpy as np
def gssd(a,b,x0,imax=10000,tol=1e-10):
    ndim=a.shape[0]
    x=x0.copy()
    for k in range(imax):
        xtemp=x.copy()
        for i in range(ndim):
            s=0.
            for j in range(0,ndim):
                if(j != i):
                    s+=a[i,j]*x[j]
            x[i]=(b[i]-s)/a[i,i]
        x_norm=np.linalg.norm(x-xtemp)
        if (x_norm<tol):
            print(k,tol)
            break
    return x

A = np.array([[130, 9, 5, 3, 1.5, 1],
              [10, 110, 8, 5, 2.1, 2.5],
              [25, 25, 100, 10, 2.5, 3],
              [4,6,15,150,23,8],
              [6,8,10,20,130,25],
              [8,10,12,10,25,105]])
b = np.array([0.185,0.2995,0.4455,0.8244,0.9320,0.859])
x0 = np.zeros(b.shape)
print(gssd(A,b,x0))
