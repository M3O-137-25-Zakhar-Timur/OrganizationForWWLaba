from LR2.Interfaces.Interfaces import ISkillUser, IAttacker
from LR2.Scripts.Entity.basic_entity import Character, Boss
from LR2.Scripts.command.command import Command
import os

def clear_console():
    # Для Windows
    if os.name == 'nt':
        os.system('cls')
    # Для Linux/Mac
    else:
        os.system('clear')
import enum
class TypeActionsCharachers(enum.Enum):
    Attack = 0
    Spell = 1
class TypeVerifyInput(enum.Enum):
    yes = 0
    no = 1
    off_verify = 2

class InputManager():
   def __init__(self, team: Command):
       self.team = team
   def InputCharPick(self):
       while(True):
           clear_console()
           self.team.ShowInfoTeam()
           print(f"Выберите каким персонажем будете делать ход!\n"
                 f"(нажмите 1-{len(self.team.GetTeam())})")
           try:
               input_pick = int(input())

               if input_pick in self.team.GetLengthTeam():
                   return input_pick
               else:
                   print("Такого персонажа нет !")
           except:
               print("Такого персонажа нет !")
               continue
   def VerifyPick(self):
       while(True):
           print("Нажмите на y/n для подтверждения действия."
                 "(напишите off для отключения валидации выбора персонажа :3)")
           verify_input = input()
           if verify_input == "y":
               return TypeVerifyInput.yes
           elif verify_input == "n":
               return TypeVerifyInput.no
           elif verify_input == "off":
               return  TypeVerifyInput.off_verify
           else:
               print("Вы написали что-то не то...")
               continue
   def PrintCanAtions(self, can_attack, can_spell):
       if not can_attack and not can_spell:
           print("Этот персонаж не может атаковать или использовать заклинания!")
           return None
       if can_attack:
           print("Нанесите удар!")
           print("Напишите A")

       if can_attack and can_spell:
           print("--------------")

       if can_spell:
           print("Примените заклинание!")
           print("Напишите S")

   def InputAttack(self, teammate: Character):
       while True:
           can_attack = issubclass(teammate.__class__, IAttacker)
           can_spell = issubclass(teammate.__class__, ISkillUser)

           self.PrintCanAtions(can_attack,can_spell)

           try:
               input_attack = input().upper()

               if can_attack and (input_attack == "A" or input_attack == "А"):
                   return TypeActionsCharachers.Attack
               elif can_spell and input_attack == "S":
                   return TypeActionsCharachers.Spell
               else:
                   print("Ты написал что-то не то!!!")

           except:
               print("Ты написал что-то не то!!!")

class Battle():
    def __init__(self,team: Command, enemy:Boss):
        self._inputManager: InputManager = InputManager(team)
        self._pickChar: Character = None
        self._is_verify_on = True
        self._enemy = enemy
        self._team = team
        self._count_iteration = 0
        self._count_use_attack = 0
        self._count_use_spell = 0
    def ShowInfoAboutBattle(self):
        print(f"Характеристика боя: \n"
              f"Количество ходов : {self._count_iteration}")
    def Iteration(self):
        self._enemy.ShowInformation()
        while (True):
            pickCharIndex = self._inputManager.InputCharPick()
            pickChar = self._team.GetTeam()[pickCharIndex-1]
            print(F"Вы выбрали - {pickChar.get_name()}")
            self._count_iteration += 1
            if self._is_verify_on:
                print(F"Вы уверены в выборе?")
                verifyPick = self._inputManager.VerifyPick()
                if verifyPick == TypeVerifyInput.yes:
                    print(f"ВЫ будете сражаться за {pickChar.get_name()}")
                    break
                elif verifyPick == TypeVerifyInput.no:
                    continue
                elif verifyPick == TypeVerifyInput.off_verify:
                    self._is_verify_on = False
                    print("валидация отключена!")
                    break
            else:
                break

        state_attack = self._inputManager.InputAttack(pickChar)
        if state_attack == TypeActionsCharachers.Spell:
            pickChar.use_skill(self._enemy, self._team)
            self._count_use_spell += 1
        elif state_attack == TypeActionsCharachers.Attack:
            pickChar.attack(self._enemy)
            self._count_use_attack += 1

        self._enemy.use_attack(pickChar)








