import numpy as np

def newton_fractal(p,a):
    """Out: a matrix that is actually an image of the Newton fractal starting from the polynomial p."""
    N,itermax,tol,epsilon = 700,100,1e-5,1e-16
    P = np.poly1d(p)
    dP = P.deriv()
    racines = P.roots
    t = np.linspace(-a,a,N)
    x,y = np.meshgrid(t,t,sparse=False,indexing='xy')
    table = np.zeros(x.shape)
    z0 = x + 1j *y + epsilon
    iter = 0
    #Newton
    z = z0
    while iter <= itermax:
        z = z-P(z)/dP(z)
        iter += 1
        
    k = 0
    for r in racines:
        indx = np.nonzero(abs(z-r) < tol)
        table[indx] = k+1
        k += 1
    return table
