import library
import matplotlib.pyplot as plt


P,a = [1,0,0,1,0,0,-1],1
image = library.newton_fractal(P, a)
plt.imshow(image)