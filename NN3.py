# expanded 3-layer (1 hidden layer) neural network from
# https://iamtrask.github.io/2015/07/12/basic-python-network/

import numpy as np
import matplotlib.pyplot as plt

# sigmoid function
def nonlin(x,deriv=False):
        if(deriv==True):
            return x*(1-x)
        return 1/(1+np.exp(-x))

# input data
X = np.array([[1,1,1],[1,2,1],[2,2,1],[2,3,1],[2,1,1],[3,2,1],[4,1,1],[4,2,1]])
y = np.array([[0],[0],[0],[0],[1],[1],[1],[1]])                
# output data
newX=np.array([[3,3,1],[4,3,1]])
# seed random numbers to make calculation deterministic (a good practice)


# randomly initialize the weights with mean 0
syn0 =[[-2.10462558 , 4.30662071 ,-3.49765842, -1.22765778],
 [ 1.95300663 ,-4.46559351,  3.45493791 , 0.59325871],
 [ 0.82067225, -1.61242069 , 1.50078947 , 0.69334666]]

syn1 = [[-3.16918025],
 [ 8.28419202],
 [-5.79735796],
 [-1.50022836]]


# run multiple epochs, where epoch = one forward pass and one backward 
# pass of all the training examples.
for j in range(60000):

    # Feed forward through layers 0, 1, and 2
    l0 = newX    # input
    l1 = nonlin(np.dot(l0,syn0))
    l2 = nonlin(np.dot(l1,syn1))

    # # how much did we miss the target value?
    # l2_error = y - l2
    
    # if (j% 10000) == 0:
    #     print ("epoch "+ str(j) + " Error: " + str(np.mean(np.abs(l2_error))))

    # # in what direction is the target value?
    # # were we really sure? if so, don't change too much.
    # l2_delta = l2_error*nonlin(l2,deriv=True)

    # # how much did each l1 value contribute to the l2 error (according to the weights)?
    # l1_error = l2_delta.dot(syn1.T)
    
    # # in what direction is the target l1?
    # # were we really sure? if so, don't change too much.
    # l1_delta = l1_error * nonlin(l1,deriv=True)

    # syn1 += l1.T.dot(l2_delta)
    # syn0 += l0.T.dot(l1_delta)

print("Output After Training: ")
# print(syn0)
# print(syn1)
print(l2)

# weight = syn1
# user_input_one = str(input("User Input One: "))
# user_input_two = str(input("User Input Two: "))
# user_input_three = str(input("User Input Three: "))
    
# print("Considering New Situation: ", user_input_one, user_input_two, user_input_three)
# print("New Output data: ")
# xnew = np.array([user_input_one, user_input_two, user_input_three])
# xnew = xnew.astype(float)

# l2new = nonlin(np.dot(xnew,weight))
# print(l2new)
# print("End")