import numpy as np
#The ones method creates an array of ones
ones = np.ones((3,4))
print(ones)

print()
#The zeros method creates an array of zeros
zeros = np.zeros((3,4))
print(zeros)

print()

#create an array with randoms values
random = np.random.random((2,2))
print(random)

print()

#Create an array empty with the method empty
emptyy = np.empty((3,2))
print(emptyy)

print()

#Create an array whit one value with the method full
full = np.full((2,3), 8)
print(full)

print()

#Create array with spaced values with the methods linspace and arange

#arange
spaced1 = np.arange(0, 35, 5)
print(spaced1)
#linspace
space2 = np.linspace(0, 2, 5)
print(space2 )

print()

#Create an array identity with mwthods eye or identity
 
#eye
identity1 = np.eye(4,4)
print(identity1)

print()
#identity
identity2 = np.identity(4)
print(identity2)

print()
#Know the dimension of the array with the method ndim
a = np.array([(1,2,3), (4,5,6)])
print(a.ndim)

print()

#Know the date type of the array whir method dtype
b = np.array([(1,2,3)])
print(b.dtype)

print()
 
#Know the size and shape of the array with methods size and shape
c = np.array([(1,2,3,4,5,6)])
print(c.size)
print(c.shape)

print()

#Change the shape of the array with the method reshape

d = np.array([(1,2,3,4), (5,6,7,8)])
print(d)
print("Change shape: ")
d = d.reshape(4,2)
print('  ',d)

print()
#Find minimum, maximum and sum of a array
e = np.array([2,3,4])
print('Operations: ')
#minimum
print('Min value: ',e.min())
#maximum
print('Max value: ',e.max())
#sum
print('Sum of the all values in the array: ',e.sum())

print()

#Calculate square root and standard deviation of the array with method sqrt and std
print('Calculeting squre root and standard deviation in the array: ')
f = np.array([(1,2,3), (4,5,6)])
print(f ,'\n')
print('squre root: ')
print(np.sqrt(f), '\n')
print('standard deviation: ')
print(np.std(f))
