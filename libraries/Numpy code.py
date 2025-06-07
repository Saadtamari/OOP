#Numpy

#import numpy 
#from numpy import *
import numpy as np

### List vs Array
l = [1,2,3,4,5]
arr = np.array([1,2,3,4,5])
#print(arr,arr)
#print(arr+arr)

### type, dtype, shape , sum, max ,min ,mean ,std 
arr = np.array([[1,2,3,4,5],[2,5,10,3,8],[4,5,2,9,7]])
#print(arr)
# print(type(arr))
# print(arr.dtype)
# print(arr.shape) # (... , ....)
# print(arr.size)

### Index & Sclicing --> 2
#s= "Hello World"
# print(s[-1])
# print(arr[1])

# print(  s[-1::-1]   )
# print(arr[-1::-1])

print()
#print(arr[1 , 2])
#arr[:2 , 1:4 ] = 1
#print( arr)
#arr[0] = [5,10,2,4,7]
#print(arr)
#print( arr [ 0 , :4])



### linspace(start,end,size=50)       arange(start,end,jump)

#print(np.linspace(1,50,2)) # Jump = end-start / size -1

#print(np.arange(10,1,-2)) #range()
#print(np.arange(0,100,5))

### reshape()


# arr = np.linspace(1,12,12)
# print(arr)
# print()
# print(arr.reshape(4,3)) 


### sort -- > np.sort(arrName) , arrName.sort()

# arr = np.array([[10,2,-1,4,5],[2,5,10,3,8],[4,5,2,9,7]])
# print(arr)
# print()
# print(np.sort(arr))#,axis=0))
# print(arr)
# print(arr.sort())
# print()
# # arr.sort()
# print(arr) 


### Array vs Matrix

arr1 = np.array([2,3,4])
arr2 = np.array([2,2,2])
print(arr1*arr2)
#print(arr1.shape) #(3,)


mat1 = np.mat([2,3,4])
mat2 = np.mat([[2,2],[1,3],[1,2]])
# (1,3) * (3,2) -- > (1,2)
print(mat1*mat2) 

