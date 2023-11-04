# Uma função/método para determinar qual ação tomar. A decisão deve ser: Mover (em
# que direção), aspirar sujeira ou voltar para casa.
from collections import deque
from collections import defaultdict

class RobotActions:
    def __init__(self):
        pass
    #Change to Cardinal points
    def move(self, direction, currentLocation, energy):
        currentLocation = int(currentLocation)

        if direction in ["East","east"]:
            if currentLocation not in [3,7,11,15] and energy > 0:
                print(f"Moved to {currentLocation + 1}")
                return [energy - 1, currentLocation + 1]
            else:
                print(f"Do not move to: {currentLocation + 1}")
                return [energy, currentLocation]
            
        elif direction in ["West","west"]:
            if currentLocation not in [0,4,8,12] and energy > 0:
                print(f"Moved to {currentLocation + 1}")
                return [energy - 1, currentLocation + 1]
            else:
                print(f"Do not move to: {currentLocation + 1}")
                return [energy, currentLocation]
            
        elif direction in ["North", "north"]:
            if currentLocation not in [0,1,2,3] and energy > 0:
                print(f"Moved to {currentLocation + 1}")
                return [energy - 1, currentLocation + 1]
            else:
                print(f"Do not move to: {currentLocation + 1}")
                return [energy, currentLocation]
         
        elif direction in ["South", "south"]:
            if currentLocation not in [12,13,14,15] and energy > 0:
                print(f"Moved to {currentLocation + 1}")
                return [energy - 1, currentLocation + 1]
            else:
                print(f"Do not move to: {currentLocation + 1}")
                return [energy, currentLocation]
        
        else:
            print("Invalid direction")
            return [energy, currentLocation]

    def aspire(self, energy,currentLocation):
        status = currentLocation["Status"]
        if status == "Dirty" and energy > 0:
            return [energy - 1, "Clean"]
        else: 
            print("Do not cleaner, localization already cleaned")
            return [energy, status]

    def verifyHandbag(self):
        pass