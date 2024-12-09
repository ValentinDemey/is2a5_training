import numpy as np

# Fonction pour créer des données fictives
def create_data():
    data = [
        {'date': '2023-01-01', 'value': '100'},
        {'date': '2023-01-02', 'value': '150'},
        {'date': '2023-01-03', 'value': 'error'},
        {'dat': '2023-01-04', 'value': '130'},
        {'date': '2023-01-05', 'value': None},
        {'date': '2023-01-06', 'value': '180'},
        {'date': '2023-01-07', 'value': '220'},
        {'date': '2023-01-08', 'value': '190'},
        {'date': '2023-01-09', 'value': 'error'},
        {'date': '2023-01-10', 'value': '300'}
    ]
    return data

# Fonction pour vérifier la longueur des dates et supprimer la clé-valeur si la date n'est pas correcte
def validate_date_length(data):
    data_clean=[]
    for entry in data:
        if 'date' in entry:
            if len(entry['date']) != 10:
                data_clean.append(entry)
    return data

# Fonction pour calculer la somme des valeurs
def sum_values(data):
    total_sum = 0
    for entry in data:
        try:
            total_sum += float(entry['value'])
        except:
            total_sum +=0
    return total_sum

# Fonction principale pour tester le débogage
if __name__ == "__main__":
    # Créer des données
    data = create_data()
    print("Données initiales :", data)

    # Valider la longueur des dates
    data = validate_date_length(data)
    print("\nDonnées après validation des dates :", data)

    # Calculer la somme des valeurs
    total_sum = sum_values(data)
    print("\nSomme totale des valeurs :", total_sum)
