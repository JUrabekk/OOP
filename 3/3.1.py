class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates
    def get_proteins(self):
        return self.proteins
    def get_fats(self):
        return self.fats
    def get_carbohydrates(self):
        return self.carbohydrates
    def get_kcalories(self):
        return 4 * self.proteins + 9 * self.fats + 4 * self.carbohydrates
    def __add__(self, other):
        new_proteins = self.proteins + other.proteins
        new_fats = self.fats + other.fats
        new_carbohydrates = self.carbohydrates + other.carbohydrates
        return FoodInfo(new_proteins, new_fats, new_carbohydrates)
food1 = FoodInfo(100, 100, 100)
food2 = FoodInfo(50, 60, 70)
food3 = food1 + food2
print(food1.get_proteins(), food1.get_fats(), food1.get_carbohydrates(), food1.get_kcalories())
print(food2.get_proteins(), food2.get_fats(), food2.get_carbohydrates(), food2.get_kcalories())
print(food3.get_proteins(), food3.get_fats(), food3.get_carbohydrates(), food3.get_kcalories())
