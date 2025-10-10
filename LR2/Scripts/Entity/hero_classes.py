from LR2.Interfaces.Interfaces import IUserPotion, ISkillUser, IAttacker
from LR2.Scripts.Entity.basic_entity import *
from LR2.Scripts.command.command import Command


class Warrior(Character, ISkillUser, IAttacker,IUserPotion):
    def __init__(self, name,number):
        super().__init__(name,number)
        self._MAX_HEALTH = 150
        self._MAX_MANA = 50
        self._health = self._MAX_HEALTH
        self._mana = self._MAX_MANA
        self._strength = 8
        self._agility = 2
        self._intellect = 1

        self._damage = round((10 + self._strength * 0.5) * (self._strength * 0.2),3)
        self._shield_damage = round((10 * self._strength +  self._damage),3)
    def use_skill(self,enemy:Boss, team: Command = None):
        self.get_health(20)
        print(f"{self._name} | Воин : Активирует свой щит и наносит {enemy.get_name()} | Босс {self._shield_damage} урона и лечит себя на {20} здоровья")
        enemy.get_damage(self._shield_damage)
    def attack(self, enemy:Boss):
        print(f"{self._name} | Воин : Пронзает своим мечом {enemy.get_name()} | Босс и наноcит ему {self._damage} урона")
        enemy.get_damage(self._damage)
    def use_potion(self, potion:Potion):
        pass



class Mage(Character,ISkillUser, IUserPotion):
    def __init__(self,name,number):
        super().__init__(name,number)
        self._MAX_HEALTH = 70
        self._MAX_MANA = 250
        self._health = self._MAX_HEALTH
        self._mana = self._MAX_MANA
        self._strength = 1
        self._agility = 2
        self._intellect = 10

        self._main_heal = 20

        self._damage = round((10 * self._strength +  self._damage),3)
    def use_skill(self,enemy:Boss, team: Command = None):
        print(f"{self._name} | Маг : Наносит {enemy.get_name()} | Босс {self._damage} урона и лечит себя на {self._main_heal}")
        self.get_health(self._main_heal)
        enemy.get_damage(self._damage)
    def use_potion(self, potion:Potion):
        pass

class Healer(Character, ISkillUser,IUserPotion):
    def __init__(self,name,number):
        super().__init__(name,number)
        self._MAX_HEALTH = 99
        self._MAX_MANA = 200
        self._health = self._MAX_HEALTH
        self._mana = self._MAX_MANA
        self._strength = 6
        self._agility = 1
        self._intellect = 7

        self._heal = (self._intellect + self._agility + self._strength) * 2
        self.potion = Potion("dispel")

    def use_skill(self, enemy: Boss, team: Command):
        print(f"{self._name} | Лекарь : Дарует своим союзникам {self._heal} здоровья!")
        for teammate in team.GetTeam():
            teammate.get_health(self._heal)
    def use_potion(self, potion:Potion):
        pass
