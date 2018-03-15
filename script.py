# per ogni regione ordinare in base a valore minore di latenza


V=0
S=0
C=0
P=0
prov = []
nazioni = []
req = []
# creo un vettore di V elementi
# il cui elemento contiene:
# vettori di dizionari che contengono: max, prezzo,
# pacchetto(vettore di s el) e un vettore lag di C elementi


def leggifile(input):
    fin = open(input, "r")
    primaRiga = fin.readline().split()
    global V,S,C,P,prov,req, nazioni
    V = int(primaRiga[0])
    S = int(primaRiga[1])
    C = int(primaRiga[2])
    P = int(primaRiga[3])
    fin.readline()
    nazioni = fin.readline().split()
    for i in range(0,V):    # scorro i provider
        riga = fin.readline().split()
        n = int(riga[1])
        temp2 = []
        for j in range(0,n): # scorro le regioni dentro il provider
            region = {}
            fin.readline() # salto nome regione
            line = fin.readline().split()
            region["tot"] = int(line[0])
            region["prezzo"] = float(line[1])
            vett = []
            for k in range(0,S):
                vett.append(int(line[k+2]))

            region["pacchetto"] = vett

            line = fin.readline().split() # ora leggo lag
            vett = []
            for k in range(0, C):
                vett.append(int(line[k]))
            region["lag"] = vett
            temp2.append(region)
        prov.append(temp2)
    # ora con le richieste
    for i in range(0,P):
        temp = {}
        line = fin.readline().split()
        temp["multa"] = int(line[0])
        temp["nazione"] = nazioni.index(line[1])
        vett = []
        for j in range(0,S):
            vett.append(int(line[j+2]))
        temp["valori"] = vett # contiene i valori richiesti per ogni servizio
        req.append(temp)




def funvecchia():
    for i in range(len(prov)): # scorro provider
        for j in range(len(nazioni)):# scorro le nazioni
            for k in range(len(prov[i])): # scorro le regioni del provider
                print(len(prov[i]))


def fun():
    for r in req:
        indexProv = None
        indexReg = None
        naz = r["nazione"]  # dove è la richiesta
        for i in range(len(prov)):
            pr = prov[i]
            min = None
            for reg in pr: # reg è un dizionario
                lag = reg["lag"][naz]
                if min==None or lag < min:
                    min = lag
                    indexProv = i # indice del provider
                    indexReg =








if __name__ == '__main__':
    leggifile("1.in")
    print(prov)
    print(req)