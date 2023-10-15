
class WaterJugProblem:
    def __init__(self, capacity1, capacity2, target):
        self.capacity1 = capacity1
        self.capacity2 = capacity2
        self.target = target
        self.visited = set()

    def is_goal_state(self, state):
        return state[0] == self.target or state[1] == self.target

    def get_successors(self, state):
        successors = []
        successors.append((self.capacity1, state[1]))  # Fill jug1
        successors.append((state[0], self.capacity2))  # Fill jug2
        successors.append((0, state[1]))  # Empty jug1
        successors.append((state[0], 0))  # Empty jug2
        successors.append((max(0, state[0] - (self.capacity2 - state[1])), min(state[1] + state[0], self.capacity2)))  # Pour from jug1 to jug2
        successors.append((min(state[0] + state[1], self.capacity1), max(0, state[1] - (self.capacity1 - state[0]))))  # Pour from jug2 to jug1
        return [s for s in successors if s not in self.visited]

    def dfs(self, state, path):
        if state in self.visited:
            return False
        self.visited.add(state)
        path.append(state)  # Add the current state to the path

        if self.is_goal_state(state):
            print("Goal state reached:", state)
            print("Solution path:")
            for step in path:
                print(step)
            return True

        for successor in self.get_successors(state):
            if self.dfs(successor, path):
                return True

        path.pop()  # Remove the current state from the path
        return False

    def solve(self):
        initial_state = (0, 0)
        if self.dfs(initial_state, []):
            print("Solution exists.")
        else:
            print("Solution does not exist.")

# Example usage:
jug_problem = WaterJugProblem(5, 4, 2)
jug_problem.solve()