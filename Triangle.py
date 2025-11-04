import random
import csv
def Triagen(P1, P2, P3):

    while(True):
    # u v values
        u = random.random()
        v = random.random()

        if(u+v > 1):
            u = 1 - u
            v = 1- v
    
        alpha = 1 - (u - v)
        beta = u
        gamma = v
        X = alpha*P1[0] + beta*P2[0] + gamma*P3[0]
        Y = alpha*P1[1] + beta*P2[1] + gamma*P3[1]
        Z = alpha*P1[2] + beta*P2[2] + gamma*P3[2]
            
        yield X,Y,Z

a_tria = Triagen([0,0,0], [1,0,0], [1,1,0])
b_tria = Triagen([0,0,0], [0,1,0], [-1,0,0])
with open("./Triangle1.csv",mode = 'w',newline='') as File:
    WriterObj = csv.writer(File)
    for i in range(10000):
        WriterObj.writerow(next(a_tria))
        WriterObj.writerow(next(b_tria))
        
