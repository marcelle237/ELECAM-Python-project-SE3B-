

Pollings = [
    polling = [
        {
            "station": "AWAE",
            "Quater": [
                "Nkomo", "Awae", "Mfou", "Nkoabang", "Petou"
            ],
            "latitude": 
            "longitude":
        }
    ],
    polling = [
        {
            "station": "Mobile Omnisport",
            "Quater": [
                "Ngousso", "Soa", "Essos", "Fourgerole", "Petou"
            ],
            "latitude": 
            "longitude":
        }
    ],
    polling = [
        {
            "station": "Bastos",
            "Quater": [
                "Manguier", "Bata Nlongkak", "Mballa2", "Elig-Edzoa", "Ecole de police"
            ],
            "latitude": 
            "longitude":
        }
    ],
]

def getstation():
    for polling in Pollings:
        if user_quarter in polling ['Quater']:
            return polling['station']

    return None