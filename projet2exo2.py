#Moud atika 201400008517
#Kerrab meha 201400007461
#Sifi lamia 201300005809
#Ticherfatin cylia 201400007276

# coding: utf-8

# In[1]:


from math import log2


# In[2]:


def minProd(k):
    
    T = 0
    for i in range(2, k+1) :
        limite = int( log2(i)+2 )

        l = 1_000_000  # tres grande valeur
        for j in range(1, limite ) :
            s = sliding_window(i, j)
            l = s if s < l else l  # on ne garde que la plus petite des chianes
        T = T + l

    print( "Somme des longueurs des chaines multiplications minimales necessaire =", T )


# Il s'agit de l'algorithme Sliding Window tel que décrit dans 'Elipical Cryptography...' avec une modification au niveau de l'étape de précalcule sensé etre ainsi plus économe.

# In[3]:


def sliding_window(n, k):
    
    # chaine de puissance initiale
    P = { 1:2, 2:4 }
    
    # converition en binaire 
    m = bin(n)  
    m = m[2:][::-1]

    # initialisation des variable de la boucle
    Z = 1
    i = len(m)-1
    coups = 1 # coup de Z[1]=2

    # la boucle lit le chiffre binaire de gauche a droite
    while i >= 0 :
        
        if m[i] == '0': 
            
            # on met au carré a chauque 0 rencontrer hors sequence          
            Z = Z*Z
            i = i- 1
            coups = coups + 1
            
        else :
            
            # recherche la sequence précalculer la plus longue 
            for ii in range(k):

                # évite les index negatif
                h = i-ii if i-ii > 0 else 0
                
                if m[h] == '1':
                    u = int( m[ h:i+1 ][::-1], 2)
                    v = h

            # mise au carré (i-v+1) fois
            Z = Z**(2**(i-v+1))
            coups = coups + i-v+1 if Z > 1 else coups # sans consequance si Z == 1
            i = v-1
            
            # precalcule des puissances impaire au besoin
            while u not in P :
                P[ 2*len(P)-1 ] = P[ 2*len(P)-3 ]*P[2]
                coups = coups + 1
            
            Z = Z*P[ u ]
            coups = coups + 1 if Z > P[ u ] else coups # sans consequence si l'un des terme égale 1

    return coups


# In[4]:


minProd(200)


 
