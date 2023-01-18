import numpy as np

## Metodo de Euler para un PVI
def euler(f,x0,t):
    # import numpy as np
    # INPUT:
    #     f: y' = f(t,y)
    #    x0: y(t0) = y0
    #     t: rango de tiempo
    # OUTPU:
    
    x = np.zeros(len(t))
    
    x[0] = x0
    
    xs = [[t[0],x[0]]]
    for n in range(len(t)-1):  
        x[n+1] = x[n] + f(x[n],t[n])*(t[n+1] - t[n])
        
        xs.append([t[n+1],x[n+1]])
        
    return np.round(np.array(xs),4)

# Metodo de Euler para un sistema de dos ecuaciones diferenciales
# Con condiciones iniciales
def euler2(f1, f2, y0, x0, t):
    y = np.zeros(len(t))
    x = np.zeros(len(t))
    
    y[0] = y0
    x[0] = x0
    
    yx = [[y[0],x[0]]]
    for n in range(0,len(t)-1):
        y[n+1] = y[n] + f1(y[n],x[n],t[n])*(t[n+1] - t[n])
        x[n+1] = x[n] + f2(y[n],x[n],t[n])*(t[n+1] - t[n])
        yx.append([y[n+1],x[n+1]])
    return np.round(np.array(yx),4)


def euler3(f1, f2, f3):
    pass


def rungekutta(f1, f2, y0, x0, t):
    N = len(t)
    h = (t[-1] - t[0])/N
    
    y = np.zeros(N)
    x = np.zeros(N)

    y[0] = y0
    x[0] = x0
    yx = [[y[0],x[0]]]

    for n in range(N-1):
        ky1 = f1(y[n],x[n],t[n])
        kx1 = f2(y[n],x[n],t[n])

        ky2 = f1(y[n] + 0.5*ky1*h,x[n] + 0.5*kx1*h,t[n] + 0.5*h)
        kx2 = f2(y[n] + 0.5*ky1*h,x[n] + 0.5*kx1*h,t[n] + 0.5*h)

        ky3 = f1(y[n] + 0.5*ky2*h,x[n] + 0.5*kx2*h,t[n] + 0.5*h)
        kx3 = f2(y[n] + 0.5*ky2*h,x[n] + 0.5*kx2*h,t[n] + 0.5*h)

        ky4 = f1(y[n] + ky3*h,x[n] + kx3*h,t[n] + h)
        kx4 = f2(y[n] + ky3*h,x[n] + kx3*h,t[n] + h)

        y[n+1] = y[n] + (h/6)*(ky1 + 2*ky2 + 2*ky3 + ky4)
        x[n+1] = x[n] + (h/6)*(kx1 + 2*kx2 + 2*kx3 + kx4)

#        t[n+1] = t[n] + h

        yx.append([y[n+1],x[n+1]])
    
    return np.round(np.array(yx),4)

