# Zadanie 1

def elwise(L1, L2):
    size = len(L2)
    if(len(L1) > len(L2)):
        size = len(L1)
    i = 0
    lista = []
    while(size > i):
        if(len(L1) > i):
            e1 = L1[i]
        else:
            e1 = 1
        if(len(L2) > i):
            e2 = L2[i]
        else:
            e2 = 1
        lista.append(e1 * e2)
        i += 1
    return lista

L1 = [2,3,4]
L2 = [2,2,12,17]
# print(elwise(L1, L2))

# Zadanie 2

def bubbleSort(l):
    n = len(l)
    while(n > 1):
        for i in range(n - 1):
            if(l[i] > l[i + 1]):
                l[i], l[i + 1] = l[i + 1], l[i]
        n -= 1
    return l

def mediana(L):
    if(len(L) == 0):
        return None
    L = bubbleSort(L)
    if(len(L) % 2 == 1):
        return L[len(L) - (len(L) // 2) - 1]
    else:
        e1 = L[len(L) // 2 - 1]
        e2 = L[len(L) // 2]
        return (e1 + e2) // 2
#print(mediana(L2))

# Zadanie 3

def rplstr(string,old,new):
    size = len(old)
    new_string = ""
    if(len(old) == 0):
        return string
    while(len(string) > 0):
        if(string[0] != old[0]):
            new_string += string[0]
            string = string[1:]
            continue
        if(string[:size] == old):
            new_string += new
            string = string[size:]
        else:
            new_string += string[0]
            string = string[1:]
    return new_string
    
string = "Ala ma kota, kot ma Ale"
#print(rplstr(string, "ma", "niema"))

# Zadanie 4

def podciagi(l):
    dseq = {"nierosnacy":[],"niemalejacy":[],"staly":[],"rosnacy":[],"malejacy":[]}
    ldseq = {}
    s1 = ""
    s2 = ""
    s3 = ""
    s4 = ""
    s5 = ""
    s6 = ""
    for i in range(len(l)-1):
        #stale
        s1 = ""
        if(l[i] == l[i+1]):
            if(len(s1) == 0):
                s1 += str(l[i])
            s1 += " "
            s1 += str(l[i+1])
            dseq["staly"].append(s1)
        else:
            s1 = ""
        #rosnące
        if(l[i] < l[i+1]):
            if(len(s2) == 0):
                s2 += str(l[i])
            s2 += " "
            s2 += str(l[i+1])
            dseq["rosnacy"].append(s2)
        else:
            s2 = ""
        #malejace
        if(l[i] > l[i+1]):
            if(len(s3) == 0):
                s3 += str(l[i])
            s3 += " "
            s3 += str(l[i+1])
            dseq["malejacy"].append(s3)
        else:
            s3 = ""
        #niemalejacy
        if(l[i] <= l[i+1]):
            if(len(s4) == 0):
                s4 += str(l[i])
            s4 += " "
            s4 += str(l[i+1])
            dseq["niemalejacy"].append(s4)
        else:
            s4 = ""
        #nierosnacy
        if(l[i] >= l[i+1]):
            if(len(s5) == 0):
                s5 += str(l[i])
            s5 += " "
            s5 += str(l[i+1])
            dseq["nierosnacy"].append(s5)
        else:
            s5 = ""

    ciagi = list(dseq.keys())
    for i in range(len(ciagi)):
        ldseq[str(ciagi[i])] = len(ciagi[i])
        
l = [1,1,1,7,2,2,2,3,4,5]
#podciagi(l)
