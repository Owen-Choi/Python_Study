class calcClass:

    def __init__(self, first, second):
        self.setdata(first, second)

    def setdata(self, first, second):
        self.fisrt = first
        self.second = second

    def add(self):
        return self.fisrt + self.second

# calcClass를 상속하는 moreCalcClass
class moreCalcClass(calcClass):
    def pow(self):
        return self.fisrt ** self.second

a = calcClass(10, 20)
#a.setdata(10,20)
print(a.add())

b = moreCalcClass(10,2)
print(b.pow())