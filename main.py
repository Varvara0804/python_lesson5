import random
import time




class Cat:
    def __init__(self, name, playfulness, energy, hunger):
        self.name = name
        self.playfulness = playfulness
        self.energy = energy
        self.hunger = hunger
        print(f"__________________________________________")
        print(f"Новое животное - кошка '{self.name}'")
        print(f"Характер '{self.playfulness}'")
        print(f"Энергия '{self.energy}'")
        print(f"Голод '{self.hunger}'")
        print(f"__________________________________________")

    def change_playfulness(self, new_playfulness):
        self.playfulness = new_playfulness
        print(f"__________________________________________")
        print(f"Вы играете с кошкой '{self.name}'")
        print(f"Игра завершена")
        print(f"Кошка теперь '{self.playfulness}'")
        print(f"__________________________________________")


    def change_hunger(self, new_hunger):
        self.hunger = new_hunger
        print(f"__________________________________________")
        print(f"Вы кормите кошку '{self.name}'")
        print(f"Кошка наелась")
        print(f"Голод понизился до '{self.hunger}'")
        print(f"__________________________________________")



class Dragon:
    def __init__(self, name, color, movement, aggression):
        self.name = name
        self.color = color
        self.movement = movement
        self.aggression = aggression
        print(f"__________________________________________")
        print(f"прилетело существо - дракон '{self.name}'")
        print(f"Он имеет цвет '{self.color}'")
        print(f"Он передвигается '{self.movement}'")
        print(f"Характер '{self.aggression}'")
        print(f"__________________________________________")

    def change_color(self, new_color):
        self.color = new_color
        print(f"__________________________________________")
        print(f"Вы случайно ударили дракона")
        print(f"Он стал '{self.color}'")
        print(f"__________________________________________")



    def aggression_increase(self):
        print(f"__________________________________________")
        print(f"Вы разозлили дракона '{self.name}'")
        while self.aggression < 100:
            print(f"Злость дракона '{self.name}' ({self.aggression})")
            self.aggression = self.aggression + random.randrange(15)
            time.sleep(0.3)
        print(f"Злость достигла 100%, вы испепелены")

animal1 = Cat("Муся", "игривая", 60, 40)
animal2 = Dragon("Григорий", "зелёный", "полёт", 20)


animal1.change_playfulness("устала")
animal1.change_hunger(0)
animal2.change_color("фиолетовый в крапинку")
animal2.aggression_increase()
