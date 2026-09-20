class Vehicle:
    def __init__(self, speed:float, starting_position:float=0.0):
        self.position: float = starting_position
        self.speed = speed

    def move(self, magnitude:float, direction:int):
        "direction:int -> 1: \"forwards\" or -1: \"backwards\""

        if direction not in (1, -1):
            raise ValueError("\"direction\" must be 1 or -1")

        self.position += direction * self.speed * magnitude

    def __repr__(self) -> str:
        return f"Position: {self.position}"

class Car(Vehicle):
    def __init__(self, speed:float, fuel_capacity:float, starting_fuel:float, fuel_eff:float, starting_position:float=0):
        "starting fuel is a value between 0 and fuel_capacity (inclusive), fuel_eff is a value between 0 and 1 (exclusive)"
        super().__init__(speed, starting_position) # performs the __init__() function of the parent class

        if fuel_capacity <= 0:
            raise ValueError("fuel_capcity must be greater than 0")
        self.fuel_capacity = fuel_capacity

        if starting_fuel < 0 or starting_fuel > fuel_capacity:
            raise ValueError("starting_fuel must be between 0-fuel_capacity (inclusive)")
        self.fuel_amt = starting_fuel

        if fuel_eff >= 1 or fuel_eff <= 0:
            raise ValueError("fuel_eff must be between 0-1 (exclusive)")
        self.fuel_eff = fuel_eff

    def move(self, magnitude:float, direction:int):
        "direction:int -> 1: \"forwards\" or -1: \"backwards\""

        if self.fuel_amt <= 0.0:
            print("Cannot move - no fuel remaining :(")

        fuel_consumpt = magnitude - (magnitude * self.fuel_eff)
        if fuel_consumpt > self.fuel_amt:
            print("Ran out of fuel!")

            remaining_magnitude = self.fuel_amt/(1 - self.fuel_eff)
            super().move(remaining_magnitude, direction)

            self.fuel_amt = 0.0

        else:
            super().move(magnitude, direction)
            self.fuel_amt -= fuel_consumpt

    def refuel(self, refuel_amt:float):
        self.fuel_amt = min(self.fuel_capacity, self.fuel_amt + refuel_amt)

    def __repr__(self) -> str:
        return super().__repr__() + f", Fuel Remaining: {self.fuel_amt}"

my_car = Car(10, 100, 100, 0.7)
my_car.move(10,1)
print(my_car)

my_car.refuel(50)
print(my_car)