import sqlite3
import csv

# Connexion à la base de données (créera la base de données si elle n'existe pas)
conn = sqlite3.connect('animaux.db')

# Création d'un curseur pour exécuter des requêtes SQL
cur = conn.cursor()

# Lecture des données à partir du fichier CSV et insertion en blocs
with open('donnees_animaux.csv', 'r') as f:
    reader = csv.reader(f)
    # Ignorer l'en-tête si nécessaire
    next(reader)
    # Insérer les données en blocs
    cur.executemany("INSERT INTO Animaux (filename, label) VALUES (?, ?)", reader)

# Validation des modifications et fermeture de la connexion
conn.commit()
conn.close()

print("Données insérées avec succès.")