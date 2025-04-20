class Pro:
    def __init__(self, id):
        self.id = id
        self.act = True

class GFG:
    def __init__(self):
        self.TotalProcess = 0
        self.process = []

    def initialiseGFG(self):
        print("No of processes: 5")
        self.TotalProcess = 5
        self.process = [Pro(i) for i in range(self.TotalProcess)]

    def Election(self):
        print(f"Process no {self.process[self.FetchMaximum()].id} fails")
        self.process[self.FetchMaximum()].act = False

        print("Election Initiated by 2")
        initializedProcess = 2
        old = initializedProcess
        newer = (old + 1) % self.TotalProcess

        while True:
            if self.process[newer].act:
                print(f"Process {self.process[old].id} passes Election({self.process[old].id}) to {self.process[newer].id}")
                old = newer
            newer = (newer + 1) % self.TotalProcess
            if newer == initializedProcess:
                break

        newCoordinator = self.process[self.FetchMaximum()].id
        print(f"Process {newCoordinator} becomes coordinator")

        # Broadcasting coordinator info
        coord = newCoordinator
        old = coord
        newer = (old + 1) % self.TotalProcess

        while True:
            if self.process[newer].act:
                print(f"Process {old} passes Coordinator({coord}) message to process {self.process[newer].id}")
                old = newer
            newer = (newer + 1) % self.TotalProcess
            if newer == coord:
                print("End Of Election")
                break

    def FetchMaximum(self):
        maxId = -1
        ind = -1
        for i in range(self.TotalProcess):
            if self.process[i].act and self.process[i].id > maxId:
                maxId = self.process[i].id
                ind = i
        return ind

def main():
    obj = GFG()
    obj.initialiseGFG()
    obj.Election()

if __name__ == "__main__":
    main()

Conclusion:
# In a distributed system, election algorithms like Bully or Ring are used to elect a new coordinator. The process with the highest ID (in Bully) or the next active process in a logical ring (in Ring) takes over as the coordinator, ensuring a leader is always chosen even after failures.
