import matplotlib.pyplot as plt
import numpy as np

'''Method Euler'''

Y,T,E = [],[],[]
t,y = 0,0
t2 = 5
tn = 50

t_analytic = np.linspace(0,t2,tn)
function_an = 3*t_analytic**3+t_analytic**2
delta_t = 1e-5

def function(x):
    return 3*x**3+x**2

while t <= t2:
    y = y + delta_t * function(t)
    error = abs(function(t) - y)

    Y.append(y),T.append(t),E.append(error)

    t +=delta_t


plt.plot(t_analytic,function_an,label='analytical')
plt.plot(T,Y,label='numerical')
plt.plot(T,E,label='error')
plt.grid()
plt.legend()
plt.show()