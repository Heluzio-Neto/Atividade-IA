# • Implementação do ambiente estático. Você precisa definir um array ou alguma outra
# estrutura de dados que representará as localizações (de A a P).
# • Uma função/método para determinar qual ação tomar. A decisão deve ser: Mover (em
# que direção), aspirar sujeira ou voltar para casa.
# • Uma função/método para determinar em qual direção seguir.
# • Uma função/método para identificar a rota e navegar de volta para casa a partir da
# localização atual.
# • Uma função/método para testar se o objetivo desejado foi alcançado ou não.

from services.RobotActions import RobotActions
from collections import deque

class RobotVacuumCleaner(RobotActions):
    
    staticEnvironment = [
        {"Location": "A", "Status": "Clean", "index": 0}, 
        {"Location": "B", "Status": "Dirty", "index": 1}, 
        {"Location": "C", "Status": "Clean", "index": 2}, 
        {"Location": "D", "Status": "Dirty", "index": 3},
        {"Location": "E", "Status": "Clean", "index": 4}, 
        {"Location": "F", "Status": "Dirty", "index": 5}, 
        {"Location": "G", "Status": "Clean", "index": 6}, 
        {"Location": "H", "Status": "Dirty", "index": 7},
        {"Location": "I", "Status": "Clean", "index": 8}, 
        {"Location": "J", "Status": "Dirty", "index": 9}, 
        {"Location": "K", "Status": "Clean", "index": 10}, 
        {"Location": "L", "Status": "Dirty", "index": 11},
        {"Location": "M", "Status": "Clean", "index": 12}, 
        {"Location": "N", "Status": "Dirty", "index": 13}, 
        {"Location": "O", "Status": "Clean", "index": 14}, 
        {"Location": "P", "Status": "Dirty", "index": 15}
    ]

    currentLocation = staticEnvironment[0]

    energy = 100
    capacity = 10

    def __init__(self):
        #self.showEnvironment()
        pass

    def showEnvironment(self):
        for line in self.staticEnvironment:
            print(line)
    
    def actionToDo(self, action, direction = None):
        if action == "Move":
            print(f"Move to: {direction}")
            [self.energy, new_index] = self.move(direction, self.currentLocation, self.energy)
            self.currentLocation = self.staticEnvironment[new_index]
        elif action == "Cleaner": 
            print("Actual energy: {}".format(self.energy))
            print("Actual location: {}".format(self.currentLocation['index']))
            print("Actual capacity: {}".format(self.capacity))

            [self.energy, self.staticEnvironment[self.currentLocation['index']]["Status"], self.capacity] = self.aspire(self.energy, self.staticEnvironment[self.currentLocation["index"]], self.capacity) 

        elif action == "Home":
            self.backHome(self.staticEnvironment, self.staticEnvironment[self.currentLocation])
    
    def find_location(self, desired_location):
        found_dict = None

        for item in self.staticEnvironment:
            if item["Location"] == desired_location:
                found_dict = item
                break

        return found_dict


robot = RobotVacuumCleaner()
robot.actionToDo("Move", "East")
robot.actionToDo("Cleaner")
robot.actionToDo("Move", "East")
robot.actionToDo("Cleaner")
robot.actionToDo("Move", "East")
robot.actionToDo("Cleaner")
robot.actionToDo("Move", "South")
robot.actionToDo("Cleaner")
robot.actionToDo("Move", "South")
robot.actionToDo("Cleaner")
robot.actionToDo("Move", "South")
robot.actionToDo("Cleaner")
print(robot.staticEnvironment[robot.currentLocation["index"]])

