import numpy as np

#Función que calcula la matriz resultante C después de aplicar la operación convolución de A*B
def convolucion(A,B):
    C=0
    return C

matriz1=[[6,9,0,3],[8,4,9,1],[4,1,3,12],[3,2,1,100]]
filtro=[[1,0,2],[5,0,9],[6,2,1]]

A=np.array(matriz1)
B=np.array(filtro)

C=np.zeros((2,2))

C[0][0]=((A[0][0])*(B[0][0]))+((A[0][1])*(B[0][1]))+((A[0][2])*(B[0][2]))+((A[1][0])*(B[1][0]))+((A[1][1])*(B[1][1]))+((A[1][2])*(B[1][2]))+((A[2][0])*(B[2][0]))+((A[2][1])*(B[2][1]))+((A[2][2])*(B[2][2]))

C[0][1]=((A[0][1])*(B[0][0]))+((A[0][2])*(B[0][1]))+((A[0][3])*(B[0][2]))+((A[1][1])*(B[1][0]))+((A[1][2])*(B[1][1]))+((A[1][3])*(B[1][2]))+((A[2][1])*(B[2][0]))+((A[2][2])*(B[2][1]))+((A[2][3])*(B[2][2]))

C[1][0]=((A[1][0])*(B[0][0]))+((A[1][1])*(B[0][1]))+((A[1][2])*(B[0][2]))+((A[2][0])*(B[1][0]))+((A[2][1])*(B[1][1]))+((A[2][2])*(B[1][2]))+((A[3][0])*(B[2][0]))+((A[3][1])*(B[2][1]))+((A[3][2])*(B[2][2]))

C[1][1]=((A[1][1])*(B[0][0]))+((A[1][2])*(B[0][1]))+((A[1][3])*(B[0][2]))+((A[2][1])*(B[1][0]))+((A[2][2])*(B[1][1]))+((A[2][3])*(B[1][2]))+((A[3][1])*(B[2][0]))+((A[3][2])*(B[2][1]))+((A[3][3])*(B[2][2]))

print(A)

print(A[1][0])

print(C)

matriz2=[[1,2,3,4,5,6],[7,8,9,10,11,12],[0,0,1,16,17,18],[0,1,0,7,23,24],[1,7,6,5,4,3]]
filtro2=[[1,1,1],[0,0,0],[2,10,3]]

D=np.array(matriz2)
E=np.array(filtro2)

F=np.zeros((3,4))


matriz=[[1,2,3,4,5,6],[7,8,9,10,11,12],[0,0,1,16,17,18],[0,1,0,7,23,24],[1,7,6,5,4,3]]
filtro=[[1,1,1],[0,0,0],[2,10,3]]

matriz2=[]
matriz=np.array(matriz)
filtro=np.array(filtro)

cont=0
cont_2=0
resultado=0
for i in range(len(matriz)):
    for x in range(len(filtro[0])):
        for y in range(len(filtro[0])):
            resultado +=(matriz[x+cont_2][y])*(filtro[x][y])
            cont= cont +1
            if cont ==9:
                matriz2.append(resultado)
                resultado=0
                break            
    con_2=cont_2 +1 
print(matriz2) 

