# Uma função/método para determinar qual ação tomar. A decisão deve ser: Mover (em
# que direção), aspirar sujeira ou voltar para casa.
from collections import deque

class RobotActions:
    def __init__(self):
        pass
    #Change to Cardinal points
    def move(self, direction, currentLocation, energy):
        print(currentLocation)
        if direction in ["East","east"]:
            if currentLocation['Location'] not in ["D","H", "L", "P"] and energy > 0:
                print(f"Moved to {currentLocation['index'] + 1}")
                index = currentLocation['index'] + 1
                return [energy - 1, index]
            else:
                print(f"Do not move to: {currentLocation + 1}")
                return [energy, currentLocation]
            
        elif direction in ["West","west"]:
            if currentLocation not in ["A", "E", "I", "M"] and energy > 0:
                print(f"Moved to {currentLocation['index'] - 1}")
                index = currentLocation['index'] - 1
                return [energy - 1, index]
            else:
                print(f"Do not move to: {currentLocation['index'] - 1}")
                return [energy, currentLocation]
            
        elif direction in ["North", "north"]:
            if currentLocation not in ["A", "B", "C", "D"] and energy > 0:
                print(f"Moved to {currentLocation['index'] - 4}")
                index = currentLocation['index'] - 4
                return [energy - 1, index]
            else:
                print(f"Do not move to: {index}")
                return [energy, currentLocation]
         
        elif direction in ["South", "south"]:
            if currentLocation not in ["M", "N", "O", "P"] and energy > 0:
                print(f"Moved to {currentLocation['index'] + 4}")
                index = currentLocation['index'] + 4
                return [energy - 1, index]
            else:
                print(f"Do not move to: {currentLocation['index'] + 4}")
                return [energy, currentLocation]
        
        else:
            print("Invalid direction")
            return [energy, currentLocation]

    def aspire(self, energy,currentLocation, capacity):
        status = currentLocation["Status"]
        if status == "Dirty" and energy > 0 and capacity > 0:
            return [energy - 1, "Clean", capacity - 1]
        else: 
            print("Do not cleaner, localization already cleaned")
            return [energy, status, capacity]
        
    def backHome(self, staticEnvironment, currentLocation):
        # Construa um grafo a partir dos dados
        graph = {}
        for item in staticEnvironment:
            location = item["Location"]
            if location == "A":
                continue
            if location not in graph:
                graph[location] = []
            graph[location].append(item["index"])

        # Exemplo: encontrar a melhor rota de D para A
        start_location = currentLocation['Location'] # O índice de "D" é 3
        end_location = 0  # O índice de "A" é 0
        shortest_path = self.find_shortest_path(graph, start_location, end_location)

        if shortest_path:
            print("Melhor rota de {} para {}: ".format(staticEnvironment[start_location]["Location"], staticEnvironment[end_location]["Location"]))
            for index in shortest_path:
                print(f"Location: {staticEnvironment[index]['Location']} - Status: {staticEnvironment[index]['Status']}")
        else:
            print(f"Não foi possível encontrar uma rota de {currentLocation['Location']} para {staticEnvironment[end_location]['Location']}.")

    @staticmethod
    def find_shortest_path(graph, start, end):
        visited = []
        queue = deque([(start, [])])

        while queue:
            node, path = queue.popleft()
            if node == end:
                return path + [node]
            
            if node not in visited:
                visited.append(node)
                for neighbor in graph.get(node, []):
                    if neighbor not in visited:
                        queue.append((neighbor, path + [node]))

    def verifyGoal(self, staticEnvironment): 
        for item in staticEnvironment:
            if item["Status"] == "Dirty":
                return True
        return "Objective successfully achieved"