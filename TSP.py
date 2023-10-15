class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.visited = False

    def distance_to(self, other_city):
        return ((self.x - other_city.x) ** 2 + (self.y - other_city.y) ** 2) ** 0.5

def nearest_neighbor_tsp(cities):
    start_city = cities[0]
    start_city.visited = True
    tour = [start_city]
    total_distance = 0  # To keep track of the total distance

    while len(tour) < len(cities):
        current_city = tour[-1]
        min_distance = float('inf')
        nearest_city = None

        for city in cities:
            if not city.visited:
                distance = current_city.distance_to(city)
                if distance < min_distance:
                    min_distance = distance
                    nearest_city = city

        nearest_city.visited = True
        tour.append(nearest_city)
        total_distance += min_distance

    # Return to the starting city to complete the tour
    tour.append(start_city)
    total_distance += start_city.distance_to(tour[-2])  # Add the distance back to the starting city

    return tour, total_distance

# Example usage:
city1 = City("A", 0, 0)
city2 = City("B", 15, 9)
city3 = City("C", 14, 5)
city4 = City("D", 10, 7)

cities = [city1, city2, city3, city4]
optimal_tour, shortest_distance = nearest_neighbor_tsp(cities)

print("Optimal tour order:")
for city in optimal_tour:
    print(city.name)

print(f"Shortest distance: {shortest_distance:.2f}")
