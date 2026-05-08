# parent class
class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name, "Age:", self.age)
        

# Subclass: Dog
class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def show_breed(self):
        print(self.name, "is a", self.breed, "dog.")


# Subclass: Cat         
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def show_color(self):
        print(self.name, "is a", self.color, "cat.")


# Example usage
dog1 = Dog("Buddy", 3, "Golden Retriever")
cat1 = Cat("Whiskers", 2, "Black")

dog1.show_info()
dog1.show_breed()

cat1.show_info()
cat1.show_color()