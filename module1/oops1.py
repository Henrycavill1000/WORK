class Iphone:
    def __init__(self):
        self.model='model'
        self.ram='ram'
        self.storage='storage'
    def info(self):
        print('Iphone',self.model,'Info:')
        print('Model:',self.model)
        print('Ram:',self.ram)
        print('Storage:',self.storage)
        print('')
mob1=Iphone()
mob1.model=" 14 pro max"
mob1.ram='16GB'
mob1.storage='512GB'
mob1.info()

mob2=Iphone()
mob2.model=" 15 pro max"
mob2.ram='16GB'
mob2.storage='1TB'
mob2.info()