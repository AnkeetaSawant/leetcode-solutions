from enum import Enum

class CarType(Enum):
    big = 1
    medium = 2
    small = 3

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots = {
            CarType.big.value: big,
            CarType.medium.value: medium,
            CarType.small.value: small
        }

    def addCar(self, carType: int) -> bool:
        if self.slots[carType] > 0:
            self.slots[carType] -= 1
            return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)