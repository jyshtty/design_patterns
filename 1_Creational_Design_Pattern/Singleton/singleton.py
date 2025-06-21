# Ensure that only one instance of a class is created throughout the program, no matter how many times you try to instantiate it.




class Singleton:
    _is_instance = None

    def __new__(cls):
        if cls._is_instance is None:
            cls._is_instance = super().__new__(cls)

        return cls._is_instance
    
obj1 = Singleton()
obj2 = Singleton()

print(obj1 == obj2)

