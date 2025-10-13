from LR2.Interfaces.Interfaces import IUserPotion, ISkillUser, IAttacker
from LR2.Scripts.Entity.basic_entity import *
from LR2.Scripts.command.command import Command


class Warrior(Character, ISkillUser, IAttacker,IUserPotion):
    def __init__(self, name,number):
        super().__init__(name,number)
        self._MAX_HEALTH = 150
        self._MAX_MANA = 60
        self._health = self._MAX_HEALTH
        self._mana = self._MAX_MANA
        self._strength = 8
        self._agility = 2
        self._intellect = 1

        self._mana_cost = 20
        self._damage = 15 + self._strength * 2
        self._shield_damage = 25 + self._strength * 3

    def use_skill(self, enemy: Boss, team: Command = None):
        if self.can_use_skill():
            heal_amount = 15 + self._strength * 0.5
            print(
                f"({self._name} | {self.__class__.__name__}) : Активирует щит, наносит {self._shield_damage} урона ({enemy.get_name()} | {enemy.__class__.__name__}) и лечит себя на {heal_amount}")

            self.spend_mana(self._mana_cost)
            self.get_health(heal_amount)
            enemy.get_damage(self._shield_damage, self)
            return self._shield_damage
    def can_use_skill(self): return self._mana - self._mana_cost >= 0

    def attack(self, enemy:Boss):
        print(f"({self._name} | {self.__class__.__name__}) : Пронзает своим мечом ({enemy.get_name()} | {enemy.__class__.__name__}) и наноcит ему {self._damage} урона")
        enemy.get_damage(self._damage)
        return self._damage if self._damage != None else 0
    def use_potion(self, potion:Potion):
        pass
    def ShowInformation(self):
        if self.is_life():
            # Создаем прогресс-бары для здоровья и маны
            health_bar = create_progress_bar(self._health, self._MAX_HEALTH)
            mana_bar = create_progress_bar(self._mana, self._MAX_MANA, True)

            return (f"┌─ ГЕРОЙ #{self._number} ──────────────────────┐\n"
                    f"│  Имя: {self._name:<20} \n"
                    f"│  Класс: {self.__class__.__name__:<20} \n"
                    f"│  Уровень: {self._level:<20} \n"
                    f"│  Здоровье: {health_bar:<20} \n"
                    f"│  Мана: {mana_bar} \n"
                    f"│  Урон атаки: {self._damage} \n"
                    f"│  Сила способности: {self._shield_damage} | {self._mana_cost} MP \n"
                    f"│  Текущие эффекты: {self.show_info_effects()} \n"
                    f"├─ АТРИБУТЫ ───────────────────────────────────┤\n"
                    f"   Сила      : {self._strength:<5} 🔥\n"
                    f"   Ловкость  : {self._agility:<5} 🏹\n"
                    f"   Интеллект : {self._intellect:<5} 🧠\n"
                    f"└──────────────────────────────────────────────┘\n")
        else:
            return (f"┌─ ГЕРОЙ #{self._number} ──────────────────────┐\n"
                    f"│  Имя: {self._name:<28} \n"
                    f"│  Класс: {self.__class__.__name__:<25} \n"
                    f"│  💀 МЕРТВ {'':<23} \n"
                    f"└──────────────────────────────────────────────┘\n")

