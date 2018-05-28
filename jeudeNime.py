
#Moud Atika 20140008517****Meha Karreb 201400007461****Sifi Lamia 201300005809******Ticherfatine Cylia 201400007276
from random import randrange
import pickle

def update(winner, loser, score, rounds):
	# met a jour le fichier score selon le resultat de la partie jouer
	point = 0
	
	for i in range(1, rounds+1) :
		point += i*10**i 
	
	if winner in score:
		score[winner][1] = point 
		score[winner][0] = min( score[winner][0], point) 
	else:
		score[winner] = [ point, point ]

	if loser in score :
		score[loser][1] = float('inf')
	else:
		score[loser] = [ float('inf'), float('inf') ] # plus adapter a la logique du jeu

	return score

def best_10(score):
	# affiche le 10 meilleurs score

	print('Les Meilleurs Scores :')
	names, points = zip( *score.items() )
	best, _ = zip(*points)
	
	L = list( zip(names, best) )
	L.sort( key = lambda x: x[1] )

	for u in range( min(10, len(L)) ):
		print( L[u][0], ':', L[u][1] )

def prompt(tab):
	# imprime la plache de jeu a chaque coups
	for t, u in enumerate(tab) :
		print( f"{t+1} |", '*'*u, ' '*(max(tab)-u), f"| {u}" )

def main():
	try :
		# en cas ou le fichier existe deja
		with open('score', 'rb') as file :
			score = pickle.load(file)
	except :
		# cas ou le fichier n'existe pas
		score = {}

	# debut de partie
	a = input('Joueur 1 :')
	b = input('Joueur 2 :')
	p = [a, b]

	tab = [ randrange(5,24) for _ in range( randrange(3,8) ) ]
	prompt(tab)

	rounds = 0
	player = randrange(0,2)

	# loop principal du jeu
	while sum(tab) > 0 :
		i, j = input( p[player]+' entrez votre coups :' ).split('-')
		line = eval(i)
		pion = eval(j)

		# interception des entrer non valide 
		try :
			tab[line-1] -= pion
			if tab[line-1] < 0 :
				ValueError
		except :
			print('Coups Invalide...')
			continue

		rounds += 1
		player = (player+1) %2
		prompt(tab)

	# fin de la partie
	winner, loser = p[player], p[ (player+1) %2 ]
	best_10( update(winner, loser, score, rounds) )

	# enregistrement des scores
	with open('score', 'wb') as file :
		pickle.dump(score, file)

	decision = input("Voulez-vous rejouer ? [oui/non] :")
	main() if decision == 'oui' else None

main()
