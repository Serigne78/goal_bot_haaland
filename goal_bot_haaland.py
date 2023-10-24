import requests
from twilio.rest import Client
import time

# Vos informations d'authentification Twilio
account_sid = 'xxxxxxxx'
auth_token = 'xxxxxxxxxx'

# Votre numéro Twilio et votre numéro de téléphone
twilio_phone_number = 'xxxxxxxx'
your_phone_number = '+xxxxxxx'

# L'URL de l'API
url = "https://api-football-v1.p.rapidapi.com/v3/players/topscorers"

# Paramètres de requête pour récupérer les statistiques d'Erling Haaland en Premier League en 2023
querystring = {"league": "39", "season": "2023"}

# Headers pour l'API RapidAPI
headers = {
    "X-RapidAPI-Key": "8b111ba3d5msha04adf3a5ea54cbp1185fbjsn746a6fd97bff",
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

# Variable pour stocker le nombre de buts précédent
buts_marques_precedent = 8

while True:
    # Effectuer une requête pour obtenir les données actualisées
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    # Trouver les statistiques du joueur Erling Haaland
    for joueur in data['response']:
        if joueur['player']['name'] == 'E. Haaland':
            statistiques_haaland = joueur['statistics']

    # Initialiser la variable pour le nombre total de buts de Haaland en Premier League
    buts_marques = 0

    # Parcourir les statistiques pour obtenir le total de buts en Premier League
    for statistique in statistiques_haaland:
        if statistique['league']['name'] == 'Premier League':
            buts_marques = statistique['goals']['total']

    # Vérifier si Erling Haaland a marqué plus de buts depuis la dernière vérification
    if buts_marques > buts_marques_precedent:
        # Créer un client Twilio
        client = Client(account_sid, auth_token)

        # Envoyer un message avec le nombre de buts marqués
        message = client.messages.create(
            from_=twilio_phone_number,
            body=f'Erling Haaland a marqué un nouveau but en Premier League en 2023. Total : {buts_marques}',
            to=your_phone_number
        )

        print(f"Message envoyé : {message.sid}")

    # Mettre à jour le nombre de buts précédent
    buts_marques_precedent = buts_marques



