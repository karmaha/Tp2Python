
#Moud Atika 20140008517****Meha Karreb 201400007461****Sifi Lamia 201300005809******Ticherfatine Cylia 201400007276

# In[6]:


from math import sqrt


# In[7]:


def filtrer(a, b):
    # retourne une liste dépourvu d'éléments ayant un facteur premier unique dans l'interval donné
    facteur = { k : [] for k in range(a, b+1) }
    
    # calcule des facteur premier de tous les éléments
    for n in range(a, b+1) :
        m, i = n, 2
        
        while i**2 < m+1 :
            d, r = divmod(m, i)
            
            if r == 0 :
                m = d
                facteur[n].append(i)
            else:
                i = i+1
    
        if m > 1:
            facteur[n].append(m)

    R = [ i for j in facteur.values() for i in j ]
    orphelin, utile = set(), []

    # si le facteur est unique il est enregister dans orphelin
    for n in set(R) :
        if R.count(n) == 1 :
            orphelin.add(n)
    
    # on ne retiens que les éléments n'ayant aucun des facteurs contenu dans orphelin
    for n in range(a, b+1) :
        i = orphelin.intersection( facteur[n] )
        
        if len(i) == 0 :
            utile.append(n)

    return utile

# In[8]:


def combinaison(s):
    # fonction recursive créant une liste de tout les sous ensemble possible
    if s:
        rest = combinaison(s[1:])
        return rest + [[s[0]] + x for x in rest]
    return [[]]


# In[9]:


# fonction principal 
def C(a, b):
    f = filtrer(a, b)
    
    conteur = 0
    for i in combinaison(f)[1:] :
        
        c = 1
        for ii in i : # calcule du produit
            c = c*ii

        if c**(1/2)%1 == 0 : # verifie si c est un carré parfait
            conteur += 1

    print( "Nombre de carrés parfaits produits =", conteur )


# In[10]:


C(40, 55)

