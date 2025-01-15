import googlemaps

# Initialize Google Maps API client
gmaps = googlemaps.Client(key='YOUR_GOOGLE_MAPS_API_KEY')

def get_closest_polling_station(quarter, polling_stations):
    closest_station = None
    min_distance = float('inf')

    for station in polling_stations:
        # Get the distance between the quarter and the polling station
        distance_matrix = gmaps.distance_matrix(
            origins={(quarter.latitude, quarter.longitude)},
            destinations={(station.latitude, station.longitude)},
            mode="driving"
        )
        distance = distance_matrix['rows'][0]['elements'][0]['distance']['value']

        if distance < min_distance:
            min_distance = distance
            closest_station = station

    return closest_station, min_distance
