import numpy as np
#array of 10 zeros 
np.zeros(10)
#an array of 10 ones
np.ones(10)
#an array of 10 fives
np.ones(10) * 5
#array of the integers from 10 to 50
np.arange(10, 51)
#array of all the even integers from 10 to 50
np.arange(10,50,2)
#matrix 3x3 with values 0 to 8
arr=np.arange(0,9)
arr.reshape(3,3)
#np.arrange(9).reshape(3,3)
#identiity matrix
np.eye(3)
#random number b/w 0 and 1
np.random.rand(1)
#standard normal deviation - array of 25 random numbers
np.random.randn(25)
#matrix creation
np.arange(1,101).reshape(10, 10)/100
#Array of 20 linearly spaced points b/w 0 and 1
np.linspace(0,1,20)

#Numpy Indexing and selection
mat = np.arange(1,26).reshape(5,5)
mat[2:, 1:]
mat[3, 4]
mat[0:3, 1:2]
mat[4:]
mat[3:, :5]
#Sum of values in mat
mat.sum()
#Standard deviation
mat.std()
#Sum of rows
mat.sum(axis=1)