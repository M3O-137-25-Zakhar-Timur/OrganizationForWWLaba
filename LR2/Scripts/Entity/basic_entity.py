import random

from LR2.Interfaces.Interfaces import IUserPotion
from LR2.Scripts.Effect.effect import Effect, Effect_Empty, Effect_Heal, Effect_ManaExp
from LR2.Scripts.Items.Potion import Potion
from LR2.Scripts.strategy import *
from LR2.Utils.Utils import strike_through, create_progress_bar


class Being():
    def __init__(self, name):
        self._MAX_MANA = 0
        self._MAX_HEALTH = 0

        self._name = name
        self._level = 1
        self._health = self._MAX_HEALTH
        self._mana = self._MAX_MANA

        self._effects: [Effect] = [Effect_Heal(1), Effect_ManaExp(1)]
    def get_name(self): return self._name
    def fullup_HMP(self):
        self._health = self._MAX_HEALTH
        self._mana = self._MAX_MANA
    def get_damage(self, damage:float, origin = None):
        if self._health - round(self._health - damage,3) <= 0:
            self._health = 0
        else:
            self._health = round(self._health - damage,3)
        if origin != None:
            print(f"--({self._name} : {self.__class__.__name__}) получает {damage} урона от ({origin._name} : {origin.__class__.__name__})--")
        else:
            print(f"--({self._name} : {self.__class__.__name__}) получает {damage} урона--")

    def get_health(self, health:float, origin = None):
        if self.is_life():
            self._health += health
            if self._health > self._MAX_HEALTH: self._health = self._MAX_HEALTH
            if origin != None:
                print(f"--({self._name} : {self.__class__.__name__}) получает {health} здоровья от ({origin._name} : {origin.__class__.__name__})--")
            else:
                print(f"--({self._name} : {self.__class__.__name__}) получает {health} здоровья--")

    def get_mana(self, mana: float, origin = None):
        self._mana += mana
        if self._mana > self._MAX_MANA: self._mana = self._MAX_MANA
        if origin != None:
            print(f"--({self._name} : {self.__class__.__name__}) получает {mana} маны от ({origin._name} : {origin.__class__.__name__})--")
        else:
            print(f"--({self._name} : {self.__class__.__name__}) получает {mana} маны--")

    def set_effect(self, effect:Effect):
        self._effect = effect
    def life_cycle_tick(self):
        new_effects = []
        for effect in self._effects:
            new_effects.append(effect.use_effect(self))
        self._effects = new_effects
        if all(effect.__class__ == Effect_Empty for effect in new_effects):
            self._effects = []
        self.get_mana(20)
    def is_life(self):
        return self._health > 0
    def spend_mana(self, mana):
        self._mana -= mana

    def show_info_effects(self):
        str_effects = ", ".join([effect.get_name_effect() for effect in self._effects])
        if len(self._effects) == 0 or str_effects == "":
            return "Нет эффектов"
        return str_effects
class Boss(Being, IUserPotion):
    def __init__(self,name, behaviour = None, strategy: Strategy = None, team_level = 1):
        super().__init__(name)
        self._behaviour = behaviour
        self._strategy = strategy

        self._MAX_HEALTH = strategy.stat_value.get_MAX_HEALTH()
        self._MAX_MANA = strategy.stat_value.get_MAX_MANA()
        self._list_skills = strategy.stat_value.get_list_skills()
        self._base_damage = strategy.stat_value.get_base_damage()
        self._damage = self._base_damage * (0.8 + team_level * 0.2)  # Масштабирование под уровень команды
        super().fullup_HMP()

    def use_attack(self, enemy):
        actual_damage = self._damage * (0.8 + random.random() * 0.4)  # Случайный разброс 80%-120%
        print(f"({self._name} | {self.__class__.__name__}) : яростно атакует ({enemy.get_name()}) и наносит {actual_damage} урона")
        enemy.get_damage(actual_damage, self)
        return actual_damage
    def use_potion(self, potion:Potion):
        self._effect
    def life_cycle_tick(self):
        new_effects = []
        for effect in self._effects:
            new_effects.append(effect.use_effect(self))
        self._effects = new_effects
        if all(effect.__class__ == Effect_Empty for effect in new_effects):
            self._effects = []
        self.update_strategy()
    def up_damage(self, damage):
        self._damage += damage
        print(F"({self._name} | {self.__class__.__name__}) сменил свою фазу : увеличивает свой урон на {damage}!")
    def update_strategy(self):
        if self._health <= self._MAX_HEALTH * 0.2:
            self.up_damage(self._strategy.stat_value.get_up_damage() * 1.3)
        elif self._health <= self._MAX_HEALTH * 0.5:
            self.up_damage(self._strategy.stat_value.get_up_damage())


    def ShowInformation(self):
        health_bar = create_progress_bar(self._health, self._MAX_HEALTH)
        mana_bar = create_progress_bar(self._mana, self._MAX_MANA, True)

        print(f"┌─ БОСС ─────────────────────────────────┐\n"
              f"│  Имя: {self._name:<15} \n"
              f"│  Уровень: {self._level:<15} \n"
              f"│  Здоровье: {health_bar:<15} \n"
              f"│  Мана: {mana_bar:<15} \n"
              f"│  Урон: {self._damage:<15} ⚔  \n"
              f"│  Фаза: Обычная {'':<15} \n"
              f"│  Текущие эффекты: {self.show_info_effects()}\n"
              f"└────────────────────────────────────────┘")
    def IsLife(self):
        if self._health > 0:
            return True
        return False
class Character(Being, IUserPotion):
    def __init__(self,name, number):
        self._number = number
        self._strength = 0
        self._agility = 0
        self._intellect = 0
        self._damage = 0
        super().__init__(name)

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
                    f"│  Урон атаки: {0} \n"
                    f"│  Сила способности: {0} \n"
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



