import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scipy import interpolate
pd.set_option('display.max_column',10)

'''File get input table data (with index in) and returns the law of change (polynom)'''


def approximation_data(x_in,y_in,deg_polynom=5):

    #Table data
    # y_in = [1,10,50,160,800]
    # x_in = np.linspace(y_in[0], y_in[-1], len(y_in))
    # x_approx = np.linspace(y_in[0],y_in[-1],len(y_in)*100)

    x_approx = np.arange(x_in.iloc[0],x_in.iloc[-1],0.01)

    f = interpolate.interp1d(x_in, y_in,)
    y_1 = f(x_approx)

    z = np.polyfit(x_approx,y_1,deg_polynom)
    p = np.poly1d(z)
    y_approx = p(x_approx)

    print(f'\npolynom: \n{p}')

    sns.lineplot(x=x_approx,y=y_approx,color='blue',label=f'{p}')
    sns.scatterplot(x=x_in,y=y_in,color='orange',label='initial data')
    plt.xlabel('x')
    plt.ylabel('function (x)')
    plt.title('Approximation table data 60К 0deg')
    plt.tight_layout()
    plt.grid()
    plt.legend()
    plt.show()

    return p




# data = pd.read_csv('E:\\Library\\AMSC Amperium 2019\\AMSC Amperium® Type 8700 cable formulation 2G HTS 77.5 K Field Dependence.csv')
data = pd.read_csv('E:\\Current project\\Article new\\SuperOx_GdBCO.csv')

angle = 0
data = data[(data['Applied field (T)'] <= 4) & (data['Applied field angle (°)'] == angle)]

print(data)
print(data.columns)

# x_in = data[data['Applied field (T)']]
# y_in = data[data['Critical current (A)']]
# approximation_data(x_in,y_in,deg_polynom=5)

# for t in ['Temperature_20','Temperature_25','Temperature_45','Temperature_65','Temperature_77']:
#
#     x_in = data[data[t]]['Applied field (T)']
#     y_in = data[data[t]]['Critical current (A)']
#
#     approximation_data(x_in,y_in,deg_polynom=3)
# plt.show()