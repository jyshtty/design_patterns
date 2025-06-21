# Ensure that only one instance of a class is created throughout the program, no matter how many times you try to instantiate it.

# __new__ is a special method in Python used to create a new instance (before __init__ is called).




class Singleton:
    _is_instance = None

    def __new__(cls):
        if cls._is_instance is None:
            cls._is_instance = super().__new__(cls)

        return cls._is_instance
    
obj1 = Singleton()
obj2 = Singleton()

print(obj1 == obj2)

