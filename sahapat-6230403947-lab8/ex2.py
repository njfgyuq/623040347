class Vehicle:
    def __init__(self, name, speed, mileage):
        self.name = name
        self.__speed = speed
        self.mileage = mileage

    def set_speed(self, new_speed):
        self.__speed = new_speed

    def __str__(self):
        return f'Name: {self.name} speed: {self.__speed} ' \
               f'mileage: {self.mileage}'


class Car(Vehicle):
    def __init__(self, name, speed, mileage, num_door):
        self.num_door = num_door
        super().__init__(name, speed, mileage)

    def __str__(self):
        return f'{Vehicle.__str__(self)} num doors: {self.num_door}'


class Bus(Vehicle):
    def __init__(self, name, speed, mileage, capacity):
        self.capacity = capacity
        super().__init__(name, speed, mileage)

    def __str__(self):
        return f'{Vehicle.__str__(self)} capacity: {self.capacity}'


if __name__ == '__main__':
    car = Car("Toyota Vios", 90, 150000, 4)
    bus = Bus("School Volvo", 12, 200000, 100)
    print(car)
    print(bus)
    bus.set_speed(30)
    print(bus)
