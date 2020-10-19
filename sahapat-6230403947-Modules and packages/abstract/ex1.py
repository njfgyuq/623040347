from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, type):
        self.type = type


    @abstractmethod
    def move(self):
        pass


class Human(Animal):
    def __init__(self):
        super().__init__("Human")


    def move(self):
        print("I can walk and run")


class Snake(Animal):
    def __init__(self):
        super().__init__("Snake")


    def move(self):
        print("I can crawl")


class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")


    def move(self):
        print("I can bark")


if __name__ == '__main__':
    human = Human()
    human.move()
    snake = Snake()
    snake.move()
    dog = Dog()
    dog.move()
