import numpy as np
import pylab as plt

### Part b
def myrk2(f,tspan,y0,N,params):
    t0,tN=tspan
    t=np.linspace(t0,tN,N+1)
    h=t[1]-t[0]
    y=np.zeros((*t.shape,*np.array(y0).shape))
    y[0]=y0
    for k in range(N):
        tk,yk=t[k],y[k]
        k1=h*f(tk,yk,params)
        k2=h*f(tk+h,yk+k1,params)
        y[k+1]=yk+(k1+k2)/2
    return t,y