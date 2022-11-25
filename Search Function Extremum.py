import numpy as np
import sympy as sp
from datetime import datetime
import time

#Расчет времени
start_time=datetime.now()

x=sp.Symbol('x')

#исследуемая функция
f1=x**3-25*x+10
   
#производная f1
d_f1=sp.diff(f1)

#проверка на диф-ть ф-ии
dd_f1=sp.diff(f1)

if dd_f1 !=0:
    print("\n")
    print('Можно поисследовать')
else:
    print('Выбери другую функцию')

#функция,которая подставляет в производную значение a
def d_fun(a):
    y=d_f1.subs(x,a)
    return(y)

Eps=0.5
N=1000#Количество приращений X
X=np.linspace(-10,10,N+1)#Область поиска
A=np.array([])

for i in range(N):
    Y=d_fun(X[i])
    if abs(Y)<Eps:
        A=np.append(A,X[i])      
print('Экстремумы расположены:','x=',A)
        
end_time=datetime.now()-start_time
print("\n",'Solving Time',end_time)
        
    
