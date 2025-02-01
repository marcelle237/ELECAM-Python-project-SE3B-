import folium from geopy.distance import geodesic

#Function to calculate the distance btw 2points
def calculate_distance(point1, point2):
    return geodesic(point1, point2).miles

#Define a function to assign quarters to polling stations
def assign_quarters(quarters, polling_stattions):
    assign_quarters = {} for quarter in quarters:
    min_distance = float('inf')
    nearest_polling_station = None

    for polling_stattion in polling_stattions:
        distance = calculate_distance(quarter, polling_stattion)
        if distance < min_distance:
            min_distance = distance

            nearest_polling_station = polling_stattion

            assign_quarters[quarter] = nearest_polling_station
            return assign_quarters

#Function to search pollong station
def search_nearest_station(quarter, polling_stattions):
    assign_quarters = assign_quarters_to_stations([quarter], polling_stattions)
    return 