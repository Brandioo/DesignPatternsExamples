import string
import random


class VehicleInfo:

    def __init__(self, brand: str, catalogue_price: int, electric: bool):
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electric = electric

    def compute_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        payable_tax = tax_percentage * self.catalogue_price
        return payable_tax

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable Tax: {self.compute_tax()}")


class Vehicle:

    def __init__(self, vehicle_id: str, lisence_place: str, info: VehicleInfo):
        self.vehicle_id = vehicle_id
        self.lisence_plate = lisence_place
        self.info = info

    def print(self):
        print(f"ID: {self.vehicle_id}")
        print(f"Lisence Plate: {self.lisence_plate}")
        self.info.print()


class VehicleRegistry:
    vehicle_info = {}

    # In real life this info will be taken from the database
    def add_vehicle_info(self, brand, catalogue_price, electric):
        self.vehicle_info[brand] = VehicleInfo(brand, catalogue_price, electric)

    def __init__(self):
        self.add_vehicle_info(brand='Tesla Model 3', catalogue_price=60000, electric=True)
        self.add_vehicle_info(brand='Volkswagen ID3', catalogue_price=35000, electric=True)
        self.add_vehicle_info(brand='BMW X5', catalogue_price=45000, electric=False)

    @staticmethod
    def generate_vehicle_id(length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    @staticmethod
    def generate_vehicle_license(vehicle_id):
        return f"{vehicle_id[:2]}-{''.join(random.choices(string.digits, k=2))}-" \
               f"{''.join(random.choices(string.ascii_uppercase, k=2))}"

    def create_vehicle(self, brand):
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id=vehicle_id, lisence_place=license_plate, info=self.vehicle_info[brand])


class Application:

    @staticmethod
    def register_vehicle(brand: string):
        # create a registry instance
        registry = VehicleRegistry()

        return registry.create_vehicle(brand=brand)


if __name__ == '__main__':
    bmw_x5 = Application.register_vehicle("BMW X5")
    bmw_x5.print()
    print('\n')
    tesla_model_3 = Application.register_vehicle("Tesla Model 3")
    tesla_model_3.print()
