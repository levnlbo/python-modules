#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int, growth_rate: float = 0.8) -> None:
        self.name = name
        self.growth_rate = growth_rate
        self._height: float = 0.0
        self._age: int = 0
        self.set_height(height)
        self.set_age(age)
 
    def get_height(self) -> float:
        return self._height
 
    def get_age(self) -> int:
        return self._age
 
    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self.name}: Error, height can't be negative")
        else:
            self._height = height
 
    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
        else:
            self._age = age
 
    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")
 
    def grow(self) -> None:
        self._height = round(self._height + self.growth_rate, 1)
 
    def age_one_day(self) -> None:
        self._age += 1

class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str, growth_rate: float = 0.8) -> None:
        super().__init__(name, height, age, growth_rate)
        self.color = color
        self._blooming: bool = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._blooming:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")

    def bloom(self) -> None:
        self._blooming = True

class Tree(Plant):
    def __init__(self, name: str, height: float, age: int, trunk_diameter: float, growth_rate: float = 0.2) -> None:
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter
 
    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")
 
    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height}cm long and {self.trunk_diameter}cm wide."
        )
 
 
class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int, harvest_season: str, growth_rate: float = 2.1) -> None:
        super().__init__(name, height, age, growth_rate)
        self.harvest_season = harvest_season
        self.nutritional_value: int = 0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season}")
        print(f" Nutritional value: {self.nutritional_value}")

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1
 
    def age_one_day(self) -> None:
        super().age_one_day()
        self.nutritional_value += 1

if __name__ == "__main__":
    print("=== Garden Plant Types ===")
 
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
 
    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
 
    print()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow()
        tomato.age_one_day()
    tomato.show()