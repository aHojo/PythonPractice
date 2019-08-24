# import importlib
# importlib.reload(cars)


class Vehicle:

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def is_eco_friendly(self):
        if self.fuel == "gas":
            return False
        else:
            return True


class Car(Vehicle):

    def __init__(self, make, model, fuel="gas", number_of_wheels=4):
        super().__init__(make, model, fuel)
        self.number_of_wheels = number_of_wheels
