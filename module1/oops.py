class Vivomobile:
    def __init__(self):
        print('welcome')
    x=99
    def samplemethod(self):
        print(self.x)
    def samplemethod1(self):
        print("this is samplemethod1")
obj1=Vivomobile()
obj2=Vivomobile()
obj1.x=100
obj2.x=200
obj1.samplemethod()
obj1.samplemethod1()
Vivomobile.samplemethod(obj2)