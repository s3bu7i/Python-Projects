class MinMax:
    def getList(self):
        self.lst = []
        for i in range(5):
            self.item = int(input("Enter number"))
            self.lst.append(self.item)
    
    def showList(self):
        print(self.lst)
    
    def minmax(self):
        print("Max = "+str(max(self.lst)))
        print("Min = "+str(min(self.lst)))

obj = MinMax()
obj.getList()
obj.showList()
obj.minmax()