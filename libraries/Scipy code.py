#Scipy

# from scipy import integrate
# import numpy as np
# def fun(x):
#     return (x**2) - (1/x) + (x**.5) - (np.sin(1/x))**5

# result,error = integrate.quad(fun,5,10)
# print(result)

import scipy
import numpy as np
'''
0 1 0
1 1 -1
0 -2 1
'''
'''
5
1 
3
'''

a = np.mat( [[0,1,0] , [1,1,-1] , [0,-2,1] ]  )
a = np.mat ("[0 1 0 ; 1 1 -1 ; 0 -2 1]")
b = np.mat([ [5],[1],[3]])
b= np.mat("[5 ; 1 ; 3]")
print((a.I * b ))



