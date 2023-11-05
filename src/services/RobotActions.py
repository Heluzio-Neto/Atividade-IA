# Uma função/método para determinar qual ação tomar. A decisão deve ser: Mover (em
# que direção), aspirar sujeira ou voltar para casa.
from collections import deque

class RobotActions:
    def __init__(self):
        pass
    #Change to Cardinal points
    def move(self, direction, currentLocation, energy):
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
        
    def backHome(self, staticEnvironment, currentLocation, energy):
        print("Inital location: {}".format(currentLocation["Location"]))

        fourth_line = ["M", "N", "O", "P"]
        third_line = ["I", "J", "K", "L"]
        second_line = ["E", "F", "G", "H"]
        first_line = ["A", "B", "C", "D"]

        path = []
        energy_local = None
        

        # If the current location is in the Fourth line
        if currentLocation['Location'] in fourth_line:
            if currentLocation['Location'] != "M":
                for i in range(0, 3):
                    [en, index_actual] = self.move("North", currentLocation, energy)
                    path.append(staticEnvironment[index_actual]['Location'])
                    currentLocation = staticEnvironment[index_actual]
                valueToFor = self.verifyQttToHome(first_line, currentLocation['Location'])
                for i in range(0, valueToFor):
                    [en, index_actual] = self.move("West", currentLocation, energy)
                    path.append(staticEnvironment[index_actual]['Location'])
                    currentLocation = staticEnvironment[index_actual]       
                    energy_local = energy - (len(path))  
                return ["Back to Home Successfully", path, currentLocation, energy_local] 
            
            elif currentLocation['Location'] == "M":
                for i in range(0, 3):
                    [en, index_actual] = self.move("North", currentLocation, energy)
                    path.append(staticEnvironment[index_actual]['Location'])
                    currentLocation = staticEnvironment[index_actual]
                    energy_local = energy - (len(path))  
                return ["Back to Home Successfully", path, currentLocation, energy_local] 
        
        # If the current location is in the Third line
        if currentLocation['Location'] in third_line:
            if currentLocation['Location'] != "I":
                for i in range(0, 2):
                    [en, index_actual] = self.move("North", currentLocation, energy)
                    path.append(staticEnvironment[index_actual]['Location'])
                    currentLocation = staticEnvironment[index_actual]
                valueToFor = self.verifyQttToHome(first_line, currentLocation['Location'])
                for i in range(0, valueToFor):
                    [en, index_actual] = self.move("West", currentLocation, energy)
                    path.append(staticEnvironment[index_actual]['Location'])
                    currentLocation = staticEnvironment[index_actual]       
                    energy_local = energy - (len(path))         
                return ["Back to Home Successfully", path, currentLocation, energy_local] 
            
            elif currentLocation['Location'] == "I":
                for i in range(0, 2):
                    [en, index_actual] = self.move("North", currentLocation, energy)
                    path.append(staticEnvironment[index_actual]['Location'])
                    currentLocation = staticEnvironment[index_actual]
                    energy_local = energy - (len(path))  
                return ["Back to Home Successfully", path, currentLocation, energy_local] 
        
        # If the current location is in the Second line
        if currentLocation['Location'] in second_line:
            if currentLocation['Location'] != "E":
                for i in range(0, 1):
                    [en, index_actual] = self.move("North", currentLocation, energy)
                    path.append(staticEnvironment[index_actual]['Location'])
                    currentLocation = staticEnvironment[index_actual]
                valueToFor = self.verifyQttToHome(first_line, currentLocation['Location'])
                for i in range(0, valueToFor):
                    [en, index_actual] = self.move("West", currentLocation, energy)
                    path.append(staticEnvironment[index_actual]['Location'])
                    currentLocation = staticEnvironment[index_actual]       
                    energy_local = energy - (len(path))         
                return ["Back to Home Successfully", path, currentLocation, energy_local] 
            
            elif currentLocation['Location'] == "E":
                for i in range(0, 1):
                    [en, index_actual] = self.move("North", currentLocation, energy)
                    path.append(staticEnvironment[index_actual]['Location'])
                    currentLocation = staticEnvironment[index_actual]
                    energy_local = energy - (len(path))  
                return ["Back to Home Successfully", path, currentLocation, energy_local] 

        # If the current location is in the First line
        if currentLocation['Location'] in first_line:
            if currentLocation['Location'] != "A":
                valueToFor = self.verifyQttToHome(first_line, currentLocation['Location'])
                for i in range(0, valueToFor):
                    [en, index_actual] = self.move("West", currentLocation, energy)
                    path.append(staticEnvironment[index_actual]['Location'])
                    currentLocation = staticEnvironment[index_actual]       
                    energy_local = energy - (len(path))         
                return ["Back to Home Successfully", path, currentLocation, energy_local] 
            
            elif currentLocation['Location'] == "A":
                path = []
                energy_local = energy
                return ["Already in Home", path, currentLocation, energy_local]             
        else:    
            pass
    
    @staticmethod
    def verifyQttToHome(line_values, location_actual):
        for index, v in enumerate(line_values):
            if location_actual == v:
                return index

    def verifyGoal(self, staticEnvironment): 
        for item in staticEnvironment:
            if item["Status"] == "Dirty":
                return "Fail to clean"
        return "Objective successfully achieved"