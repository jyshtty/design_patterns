from abc import ABC, abstractmethod

class ComputerBuilder(ABC):

    @abstractmethod
    def set_ram(self, ram):
        self.ram = ram
    
    @abstractmethod
    def set_cpu(self, cpu):
        self.cpu = cpu
    
    @abstractmethod
    def set_gpu(self, gpu):
        self.gpu = gpu
    
    @abstractmethod
    def set_power_supply(self, power_supply):
        self.power_supply = power_supply
    
    @abstractmethod
    def set_storage(self, storage):
        self.storage = storage


