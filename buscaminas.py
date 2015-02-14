from random import randrange
#Necesitamos un valor aleatorio en un rango establecido
print ("BUSCAMINAS")
print ("Ganas si descubres la posicion de todas las minas \n Pierdes si te encuentras con una de ellas")

def imprimeMatriz(ma):
    for row in ma:
        print (" ".join(str(row)))

def cuenta (x,y):
    cuenta = 0
    for i in range (max(0,x-1),min(x+1,9)):
        for j in range(max(0,y-1),min(y+1,9)):
            if matriz[i][j] == -1:
                cuenta = cuenta+1
    return cuenta

#Crea una matriz oculta 
matriz = [[0 for x in range(9)] for x in range (9)]
for a in range(0,9):
    matriz2 = [[0 for x in range(9)] for x in range (9)]
    for b in range (0,9):
        matriz2.append(0)
    matriz.append(matriz2)
        
#Crear matriz visible
matriz2 = [[0 for x in range(9)] for x in range (9)]
for c in range (0,9):
    matriz3 = [[0 for x in range(9)] for x in range (9)]
    for d in range (0,14):
        matriz3.append('#')
#Rellena la matriz con las minas
suma = 0
while suma < 6:  
    random1 = randrange(0,9)
    random2 = randrange(0,9)
    if matriz[random1][random2] != -1:
        matriz[random1][random2] = -1
        suma = suma + 1
#Conteo de minas alrededor de la i-esima casilla
for r in range (0,9):
    for s in range (0,9):
        e = cuenta(r,s)
        if matriz[r][s]!=-1:
            matriz[r][s]=e
#Comienza el juego
minaE = 0
while minaE != 5:
    print ("\n")
    found = input("Pon una '*' si has encontrado una mina o solo presiona enter si no")
    if found == "*":
        print ("Ingresa coordenadas de un lugar con minas")
        y2 =int( input ("Ingresa coordenada x:  ")) -1
        x2 = int(input ("Ingresa coordenada y:  ")) -1
        if matriz[x2][y2]==-1 :
            minaE = minaE + 1
            matriz2[x2][y2]=-1
            if MinaE==5:
                imprimeMatriz (matriz2)
                print ("Ganaste :D")
                break
        else:
            imprimeMatriz(matriz)
            print("PERDEDOR :D")
            break
    print ("Ingrese coordenadas de un lugar sin minas")
    y = int(input("Ingresa coordenada x:")) -1
    x =int(input("Ingresa coordenada y:")) -1
    if matriz[x][y]!="*":
        matriz2[x][y]=matriz[x][y]
    else:
        imprimeMatriz(matriz)
        print ("PERDEDOR")
        break
    imprimeMatriz(matriz2)
    print ("Aun te quedan",5-minaE,"minas por descubrir")
print ("\n")
exit = input ("Pulsa una tecla para salir")
