import string
import random


class VehicleRegistry:

    @staticmethod
    def generate_vehicle_id(length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    @staticmethod
    def generate_vehicle_license(vehicle_id):
        return f"{vehicle_id[:2]}-{''.join(random.choices(string.digits, k=2))}-" \
               f"{''.join(random.choices(string.ascii_uppercase, k=2))}"


class Application:

    @staticmethod
    def register_vehicle(brand: string):
        # create a registry instance
        registry = VehicleRegistry()

        # generate a vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id(12)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        license_plate = registry.generate_vehicle_license(vehicle_id)

        # compute the catalogue price
        catalogue_price = 0
        if brand == "Tesla Model 3":
            catalogue_price = 60000
        elif brand == "Volkswagen ID3":
            catalogue_price = 35000
        elif brand == "BMW X5":
            catalogue_price = 45000
        elif brand == 'Benz':
            catalogue_price = 500000

        # compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        # compute the payable tax
        payable_tax = tax_percentage * catalogue_price

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        print(f"Id: {vehicle_id}")
        print(f"License plate: {license_plate}")
        print(f"Payable tax: {payable_tax}")


if __name__ == '__main__':
    Application.register_vehicle("BMW X5")
