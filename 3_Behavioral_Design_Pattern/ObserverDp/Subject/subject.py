class Subject():
    def __init__(self):
        self.observers = []


    def register(self, observer):
        self.observers.append(observer)
    
    def unregister(self, observer):
        self.observers.remove(observer)
    
    def notify(self, hum, temp):
        for observer in self.observers:
            observer.update(hum, temp)

