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
largeur = int(input("Entrez la largeur:"));
longueur = int(input("Entrez la longueur:"));
hauteur = int(input("Entrez la hauteur:"));
volume = largeur * longueur * hauteur;

print("Volume du parallélépipède: ", volume);

# %%
# Exercice: 8

''' 
Saisissez le prix unitaire HT d’un produit et la quantité commandée. Calculez le montant HT de la
commande, appliquez une remise de 15% et calculez le prix TTC après avoir saisi le taux de TVA.
'''
prix_unitaire_HT = int(input("Entrez le prix unitaire HT:"));
quantite = int(input("Entrez la quantité commandée:"));
montant_HT = prix_unitaire_HT * quantite;
montant_remise =montant_HT - (montant_HT *15/100);
TVA = int(input("Entrez le taux de TVA:"));
prix_TTC=montant_remise + (montant_remise*TVA/100);

print("Prix TTC: ", prix_TTC);

# %%
# Exercice: 9

'''
Calculez la moyenne des notes d’un élève après avoir saisi les notes de français, de math, de
géométrie et d’informatique.
'''

note_francais = int(input("Entrez la note de français:"));
note_math = int(input("Entrez la note de math:"));
note_geometrie = int(input("Entrez la note de géométrie:"));
note_informatique = int(input("Entrez la note d'informatique:"));

moyenne = (note_francais + note_math + note_geometrie + note_informatique)/4;

print("Moyenne: ", moyenne);

# %%
# Exercice: 10

'''
Affichez une table de multiplication (jusqu’à 10) dont l’ordre (le nombre concerné) sera saisi au
clavier.
'''

ordre = int(input("Entrez l'ordre:"));
for i in range (1,11):
    print(ordre,"*",i,"=",ordre*i);

