import numpy as np

def lreg(x,y):
  n = x.size
  sx, sy, sxy, sxx, syy = 0., 0., 0.,0., 0.
  for i in range(n):
    sx += x[i]
    sy += y[i]
    sxy += x[i]*y[i]
    sxx += x[i]*x[i]
    syy += y[i]*y[i]
  lxx = sxx - sx*sx/n
  lxy = sxy - sx*sy/n
  lyy = syy - sy*sy/n
  b = lxy / lxx
  a = sy / n - b * sx / n
  r = lxy / np.sqrt(lxx * lyy)
  return a, b, r

d = np.array([400,50,10,5,2],dtype=float)
sigma_s = np.array([86,121,180,242,345],dtype=float)
d1 = d**(-0.5)
sigma_0, k, r= lreg(d1, sigma_s)
print(f'sigma_0={sigma_0}, k={k}')

