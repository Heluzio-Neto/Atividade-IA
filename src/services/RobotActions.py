# Uma função/método para determinar qual ação tomar. A decisão deve ser: Mover (em
# que direção), aspirar sujeira ou voltar para casa.

class RobotActions:
    def __init__(self):
        pass
    def move(self, direction, currentLocation):
        currentLocation = int(currentLocation)
        print(currentLocation)
        if direction == "Right":
            if currentLocation not in [3,7,11,15]:
                print(f"Moved to {currentLocation + 1}")
                return currentLocation + 1
            else:
                print(f"Do not move to: {currentLocation + 1}")
                return currentLocation
            
        elif direction == "Left":
            if currentLocation not in [0,4,8,12]:
                print(f"Moved to {currentLocation + 1}")
                return currentLocation + 1
            else:
                print(f"Do not move to: {currentLocation + 1}")
                return currentLocation
            
        elif direction == "Top":
            if currentLocation not in [0,1,2,3]:
                print(f"Moved to {currentLocation + 1}")
                return currentLocation + 1
            else:
                print(f"Do not move to: {currentLocation + 1}")
                return currentLocation
         
        elif direction == "Bottom":
            if currentLocation not in [12,13,14,15]:
                print(f"Moved to {currentLocation + 1}")
                return currentLocation + 1
            else:
                print(f"Do not move to: {currentLocation + 1}")
                return currentLocation
        else:
            print("Invalid direction")

    def aspire(self):
        pass 
    def backHome(self):
        pass 