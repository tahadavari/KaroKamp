# public
# protected
# private
import csv


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Driver(Person):
    def __init__(self, first_name, last_name, avatar="", national_code="0000000"):
        super().__init__(first_name, last_name)

        self.avatar = avatar
        self.national_code = national_code

    def set_first_name(self, first_name):
        self.first_name = first_name

    def get_first_name(self):
        return self._first_name

    def get_name(self):
        print(self._first_name + " " + self.last_name)


class Passenger(Person):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)


class Trip:
    def __init__(self, src, dst, passenger: Passenger, driver: Driver):
        self.src = src
        self.dst = dst
        self.passenger: Passenger = passenger
        self.driver: Driver = driver

    def __str__(self):
        return f"{self.src} {self.dst} {self.passenger}"


drivers = []
with open('drivers_data.csv', mode='r') as file:
    csv_file = csv.reader(file)
    for line in csv_file:
        driver = Driver(line[0], line[1])
        drivers.append(driver)

for driver in drivers:
    print(driver)
passenger = Passenger("negin", "f")
trip1 = Trip("France", "Tehran", passenger, drivers[1])
print(trip1.passenger.last_name)
