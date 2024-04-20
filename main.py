
def CYK(G, str):
    tamaño = len(str)
    M =[]
    for i in range(tamaño):
        M.append([])

#Completing the matrix
    #First case, substring length = 1
    i=0
    for a in str:
        nt=[]
        for b in G:
            if a in G[b]:
                for n in range (tamaño):
                    M[i].append("-")
                nt.append(b)
                M[i][i]=nt
        i+=1

    #For length greater than 1
    for l in range(2, tamaño+1):
        for i in range (tamaño-l+1):
            j= i+l-1
            for k in range (i,j):
                agregar=[]
                for b in G:
                    for a in G[b]:
                        if  len(a)==2:
                            nt=[]
                            for c in a:
                                nt.append(c)
                            if (nt[0] in M[k][i]) and (nt[1] in M[j][k+1]):
                                agregar.append(b)
                                M[j][i]=agregar

#Verify if the string is accepted or not

    if "S" in M[tamaño-1][0]:
        return "yes"
    else:
        return "No"







def Inicio():
    respuestas={}

    G = {}

    l = input().split(" ")
    n_nt = l[0]
    n_str = l[1]
    for h in range(int(n_nt)):
        r = input().split(" ")
        G[r[0]]=[]
        for m in range(len(r)-1):
            G[r[0]].append(r[m+1])
    for s in range(int(n_str)):
        str= input()
        respuesta= CYK(G,str)
        respuestas[str]= respuesta
    return respuestas

if __name__ == '__main__':
    casos = int(input())
    coleccion= []
    for i in range(casos):
        respuesta= Inicio();
        coleccion.append(respuesta)

    for a in coleccion:
        for x in a:
            print(f"{x} -> {a[x]}")
