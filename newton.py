import math
def diff(f,x):
  dx = 1e-10
  return (f(x+dx) - f(x))/dx
def newton(f, eps, x0):
  while(True): #while(True)==while(1)
    x = x0 - f(x0)/diff(f,x0)
    if (abs(f(x)))<eps:
      return x
    else:
      x0 = x
f = lambda x : math.log(x)
x = newton(f, eps=1.e-10, x0=0.6)
print(x)