import csv
import random

def Quadgen(P1,P2,P3,P4):
    tria_a = Triagen(P1,P2,P3)
    tria_b = Triagen(P3,P4,P1)
    with open("./Text1.csv",mode = 'w',newline='') as file:
        WriterObj = csv.writer(file)
        for i in range(1000):
            WriterObj.writerow(next(tria_a))
            WriterObj.writerow(next(tria_b))
            

def Triagen(P1,P2,P3):

    while(True):
        U = random.random()
        V = random.random()

        if(U+V < 1):
            alpha = 1 - U - V
            beta = U
            gamma = V

            X = alpha*P1[0] + beta*P2[0] + gamma*P3[0]
            Y = alpha*P1[1] + beta*P2[1] + gamma*P3[1]
            Z = alpha*P1[2] + beta*P2[2] + gamma*P3[2]

            yield X,Y,Z

Quadgen([0,0,0], [1,0,0], [1,1,0], [0,1,0])




