#######Juego para David
#### Byme
#Julio 2021
import random


#0.Generar un vector de palabras
Palabras=["casa","gato", "sal","perro","celular","lapiz","día","eslpalda","cabeza","salida","amor"]

#1.Generar un numero aleatorio
index=random.randint(0,len(Palabras)-1)

#2.Establecer una palabra
p=Palabras[index]
#print(p)
print ("la palabra tiene " + str(len(p)) +" letras")
#2.2 Mostrar los espacios y convertirlos en una lista recorrible
r=("_ "*len(p))
print(r)
rayas=list(r)
#2.3 Determinar las vidas
vidas=4
pf=[]

#3.Mientras hallan vidas preguntar una letra
while pf!=p:
    logro=0
    letra=input("escoge una letra ")
    #4.Recorrer la palabra letra por letra
    for i in range(len(p)):
        #5.Si la letra esta logro=1
        if letra==p[i]:
            print("letra encontrada en la posición", i)
            logro=1
            rayas[i+i]=letra
            print(rayas)
            for i in range(len(rayas)):#arreglar cuando la letra esta duplicada
                if i%2==0:
                    pf.append(rayas[i])
                    
            
            vidas=vidas
                    
        else:
            pf=[]
            
            
    if logro==0:
        vidas=vidas-1
        print(vidas)
        
        
    pf2=str()       
    for i in range(len(pf)):
        pf2=pf2+str(pf[i])
    print(pf2)
    
        
        
    if pf2==p:
        print("ganaste")
        break
    
    if vidas==0:
        print("perdiste")
        break
    






              




