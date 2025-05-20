from abc import ABC, abstractmethod

class Observer(ABC):
    
    @abstractmethod
    def update(self, temp, humidity):
        pass

    def subscribeToSubject(self, subject):
        subject.register(self)

    def unsubscribeToSubject(self, subject):
        subject.unregister(self)
