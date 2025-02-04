# %%
# Exercice: 1

''' 
Description: Exercice 1
À partir de deux nombre a et b, écrire le résultat pour l’addition, la soustraction, la division et la
multiplication.
'''
a = 10;
b = 5;
print("Addition: ", a+b);

# %%
# Exercice: 2

''' 
Description: Exercice 2
Écrire un algorithme permettant d’afficher le double d’un nombre x.
'''
x=4;
print("Double de x: ", x*2);

# %%
# Exercice: 3

''' 
Description: Exercice 3
Écrire un algorithme permettant de calculer l’air d’un carré de côté x.
'''
y=5;
print("Carré de y:" ,y*y);

# %%
# Exercice: 4

''' 
Description: Exercice 4
Écrire un algorithme qui affiche « Hello prénom » où prénom est une valeur saisie par l’utilisateur.
'''
prenom=input("Entrez votre prénom:");
print("Hello", prenom);

# %%
# Exercice: 5

'''
Description: Exercice 5
Écrire un algorithme permettant de calculer l’âge d’une personne à partir de son année de naissance
saisie au clavier.
'''
annee_naissance = int(input("Entrez votre année de naissance:"));
annee_actuelle = 2025;
age= annee_actuelle - annee_naissance;
print("Votre âge est: ", age);

# %%
# Exercice: 6

''' 
Description: Exercice 6
Écrire un algorithme qui calcul le prix TTC à partir d’un prix HT et d’une TVA de 20 % (prestation
de service en France).
'''
prix_HT = 100;
TVA = 20;
prix_TTC = prix_HT + (prix_HT * TVA/100);
print("Prix TTC: ", prix_TTC);

# %%
# Exercice: 7

'''
Description: Exercice 7
Calculez le volume d’un parallélépipède dont la largeur, la longueur et la hauteur seront saisies au
clavier.
'''
