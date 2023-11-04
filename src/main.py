# • Implementação do ambiente estático. Você precisa definir um array ou alguma outra
# estrutura de dados que representará as localizações (de A a P).
# • Uma função/método para determinar qual ação tomar. A decisão deve ser: Mover (em
# que direção), aspirar sujeira ou voltar para casa.
# • Uma função/método para determinar em qual direção seguir.
# • Uma função/método para identificar a rota e navegar de volta para casa a partir da
# localização atual.
# • Uma função/método para testar se o objetivo desejado foi alcançado ou não.

from services.RobotActions import RobotActions

class RobotVacuumCleaner(RobotActions):
    
    staticEnvironment = [
        {"Location": "A", "Status": "Clean", "index": 0},{"Location": "B", "Status": "Dirty", "index": 1}, {"Location": "C", "Status": "Clean", "index": 2}, {"Location": "D", "Status": "Dirty", "index": 3},
        {"Location": "A", "Status": "Clean", "index": 4},{"Location": "B", "Status": "Dirty", "index": 5}, {"Location": "C", "Status": "Clean", "index": 6}, {"Location": "D", "Status": "Dirty", "index": 7},
        {"Location": "A", "Status": "Clean", "index": 8},{"Location": "B", "Status": "Dirty", "index": 9}, {"Location": "C", "Status": "Clean", "index": 10}, {"Location": "D", "Status": "Dirty", "index":11},
        {"Location": "A", "Status": "Clean", "index": 12},{"Location": "B", "Status": "Dirty", "index": 13}, {"Location": "C", "Status": "Clean", "index": 14}, {"Location": "D", "Status": "Dirty", "index": 15}
    ]

    #currentLocation = int(staticEnvironment[0]['index'])
    currentLocation = 15

    energy = 100

    def __init__(self):
        #self.showEnvironment()
        pass

    def showEnvironment(self):
        # for square in self.staticEnvironment:
        #     print(square)
        #print(self.currentLocation)
        pass
    
    def actionToDo(self, action, direction = None):
        if action == "Move":
            print(f"Move to: {direction}")
            self.currentLocation = self.move(direction, self.currentLocation)
        else: 
            pass


robot = RobotVacuumCleaner()
robot.actionToDo("Move", "Right")