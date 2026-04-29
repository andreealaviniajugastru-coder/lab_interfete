import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
print(a)
print(type(a))
print(a.dtype)
print(a.shape)
print(a[0])

b = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(b.shape)
print(b[0][2])
print(b[0,2])

c = np.array([[1,2],[13,14]])
print(type(c))
print(c.shape)

zero_array = np.array((3,2))
print(zero_array)

ones_array = np.ones((2,2))
print(ones_array)

constant_array = np. full((2,2),6)
print(constant_array)

identity_matrix = np.eye(4)
print(identity_matrix)

random_array = np.random.random((2,3))
print(random_array)
mu, sigma = 0, 0.1
gauss = np.random.normal(mu,sigma,(4,7))

first_7 = np.arange(7)
print(first_7)

array_to_slice = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
slice = array_to_slice[:,0:3]
print(slice)

print(array_to_slice[0][0])
slice[0][0] = 100
print(array_to_slice[0][0])

x = np.array([[1,2],[3,4]],dtype=np.float64)
y = np.array([[5,6],[7,8]],dtype=np.float64)

print(x+y)
print(np.subtract(x,y))

print(x-y)
print(np.multiply(x,y))

print(x/y)
print(np.divide(x,y))

print (np.sqrt(x))

my_array = np.arange(7)
powered = np.power(my_array,4)
print(powered)


