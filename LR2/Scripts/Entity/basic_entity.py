from LR2.Interfaces.Interfaces import IUserPotion
from LR2.Scripts.Effect.effect import Effect
from LR2.Scripts.Items.Potion import Potion
from LR2.Scripts.strategy import *
from LR2.Utils.Utils import strike_through


class Being():
    def __init__(self, name):
        self._MAX_MANA = 0
        self._MAX_HEALTH = 0

        self._name = name
        self._level = 1
        self._health = self._MAX_HEALTH
        self._mana = self._MAX_MANA

        self._effect = Effect("empty")

        self.life_cycle_tick = self._effect.use_effect()
    def get_name(self): return self._name
    def fullup_HMP(self):
        self._health = self._MAX_HEALTH
        self._mana = self._MAX_MANA
    def get_damage(self, damage:float):
        if self._health - round(self._health - damage,3) <= 0:
            self._health = 0
        else:
            self._health = round(self._health - damage,3)
        pass
    def get_health(self, health:float):
        self._health += health
    def set_effect(self, effect:Effect):
        self._effect = effect
    def life_cycle_tick(self):
        pass
    def is_life(self):
        return self._health > 0
class Boss(Being, IUserPotion):
    def __init__(self,name, behaviour = None, strategy: Strategy = None):
        super().__init__(name)
        self._behaviour = behaviour
        self._strategy = strategy

        self._MAX_HEALTH = strategy.stat_value.get_MAX_HEALTH()
        self._MAX_MANA = strategy.stat_value.get_MAX_MANA()
        self._list_skills = strategy.stat_value.get_list_skills()
        self._damage = strategy.stat_value.get_base_damage()

        super().fullup_HMP()

    def use_attack(self, enemy):
        print(f"{self._name} | Босс яростно пронзает своим рыком {enemy.get_name()} | {enemy.__class__.__name__.lower()} и наносит ему {self._damage} урона")
        enemy.get_damage(self._damage)
    def use_potion(self, potion:Potion):
        self._effect
    def ShowInformation(self):
        print(f"  БОСС : {self._name} \n"
                f" Уровень : {self._level} \n"
                f"Здоровье : {self._health} \n"
                f"    Мана : {self._mana} \n"
                f"------Фаза------ \n"
                f"    Обычная\n"

                )
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
        if (self.is_life()):
            return (f"  Герой номер {self._number} \n"
                f"     Имя : {self._name} \n"
                f"   Класс : {self.__class__.__name__.lower()} \n"
                f" Уровень : {self._level} \n"
                f"Здоровье : {self._health} \n"
                f"    Мана : {self._mana} \n"
                f"------Атрибуты------ \n"
                f"  Ловкость : {self._agility} \n"
                f"      Сила : {self._strength} \n"
                f" Интеллект : {self._intellect} \n \n")
        else:
            hero_number = strike_through(f"  Герой номер {self._number}")
            return (f"{hero_number}\n"
                    f"     Имя : {self._name} \n"
                    f"   Класс : {self.__class__.__name__.lower()} \n"
                    f"Здоровье : Мертв \n")


