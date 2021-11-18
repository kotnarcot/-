class Table:
    def __init__(self, l = 1, w = 1, h = 1):
        self.length = l
        self.width = w
        self.height = h
    def sum(self):
        print(self.length*self.width*self.height*0.4)

class KitchenTable(Table):
    def __init__(self, l, w, h, n = 2):
        Table.__init__(self, l, w, h)
        self.namber = n
    def resalt(self):
        print(self.length*self.width*self.height*0.4*self.namber)

table1 = Table(125,65,200)
table1.sum()
table2 = KitchenTable(125,65,200,3)
table2.resalt()
# другой код но такого же формата 









class Table:
    def __init__(self, l=1, w=1, c=3):
        self.hg = l
        self.an = w
        self.cp = c
    def sum(self):
        print(self.hg*self.an-self.cp)

class Table2(Table):
    def __init__(self, k=1, s=1, r=1):
        self.tn = k
        self.na = s
        self.ia = r
    def sum(self):
        print(self.tn+self.na+self.ia)
#    def __init__(self,l=12, w=13, c=14, f = "зеленый"):
#        Table.__init__(self, l, w, c)
#       self.color = f

Table1 = Table(3,9,7)
Table1.sum()
Table3 = Table2(5,8,5)
Table3.sum()

#Table3 = Table2(12,11,10,"белый")
#print(Table3.hg)
