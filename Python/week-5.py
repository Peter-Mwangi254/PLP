# Assignment 1: Design Your Own Class
class Avenger:
    def __init__(self, name, power, weapon):
        self.name = name
        self.power = power
        self.weapon = weapon

    def attack(self):
        print(f"{self.name} attacks using {self.weapon}!")

    def info(self):
        print(f"Name: {self.name}, Power: {self.power}, Weapon: {self.weapon}")


class IronMan(Avenger):
    def __init__(self, name="Iron Man", power="Genius-level intellect", weapon="Arc Reactor Suit"):
        super().__init__(name, power, weapon)

    def attack(self):
        print(f"{self.name} fires repulsor beams from his suit! 🔥")


class Thor(Avenger):
    def __init__(self, name="Thor", power="God of Thunder", weapon="Mjolnir"):
        super().__init__(name, power, weapon)

    def attack(self):
        print(f"{self.name} summons lightning with {self.weapon}! ⚡")


class CaptainAmerica(Avenger):
    def __init__(self, name="Captain America", power="Enhanced strength and agility", weapon="Vibranium Shield"):
        super().__init__(name, power, weapon)

    def attack(self):
        print(f"{self.name} throws his shield with precision! 🛡️")


# Activity 2: Polymorphism Challenge 🎭

class Vehicle:
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")