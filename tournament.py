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
    raise TypeError(
        f"Object of type {obj.__class__.__name__} is not JSON serializable")

# Function to create a new tournament


def creer_nouveau_tournoi():
    nom = input("Nom du tournoi : ")
    lieu = input("Lieu : ")
    date_debut = input("Date de début : ")
    date_fin = input("Date de fin : ")
    description = input("Description : ")

    numero_tour = 1
    matches = []
    tour1 = Tour(numero_tour, matches)

    tournoi = Tournoi(nom, lieu, date_debut, date_fin,
                      [tour1], [], description)

    tournoi_json = json.dumps(tournoi, default=convert_to_json, indent=4)
    with open('tournoi.json', 'w') as fichier:
        fichier.write(tournoi_json)
    print("Le tournoi a été créé et enregistré.")

# Main menu function


def menu_principal():
    while True:
        print("Menu principal:")
        print("1. Créer un nouveau tournoi")
        choix = input("Choisissez une option (1) : ")

        if choix == '1':
            creer_nouveau_tournoi()
        else:
            print("Option invalide.")


# Run the main menu
menu_principal()
