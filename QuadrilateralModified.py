import csv
import random


def index(a,b,P1,P2,P3,P4):
    index1 = a
    index2 = b
    Points =[]
    if(index1 == 0 or index2 == 0):
        Points.append(P1)
        Points.append(P2)
        Points.append(P3)
    if(index1 == 1 or index2 == 1):
        Points.append(P1)
        Points.append(P2)
        Points.append(P4)
    if(index1 == 2 or index2 == 2):
        Points.append(P1)
        Points.append(P3)
        Points.append(P4)
    if(index1 == 3 or index2 == 3):
        Points.append(P2)
        Points.append(P3)
        Points.append(P4)
    return Points


def ComputeAreaofQuad(P1,P2,P3,P4):
    Area = 0.5*((P1[0]*P2[1] + P2[0]*P3[1] + P3[0]*P4[1] + P4[0]*P1[1]) - (P1[1]*P2[0] + P2[1]*P3[0]+P3[1]*P4[0] +P4[1]*P1[0]))
    return abs(Area)


def Areaoftriangle(P1,P2,P3):
    x1,y1,z1 = P1
    x2,y2,z2 = P2
    x3,y3,z3 = P3
    Area = 0.5*(x1*(y2-y3) + x2*(y3 - y1) + x3*(y1 - y2))
    return Area


def ComputeAreaofTriangle(Area, P1,P2,P3,P4):
    Points = []
    AreaofTriangle123 = Areaoftriangle(P1,P2,P3)
    AreaofTriangle124 = Areaoftriangle(P1,P2,P4)
    AreaofTriangle134 = Areaoftriangle(P1,P3,P4)
    AreaofTriangle234 = Areaoftriangle(P2,P3,P4)

    List = [AreaofTriangle123,AreaofTriangle124,AreaofTriangle134,AreaofTriangle234]
    for i in range(len(List)):
        for j in range(i+1,len(List)):
            if(List[i] == List[j]):
                a = i
                b = j
    if(List[a] + List[b] == Area):
        Points = index(a,b,P1,P2,P3,P4)
        #print(Points)
        return Points

def Quadgen(P1,P2,P3,P4):

    Area = ComputeAreaofQuad(P1,P2,P3,P4)
    print("Area:",Area)
    
    Points=ComputeAreaofTriangle(Area, P1,P2,P3,P4)
    
    tria_a = Triagen(Points[0],Points[1],Points[2])
    tria_b = Triagen(Points[3],Points[4],Points[5])
    
    while(True):
        yield next(tria_a)
        yield next(tria_b)

            
def Triagen(P1,P2,P3):

    while(True):
        U = random.random()
        V = random.random()

        if(U+V > 1):
            U = 1- U    
            V = 1- V

        alpha = 1 - U - V
        beta = U
        gamma = V

        X = alpha*P1[0] + beta*P2[0] + gamma*P3[0]
        Y = alpha*P1[1] + beta*P2[1] + gamma*P3[1]
        Z = alpha*P1[2] + beta*P2[2] + gamma*P3[2]

        yield X,Y,Z

QuadgenObj = Quadgen([0,-1,0], [1,1,0], [-1,0,0], [0,0,0])  
with open("./Quad1.csv",mode = 'w',newline='') as file:
    WriterObj = csv.writer(file)
    for i in range(10000):
        WriterObj.writerow(next(QuadgenObj))




