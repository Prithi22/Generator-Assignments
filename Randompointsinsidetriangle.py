
import random

def Triagen(P1, P2, P3):

    # u v values
    u = random.random()
    v = random.random()

    if(u+v > 1):
        u = 1 - u
        v = 1- v
    
    alpha = 1 - (u - v)
    beta = u
    gamma = v

    if(alpha , beta , gamma >=0):
        X = alpha*P1[0] + beta*P1[1] + gamma*P1[2]
        Y = alpha*P2[0] + beta*P2[1] + gamma*P2[2]
        Z = alpha*P3[0] + beta*P3[1] + gamma*P3[2]
    yield X,Y,Z

import random

def Triagen(P1, P2, P3):

    # u v values
    u = random.random()
    v = random.random()

    if(u+v > 1):
        u = 1 - u
        v = 1- v
    
    alpha = 1 - (u - v)
    beta = u
    gamma = v

    if(alpha , beta , gamma >=0):
        X = alpha*P1[0] + beta*P1[1] + gamma*P1[2]
        Y = alpha*P2[0] + beta*P2[1] + gamma*P2[2]
        Z = alpha*P3[0] + beta*P3[1] + gamma*P3[2]
    yield X,Y,Z

a_tria = Triagen([0,0,0], [1,0,0], [1,1,0])
b_tria = Triagen([0,0,0], [0,1,0], [-1,0,0])

#print(next(a_tria))
#print(next(b_tria))

# Loop that never gets exhausted
while(1):
    for i in Triagen((1,0,0),(0,1,0),(0,0,0)):
        print(i)