class Mage(Character,ISkillUser, IUserPotion, IAttacker):
    def __init__(self,name,number):
        super().__init__(name,number)
        self._MAX_HEALTH = 120
        self._MAX_MANA = 250
        self._health = self._MAX_HEALTH
        self._mana = self._MAX_MANA
        self._strength = 1
        self._agility = 2
        self._intellect = 10

        self._main_heal = 20

        self._mana_cost = 10
        self._attack_damage = 10 + self._intellect * 1.5  # ~25 урона
        self._skill_damage = 15 + self._intellect * 2  # ~35 урона

    def attack(self, enemy: Boss):
        print(
            f"({self._name} | {self.__class__.__name__}) : Бросает магический снаряд и наносит {self._attack_damage} урона ({enemy.get_name()} | {enemy.__class__.__name__})")
        enemy.get_damage(self._attack_damage, self)
        return self._attack_damage  if self._attack_damage != None else 0
    def use_skill(self, enemy: Boss, team: Command = None):
        if self.can_use_skill():
            print(
                f"({self._name} | {self.__class__.__name__}) : Выпускает огненный шар, наносит {self._skill_damage} урона ({enemy.get_name()} | {enemy.__class__.__name__}) и лечит себя на {self._main_heal}")

            self.spend_mana(self._mana_cost)
            self.get_health(self._main_heal)
            enemy.get_damage(self._skill_damage, self)
            return self._skill_damage
    def can_use_skill(self): return self._mana - self._mana_cost >= 0

    def use_potion(self, potion:Potion):
        pass
    def ShowInformation(self):
        if self.is_life():
            # Создаем прогресс-бары для здоровья и маны
            health_bar = create_progress_bar(self._health, self._MAX_HEALTH)
            mana_bar = create_progress_bar(self._mana, self._MAX_MANA, True)

            return (f"┌─ ГЕРОЙ #{self._number} ──────────────────────┐\n"
                    f"│  Имя: {self._name:<20} \n"
                    f"│  Класс: {self.__class__.__name__:<20} \n"
                    f"│  Уровень: {self._level:<20} \n"
                    f"│  Здоровье: {health_bar:<20} \n"
                    f"│  Мана: {mana_bar} \n"
                    f"│  Урон атаки: {self._attack_damage} \n"
                    f"│  Сила способности: {self._skill_damage} | {self._mana_cost} MP \n"
                    f"│  Текущие эффекты: {self.show_info_effects()} \n"
                    f"├─ АТРИБУТЫ ───────────────────────────────────┤\n"
                    f"   Сила      : {self._strength:<5} 🔥\n"
                    f"   Ловкость  : {self._agility:<5} 🏹\n"
                    f"   Интеллект : {self._intellect:<5} 🧠\n"
                    f"└──────────────────────────────────────────────┘\n")
        else:
            return (f"┌─ ГЕРОЙ #{self._number} ──────────────────────┐\n"
                    f"│  Имя: {self._name:<28} \n"
                    f"│  Класс: {self.__class__.__name__:<25} \n"
                    f"│  💀 МЕРТВ {'':<23} \n"
                    f"└──────────────────────────────────────────────┘\n")

class Healer(Character, ISkillUser,IUserPotion):
    def __init__(self,name,number):
        super().__init__(name,number)
        self._MAX_HEALTH = 130
        self._MAX_MANA = 200
        self._health = self._MAX_HEALTH
        self._mana = self._MAX_MANA
        self._strength = 6
        self._agility = 1
        self._intellect = 7

        self._mana_cost = 20
        self._heal = (self._intellect + self._agility + self._strength) * 2
        self.potion = Potion("dispel")

    def use_skill(self, enemy: Boss, team: Command):
        if self.can_use_skill():
            print(f"({self._name} | {self.__class__.__name__}) : Дарует своим союзникам {self._heal} здоровья!")

            self.spend_mana(self._mana_cost)
            for teammate in team.GetTeam():
                teammate.get_health(self._heal)

    def can_use_skill(self): return self._mana - self._mana_cost >= 0

    def use_potion(self, potion:Potion):
        pass
    def ShowInformation(self):
        if self.is_life():
            # Создаем прогресс-бары для здоровья и маны
            health_bar = create_progress_bar(self._health, self._MAX_HEALTH)
            mana_bar = create_progress_bar(self._mana, self._MAX_MANA, True)

            return (f"┌─ ГЕРОЙ #{self._number} ──────────────────────┐\n"
                    f"│  Имя: {self._name:<20} \n"
                    f"│  Класс: {self.__class__.__name__:<20} \n"
                    f"│  Уровень: {self._level:<20} \n"
                    f"│  Здоровье: {health_bar:<20} \n"
                    f"│  Мана: {mana_bar} \n"
                    f"│  Сила исцеления: {self._heal} | {self._mana_cost} MP\n"
                    f"│  Текущие эффекты: {self.show_info_effects()} \n"
                    f"├─ АТРИБУТЫ ───────────────────────────────────┤\n"
                    f"   Сила      : {self._strength:<5} 🔥\n"
                    f"   Ловкость  : {self._agility:<5} 🏹\n"
                    f"   Интеллект : {self._intellect:<5} 🧠\n"
                    f"└──────────────────────────────────────────────┘\n")
        else:
            return (f"┌─ ГЕРОЙ #{self._number} ──────────────────────┐\n"
                    f"│  Имя: {self._name:<28} \n"
                    f"│  Класс: {self.__class__.__name__:<25} \n"
                    f"│  💀 МЕРТВ {'':<23} \n"
                    f"└──────────────────────────────────────────────┘\n")
