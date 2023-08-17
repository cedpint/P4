import json

class Joueur:
    def __init__(self, nom, prenom, date_naissance, identifiant):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.identifiant = identifiant

class Match:
    def __init__(self, joueur1, joueur2, resultat):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = resultat

class Tour:
    def __init__(self, numero, matches):
        self.numero = numero
        self.matches = matches

class Tournoi:
    def __init__(self, nom, lieu, date_debut, date_fin, tours, joueurs, description):
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.tours = tours
        self.joueurs = joueurs
        self.description = description

# Convert function for JSON 
def convert_to_json(obj):
    if isinstance(obj, (Joueur, Match, Tour, Tournoi)):
        return obj.__dict__
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

# Example players, matches, tournament
joueur1 = Joueur("Dubois", "Patrick", "1990-01-15", "AB12345")
joueur2 = Joueur("Leblond", "Caroline", "1988-05-20", "CD67890")
match1 = Match(joueur1, joueur2, 0)  
match2 = Match(joueur1, joueur2, 0.5)  
match3 = Match(joueur1, joueur2, 1)  
tour1 = Tour(1, [match1, match2, match3])
tournoi = Tournoi("First Tournament", "Paris", "2023-08-01", "2023-08-10", [tour1], [joueur1, joueur2], "Friendly Tournament")

# Convert the tournament instance to JSON 
tournoi_json = json.dumps(tournoi, default=convert_to_json, indent=4)
with open('tournoi.json', 'w') as fichier:
    fichier.write(tournoi_json)