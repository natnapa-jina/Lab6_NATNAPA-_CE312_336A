#lab6 Ex1
class graph:
    def __init__(self):
        self.square = [[" "," "],[" "," "]]
    def create_edge(self,Node_name):
        temp = self.square[0]
        if self.square[0][-1] != " ":
            self.square[0].append(" ")
            Firstime = False
        else:
            Firstime = True
        check = 0
        if self.square[0][0] == " ":
            self.square[0][0] = "-"
        for i in range (len(self.square[0])):
            if i == len(self.square[0])- 1 and not Firstime:
                self.square.append([])
            while len(self.square[i]) < len(self.square[i-1]):
                self.square[i].append("0")
                if self.square[i][0] == "0":
                    self.square[i][0] = " "
        for i in range (len(self.square)):
            if self.square[0][i] == " " and check == 0:
                self.square[0][i] = Node_name
                check = 1
        for j in range (len(self.square[0])):
            if self.square[j][0] == " " and check == 1:
                self.square[j][0] = Node_name
                self.square[j][1] = "0"
                check = 0
    def AdjacencyMatrix(self):
        print(len(self.square) * "=")
        for i in range(len(self.square)):
            print(self.square[i])
    def connect(self,NodeA,NodeB):
        if NodeA in self.square[0] and NodeB in self.square[0] :
            NodeAIndex,NodeBIndex = 0,0
            for i in range(len(self.square)):
                if NodeA == self.square[0][i]:
                    NodeAIndex = i
                elif NodeB == self.square[0][i]:
                    NodeBIndex = i
            self.square[NodeAIndex][NodeBIndex] = "1"
            self.square[NodeBIndex][NodeAIndex] = "1"
        else:
            print ("Not")
    def AdjacencyList(self):
        tempList = [ ]
        for i in range(1,len(self.square)):
            tempList.append(str(self.square[i][0]) + ":")
            for j in range(1,len(self.square)):
                if self.square[i][j] == "1":
                    tempList.append(self.square[0][j])
            print(tempList)
            tempList=[]
    def EdgeList(self):
        tempList = [ ]
        memList = [ ]
        output = [[ ],[ ]]
        for i in range(1,len(self.square)):
            tempList.append(str(self.square[i][0]) + ":")
            memList.append(self.square[i][0])
            for j in range(1,len(self.square)):
                if self.square[i][j] == "1":
                    tempList.append(self.square[0][j])
                    memCheck = len(memList)
                    memList[memCheck-1] += self.square[0][j]
                    if j != (len(self.square) - 1):
                        memList.append(self.square[i][0])
                elif (j == (len(self.square) - 1) and self.square[i][j] == "0"):
                    memList.pop()
            tempList=[ ]
        Count = 0
        for i in range(len(memList)):
            Get = memList.pop(0)
            if Get[::-1] not in output[1]:
                output[0].append(str(Count) + ":")
                output[1].append(Get)
                Count += 1
        for i in range (len(output[0])):
            print(str(output[0][i]) + " " + str(output[1][i]))


g = graph()
g.create_edge("A")
g.create_edge("B")
g.create_edge("C")
g.create_edge("D")
g.connect("A","B")
g.connect("A","C")
g.connect("B","C")
g.connect("C","D")
g.AdjacencyMatrix()
print("\n")
g.AdjacencyList()
print("\n")
g.EdgeList()