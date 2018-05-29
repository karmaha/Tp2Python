#Moud atika 201400008517
#Kerrab meha 201400007461
#Sifi lamia 201300005809
#Ticherfatin cylia 201400007276
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from math import log2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def minProd(k):\n",
    "    \n",
    "    T = 0\n",
    "    for i in range(2, k+1) :\n",
    "        limite = int( log2(i)+1 )\n",
    "\n",
    "        l = 1_000_000  # tres grande valeur\n",
    "        for j in range(1, limite ) :\n",
    "            s = sliding_window(i, j)\n",
    "            l = s if s < l else l  # on ne garde que la plus petite des chianes\n",
    "        T = T + l\n",
    "\n",
    "    print( \"Somme des longueurs des chaines multiplications minimales necessaire =\", T )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Il s'agit de l'algorithme Sliding Window tel que décrit dans 'Elipical Cryptography...' avec une modification au niveau de l'étape de précalcule sensé etre ainsi plus économe."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def sliding_window(n, k):\n",
    "    \n",
    "    # chaine de puissance initiale\n",
    "    P = { 1:2, 2:4 }\n",
    "    \n",
    "    # converition en binaire \n",
    "    m = bin(n)  \n",
    "    m = m[2:][::-1]\n",
    "\n",
    "    # initialisation des variable de la boucle\n",
    "    Z = 1\n",
    "    i = len(m)-1\n",
    "    coups = 1 # coup de Z[1]=2\n",
    "\n",
    "    # la boucle lit le chiffre binaire de gauche a droite\n",
    "    while i >= 0 :\n",
    "        \n",
    "        if m[i] == '0': \n",
    "            \n",
    "            # on met au carré a chauque 0 rencontrer hors sequence          \n",
    "            Z = Z*Z\n",
    "            i = i- 1\n",
    "            coups = coups + 1\n",
    "            \n",
    "        else :\n",
    "            \n",
    "            # recherche la sequence précalculer la plus longue \n",
    "            for ii in range(k):\n",
    "\n",
    "                # évite les index negatif\n",
    "                h = i-ii if i-ii > 0 else 0\n",
    "                \n",
    "                if m[h] == '1':\n",
    "                    u = int( m[ h:i+1 ][::-1], 2)\n",
    "                    v = h\n",
    "\n",
    "            # mise au carré (i-v+1) fois\n",
    "            Z = Z**(2**(i-v+1))\n",
    "            coups = coups + i-v+1 if Z > 1 else coups # sans consequance si Z == 1\n",
    "            i = v-1\n",
    "            \n",
    "            # precalcule des puissances impaire au besoin\n",
    "            while u not in P :\n",
    "                P[2*(len(P)-1)+1] = P[2*(len(P)-1)-1]*P[2]\n",
    "                coups = coups + 1\n",
    "            \n",
    "            Z = Z*P[ u ]\n",
    "            coups = coups + 1 if Z > P[ u ] else coups # sans consequence si l'un des terme égale 1\n",
    "\n",
    "    return coups"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Somme des longueurs des chaines multiplications minimales necessaire = 1653\n"
     ]
    }
   ],
   "source": [
    "minProd(200)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
