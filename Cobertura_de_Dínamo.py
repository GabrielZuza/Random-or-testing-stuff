import numpy as np
import matplotlib.pyplot as plt
from vpython import *
scene2 = canvas(width = 1800, height = 1000, center = vector(0.5,0.5,0) ,background=color.black)
RR =50
raio_esfera = 0.45
def enerxia(n_dinamo):
    return -n_dinamo

def normalizando(Matriz):
    for k in range(RR):
        for j in range(RR):
            if Matriz[k,j] != 0:
                Matriz[k,j] =1
    return Matriz
csphere = np.zeros((RR,RR),dtype=sphere)   
#tau_variacao = [1e4,1e5,1e6] 

for k in [1e4]:# use tau_variacao se quiser  
    A = np.zeros((RR,RR),dtype=int)
    quad_fora_da_area = 0
    Amp = 1e3
    Tmin = 1e-3
    tau = k
    t = 0
    T = 1
    w = 0
    n_dinamo = 0
    tlist,ylist=[],[]
    
    for f in range(RR):
        for j in range(RR):
            csphere[f,j] = sphere(pos=vector(f,j,0), radius=raio_esfera,color=color.white)
            
    while(T>Tmin):
        t+=1
        T = Amp*np.exp(-t/tau)
        x,y = int(np.random.randint(0,RR)),int(np.random.randint(0,RR))
        a = [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]
        xa,ya = a[np.random.randint(0,high=4)]
        if (xa<0 or xa>=RR or ya<0 or ya>=RR):
            quad_fora_da_area+=1
            t-=1
        else: 
            if(A[x,y]==0 and A[xa,ya]==0):
                w += 1
                A[x,y] = w
                A[xa,ya] = w
                n_dinamo +=1
                if x==xa:    
                    csphere[x,y],csphere[xa,ya] = sphere(pos=vector(x,y,0), radius=raio_esfera,color=color.red),sphere(pos=vector(xa,ya,0), radius=raio_esfera,color=color.red)
                else:
                    csphere[x,y],csphere[xa,ya] = sphere(pos=vector(x,y,0), radius=raio_esfera,color=color.blue),sphere(pos=vector(xa,ya,0), radius=raio_esfera,color=color.blue)
            elif(A[x,y]==A[xa,ya]):
                if (np.random.uniform()<np.exp(-1/T)):
                    A[x,y] = 0
                    A[xa,ya] = 0
                    n_dinamo -=1
                    csphere[x,y],csphere[xa,ya] = sphere(pos=vector(x,y,0), radius=raio_esfera,color=color.white),sphere(pos=vector(xa,ya,0), radius=raio_esfera,color=color.white)
                 
            if t%100:
                rate(30)
            tlist.append(t)
            ylist.append(enerxia(n_dinamo))

