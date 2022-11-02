class Calculator:

    def add(self,a,b):
        return a + b
    def sub(self,a , b):
        return  a - b
# c = Calculator()
# print(c.add(2,3))
# print(c.sub(2,4))

c = Calculator()
assert c.add(1,2) == 3
assert c.sub(2,4) == 1
