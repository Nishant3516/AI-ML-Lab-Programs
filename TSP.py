class TravelingSalesman:
    def __init__(self, distance_matrix):
        self.distance_matrix = distance_matrix
        self.num_cities = len(distance_matrix)

    def nearest_neighbor_tsp(self):
        unvisited_cities = set(range(self.num_cities))
        tour = [0]  # Start from the first city (city 0)
        unvisited_cities.remove(0)
        total_distance = 0

        while unvisited_cities:
            current_city = tour[-1]
            nearest_city = min(unvisited_cities, key=lambda city: self.distance_matrix[current_city][city])
            tour.append(nearest_city)
            total_distance += self.distance_matrix[current_city][nearest_city]
            unvisited_cities.remove(nearest_city)

        # Return to the starting city to complete the tour
        tour.append(0)
        total_distance += self.distance_matrix[tour[-2]][0]

        return tour, total_distance

# Example usage:
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp = TravelingSalesman(distance_matrix)
optimal_tour, shortest_distance = tsp.nearest_neighbor_tsp()

print("Optimal tour order:")
print(optimal_tour)
print(f"Shortest distance: {shortest_distance}")
