class Animal:
    def __init__(self, name):
        self.alive = True
        self.fed = False
        self.name = name

    def __repr__(self):
        return f"Animal(name={self.name}, alive={self.alive}, fed={self.fed})"


class Plant:
    def __init__(self, name):
        self.edible = False
        self.name = name

    def __repr__(self):
        return f"Plant(name={self.name}, edible={self.edible})"


class Mammal(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{food.name} не является растением")


class Predator(Animal):
    def eat(self, food):
        if isinstance(food, Plant):
            if food.edible:
                print(f"{self.name} съел {food.name}")
                self.fed = True
            else:
                print(f"{self.name} не стал есть {food.name}")
                self.alive = False
        else:
            print(f"{food.name} не является растением")


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False  # Цветок по умолчанию несъедобен


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Фрукты по умолчанию съедобны


# Проверка

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)
