import numpy as np
def interp_lin(x,y,x0):          #linear interpolation
    n=x.size
    for i in range(n-1):
        i1 = i + 1
        if (x0 >= x[i1]): break
    y0 = y[i] + (y[i1] - y[i]) / (x[i1] - x[i]) * (x0 - x[i])
    return y0

def interp_lag(x, y, x0):       #lagrange interpolation
    n = x.size
    v = 0.
    for k in range(n):
        p = 1.
        for i in range(n):
            if (i != k):
                p *= (x0 - x[i]) / (x[k] - x[i])
        v += p*y[k]
    return v

d = np.array([400,50,10,5,2],dtype=float)   #must be float
sigma_s = np.array([86,121,180,242,345],dtype=float)    #must be float

x = [200., 30.]

print([interp_lin(d, sigma_s, xi) for xi in x])
print([interp_lag(d, sigma_s, xi) for xi in x])