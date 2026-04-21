#!/usr/bin/env python3

class Plant:
    class _Stats:
            def __init__(self) -> None:
                self._grow_count: int = 0
                self._age_count: int = 0
                self._show_count: int = 0

            def record_grow(self) -> None:
                self._grow_count += 1

            def record_age(self) -> None:
                self._age_count += 1

            def record_show(self) -> None:
                self._show_count += 1

            def display(self) -> None:
                print(
                    f"Stats: {self._grow_count} grow, "
                    f"{self._age_count} age, {self._show_count} show"
                )

    def __init__(
        self, name: str, height: float, age: int, growth_rate: float = 0.8
    ) -> None:
        self.name = name
        self.growth_rate = growth_rate
        self._height: float = 0.0
        self._age: int = 0
        self._stats = Plant._Stats()
        self.set_height(height)
        self.set_age(age)

    @staticmethod
    def is_older_than_a_year(age: int) -> bool:
        return age > 365

    @classmethod
    def create_anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

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
        self._stats.record_show()
        print(f"{self.name}: {self._height}cm, {self._age} days old")

    def grow(self) -> None:
        self._stats.record_grow()
        self._height = round(self._height + self.growth_rate, 1)

    def age_one_day(self) -> None:
        self._stats.record_age()
        self._age += 1

    def get_stats(self) -> "_Stats":  # type: ignore[name-defined]
        return self._stats


class Flower(Plant):
    def __init__(
        self, name: str, height: float, age: int,
        color: str, growth_rate: float = 0.8
    ) -> None:
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
    class _TreeStats(Plant._Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade_count: int = 0

        def record_shade(self) -> None:
            self._shade_count += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade_count} shade")

    def __init__(
        self, name: str, height: float, age: int,
        trunk_diameter: float, growth_rate: float = 0.2
    ) -> None:
        super().__init__(name, height, age, growth_rate)
        self.trunk_diameter = trunk_diameter
        self._stats = Tree._TreeStats()

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        if isinstance(self._stats, Tree._TreeStats):
            self._stats.record_shade()
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height}cm long and {self.trunk_diameter}cm wide."
        )


class Seed(Flower):
    def __init__(
        self, name: str, height: float, age: int,
        color: str, growth_rate: float = 0.8
    ) -> None:
        super().__init__(name, height, age, color, growth_rate)
        self.seed_count: int = 0

    def bloom(self, seed_count: int = 0) -> None:
        super().bloom()
        self.seed_count = seed_count

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self.seed_count}")

    def grow(self) -> None:
        super().grow()

    def age_one_day(self) -> None:
        super().age_one_day()


class Vegetable(Plant):
    def __init__(
        self, name: str, height: float, age: int,
        harvest_season: str, growth_rate: float = 2.1
    ) -> None:
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

    def display_plant_statistics(plant: Plant) -> None:
        print(f"[statistics for {plant.name}]")
        plant.get_stats().display()


if __name__ == "__main__":
    print("=== Garden statistics ===")

    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.is_older_than_a_year(30)}")
    print(f"Is 400 days more than a year? -> {Plant.is_older_than_a_year(400)}")

    print()
    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    display_plant_statistics(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow()
    rose.bloom()
    rose.show()
    display_plant_statistics(rose)

    print()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    display_plant_statistics(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_plant_statistics(oak)

    print()
    print("=== Seed")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow()
    sunflower.age_one_day()
    sunflower.bloom(seed_count=42)
    sunflower.show()
    display_plant_statistics(sunflower)

    print()
    print("=== Anonymous")
    # classmethod creates a plant without knowing its details.
    anon = Plant.create_anonymous()
    anon.show()
    display_plant_statistics(anon)