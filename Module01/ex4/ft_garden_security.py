#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str,
                 height: float, age: int, growth_rate: float = 0.8) -> None:
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
            print(f"Height updated: {int(height)}cm")

    def set_age(self, age: int) -> None:
        if age < 0:
            print(f"{self.name}: Error, age can't be negative")
        else:
            self._age = age
            print(f"Age updated: {age} days")

    def show(self) -> None:
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self) -> None:
        self._height = round(self._height + self.growth_rate, 1)

    def age_one_day(self) -> None:
        self._age += 1


if __name__ == "__main__":
    print("=== Garden Security System ===")
    rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()
    print()

    rose.set_height(25.0)
    rose.set_age(30)
    print()

    rose.set_height(-10.0)
    print("Height update rejected")
    rose.set_age(-5)
    print("Age update rejected")
    print()

    print("Current state: ", end="")
    rose.show()
