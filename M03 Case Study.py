# Author: Adrian Melchi
# Description: The purpose of this app is to get user input to save and display information about their vehicle.
# App Name: Vehicle Information

class Vehicle: # Super class to hold vehicle type
    def __init__(self, vehicleType):
        self.vehicle_type = vehicleType

class Auto(Vehicle): # Auto class, also locks choice to car only
    def __init__(self, year, make, model, doors, roof):
        super().__init__('car')  
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
   
    def display_info(self): # Display information to be shown at the end
        print("Vehicle type:"+ self.vehicle_type)
        print("Year:" + self.year)
        print("Make:" + self.make)
        print("Model:" + self.model)
        print("Number of doors:" + self.doors)
        print("Type of roof:" + self.roof)

def create_car(): # Information about car stored for later output
    year = input("Enter the year of the car:")
    make = input("Enter the make of the car:")
    model = input("Enter the model of the car:")
    doors = input("Enter the number of doors (2 or 4):")
    roof = input("Enter the type of roof (solid or sun roof):")

    car = Auto(year, make, model, doors, roof)
    return car

def main(): # main function to run program
    car = create_car()
    car.display_info()

if __name__ == "__main__":
    main()