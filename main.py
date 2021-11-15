import random
import string
from collections import defaultdict

class VehicleInfo:
    brand: str
    catalogue_price = int
    electric = bool

    def __init__(self, brand, model, catalogue_prize, electric):
        self.brand = brand
        self.model = model
        self.catalogue_price = catalogue_prize
        self.electric = electric

    def compute_tax(self):
        tax_rate = 0.19
        if self.electric:
            tax_rate = 0.05
        return tax_rate * self.catalogue_price

    def print_vehicle_info(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Catalogue prize : {self.catalogue_price}")
        print(f"Due tax: {self.compute_tax()}")


class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, id, license_plate, vehicle_info):
        self.id = id
        self.license_plate = license_plate
        self.vehicle_info = vehicle_info

    def print_vehicle(self):
        print(f"ID : {self.id}")
        print(f"License plate : {self.license_plate}")
        self.vehicle_info.print_vehicle_info()


class VehicleRegistry:
    vehicle_info = defaultdict(dict)

    def add_vehicle_info(self, brand, model, catalogue_price, electric):
        self.vehicle_info[brand][model] = VehicleInfo(brand, model, catalogue_price, electric)

    def __init__(self):
        self.add_vehicle_info("Tesla", "Model 3", 60000, True)
        self.add_vehicle_info("BMW", "5", 80000, False)
        self.add_vehicle_info("Porsche", "911", 100000, False)
        self.add_vehicle_info("Volkswagen", "ID3", 45000, True)

    def generate_vehicle_id(self, length=12):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_license_plate(self, id):
        return f"{id[:2]} - {''.join(random.choices(string.digits, k=2))} - {''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand, model):
        vehicle_id = self.generate_vehicle_id()
        vehicle_license_plate = self.generate_license_plate(vehicle_id)
        return Vehicle(vehicle_id, vehicle_license_plate, self.vehicle_info[brand][model])


class Application:

    def register_vehicle(self, brand: str, model: str):
        registry = VehicleRegistry()
        return registry.create_vehicle(brand, model)


if __name__ == '__main__':
    app = Application()
    vehicle = app.register_vehicle("Tesla", "Model 3")
    vehicle.print_vehicle()
