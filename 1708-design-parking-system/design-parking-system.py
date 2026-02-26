from enum import Enum

class CarType(Enum):
    big = 1
    medium = 2
    small = 3

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        print(carType, CarType.big, self.big)
        if carType == CarType.big.value and self.big > 0:
            self.big -= 1
            return True
        elif carType == CarType.small.value and self.small > 0:
            self.small -= 1
            return True
        elif carType == CarType.medium.value and self.medium > 0:
            self.medium -= 1
            return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)