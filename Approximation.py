import matplotlib.pyplot as plt
import numpy as np

'''File get input table data (with index in) and returns the law of change (polynom)'''

#Table data
y_in = [1,10,50,160,800]
x_in = np.linspace(y_in[0], y_in[-1], len(y_in))
deg_polynom = 3
z = np.polyfit(x_in,y_in,deg_polynom)
p = np.poly1d(z)
y_out = p(x_in)

print(f'\npolynom: {p}')
plt.plot(x_in,y_out,color='blue',label='polinom')
plt.scatter(x_in,y_in,color='orange',label='initial data')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Approximation table data')
plt.grid()
plt.legend()
plt.show()
