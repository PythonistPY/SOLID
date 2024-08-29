# from abc import ABC, abstractmethod
#
# class Weapon(ABC):
#     @abstractmethod
#     def attack(self):
#         pass
#
# class Sword(Weapon):
#     def __init__(self,attack):
#         self.attack()
#         print(f"Я атакую {attack}")
#
#
# class Bow(Weapon):
#     def __init__(self,attack):
#         self.attack()
#         print(f"Я атакую {attack}")
#
#
# class Fighter(Weapon):
#     def __init__(self,weapon):
#         pass
#
#
#
# class Monster():
#     def __init__(self):
#         pass
#
#
#
# fighter = Fighter
# monster = Monster
#

from abc import ABC, abstractmethod

# Шаг 1: Создание абстрактного класса для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализация конкретных типов оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Шаг 3: Модификация класса Fighter
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon is None:
            raise ValueError("Оружие не выбрано.")
        return self.weapon.attack()

# Класс Monster
class Monster:
    def __init__(self, name):
        self.name = name

    def is_defeated(self):
        return True

# Шаг 4: Реализация боя
def battle(fighter, monster):
    print(f"Боец выбирает {fighter.weapon.__class__.__name__.lower()}.")

    attack_message = fighter.attack()
    print(attack_message)

    if monster.is_defeated():
        print("Монстр побежден!")
    else:
        print("Монстр жив!")

# Пример использования
def main():
    fighter = Fighter("Артур")
    monster = Monster("Гоблин")

    # Боец выбирает меч
    fighter.change_weapon(Sword())
    battle(fighter, monster)

    print()

    # Боец выбирает лук
    fighter.change_weapon(Bow())
    battle(fighter, monster)

if __name__ == "__main__":
    main()
