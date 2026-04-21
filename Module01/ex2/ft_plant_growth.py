#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int, growth_rate: float = 0.8) -> None:
        self.name = name
        self.height = height
        self.age = age
        self.growth_rate = growth_rate

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self) -> None:
        self.height = round(self.height + self.growth_rate, 1)

    def age_one_day(self) -> None:
        self.age += 1

if __name__ == "__main__":
    rose = Plant("Rose" , 25.0, 30)

    print("=== Garden Plant Growth ===")
    rose.show()

    start_height: float = rose.height
    for day in range(1, 8):
        rose.grow()
        rose.age_one_day()
        print(f"=== Day {day} ===")
        rose.show()
