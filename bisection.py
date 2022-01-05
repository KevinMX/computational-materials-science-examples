import math

def ln(x):
    a=math.log(x)
    return a

def bi(f,e,x1,x2):
    while(True):
        xm=(x1+x2)/2
        fm=f(xm)
        f1=f(x1)
        if abs(fm)<e:
            x=xm
            return x
        elif(fm*f1>0):
            x1=xm
        else:
            x2=xm

f=lambda x:ln(x)
x=bi(f,1e-4,0.0001,10.)
print(x)