import sqlite3

# Connexion à la base de données "animal_db"
bdd = sqlite3.connect("animal_db")
# Création d'un curseur pour exécuter des requêtes SQL
curseur = bdd.cursor()

# Création des tables s'ils n'existent pas déjà
curseur.execute("CREATE TABLE IF NOT EXISTS animal (Id_animal INTEGER PRIMARY KEY, nom TEXT, age INT, taille FLOAT, masse INT, nom_espece TEXT, Id_espece INT)")
curseur.execute("CREATE TABLE IF NOT EXISTS enclos (Id_enclos INTEGER PRIMARY KEY, numero_enclos FLOAT, ecosysteme TEXT, surface INT, struct TEXT, date_entretien TEXT)")
curseur.execute("CREATE TABLE IF NOT EXISTS espece (Id_espece INTEGER PRIMARY KEY, nom_espece TEXT, classe TEXT, alimentation TEXT)")
curseur.execute("CREATE TABLE IF NOT EXISTS soin_animaux (Id_animal INTEGER PRIMARY KEY, prise_temp FLOAT, type_vaccin TEXT, date_vaccin TEXT, nature_dernier_soins TEXT, nature_soin_en_cours TEXT)")

def peupler_tables(table, *args):
    """
    Insère des données dans la table spécifiée.

    Args:
        table (str): Nom de la table où insérer les données.
        *args: Les données à insérer dans la table.
    """
    # Sélectionne la requête d'insertion en fonction de la table spécifiée
    if table == "animal":
        curseur.execute("INSERT INTO animal (Id_animal, nom, age, taille, masse, nom_espece, Id_espece) VALUES (?, ?, ?, ?, ?, ?, ?)", args)
    elif table == "enclos":
        curseur.execute("INSERT INTO enclos (Id_enclos, num_enclos, ecosysteme, surface, struct, date_entretien) VALUES (?, ?, ?, ?, ?, ?)", args)
    elif table == "espece":
        curseur.execute("INSERT INTO espece (Id_espece, nom_espece, classe, alimentation) VALUES (?, ?, ?, ?)", args)
    elif table == "soin_animaux":
        curseur.execute("INSERT INTO soin_animaux (Id_animal, prise_temp, type_vaccin, date_vaccin, nature_dernier_soins, nature_soin_en_cours) VALUES (?, ?, ?, ?, ?, ?)", args)

    # Valide les modifications dans la base de données
    bdd.commit()


def afficher(table):
    """
    Affiche tous les enregistrements de la table spécifiée.

    Args:
        table (str): Nom de la table à afficher.

    Returns:
        list: Liste contenant tous les enregistrements de la table.
    """
    # Construit la requête SELECT pour récupérer tous les enregistrements de la table
    requete = f"SELECT * FROM {table}"
    # Exécute la requête SQL
    curseur.execute(requete)
    # Récupère tous les enregistrements et les renvoie sous forme de liste
    return curseur.fetchall()

def supprimer(table):
    """
    Supprime tous les enregistrements de la table spécifiée.

    Args:
        table (str): Nom de la table à vider.

    Returns:
        str: Message indiquant que tous les enregistrements ont été supprimés.
    """
    # Exécute la requête DELETE pour supprimer tous les enregistrements de la table
    curseur.execute(f"DELETE FROM {table}")
    # Valide les modifications dans la base de données
    bdd.commit()
    return "Tous les enregistrements de la table ont été supprimés."

def supprimer_bis(id, table):
    """
    Supprime un enregistrement spécifique dans la table spécifiée.

    Args:
        id (int): ID de l'enregistrement à supprimer.
        table (str): Nom de la table où se trouve l'enregistrement.

    Returns:
        str: Message indiquant que l'enregistrement a été supprimé.
    """
    # Sélectionne la requête DELETE en fonction de la table spécifiée
    if table=='animal':
        curseur.execute(f"DELETE FROM {table} WHERE Id_animal=?", (id,))
    elif table=='espece':
        curseur.execute(f"DELETE FROM {table} WHERE Id_espece=?", (id,))
    elif table=='enclos':
        curseur.execute(f"DELETE FROM {table} WHERE Id_enclos=?", (id,))
    elif table=='soin_animaux':
        curseur.execute(f"DELETE FROM {table} WHERE Id_animal=?", (id,))
    # Valide les modifications dans la base de données
    bdd.commit()
    return f"L'enregistrement avec l'ID {id} dans la table {table} a été supprimé."

def remplacer(table, id, **donnees):
    """
    Remplace les données d'un enregistrement dans la table spécifiée.

    Args:
        table (str): Nom de la table où se trouve l'enregistrement à modifier.
        id (int): ID de l'enregistrement à modifier.
        **donnees: Nouvelles valeurs des champs à mettre à jour.
    """
    # Crée une chaîne de caractères pour les champs à mettre à jour
    champs = ', '.join([f"{cle} = ?" for cle in donnees.keys()])
    # Récupère les nouvelles valeurs des champs à mettre à jour
    valeurs = tuple(donnees.values())
    
    # Exécute la requête UPDATE en fonction de la table spécifiée
    if table == "soin_animaux":
        bdd.execute(f"UPDATE {table} SET {champs} WHERE Id_animal = ?", valeurs + (id,))
    else:
        bdd.execute(f"UPDATE {table} SET {champs} WHERE Id_{table} = ?", valeurs + (id,))
    
    # Valide les modifications dans la base de données
    bdd.commit()