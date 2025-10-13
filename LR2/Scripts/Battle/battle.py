from LR2.Interfaces.Interfaces import ISkillUser, IAttacker
from LR2.Scripts.Entity.basic_entity import Character, Boss
from LR2.Scripts.InputManager.input_manager import InputManager
from LR2.Scripts.Types.types import TypeVerifyInput, TypeActionsCharacters
from LR2.Scripts.command.command import Command
import os

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

        self._damage_dealt = 0
        self._damage_taken = 0

    def show_battle_stats(self):
        print(f"Статистика боя:")
        print(f"Нанесено урона: {self._damage_dealt}")
        print(f"Получено урона: {self._damage_taken}")
        print(f"Эффективность: {self._damage_dealt / max(1, self._damage_taken):.2f}")


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
        print("════════════════════Исход хода════════════════════")
        if state_attack == TypeActionsCharacters.Spell:
            damage_dealt = pickChar.use_skill(self._enemy, self._team)
            self._damage_dealt += damage_dealt if damage_dealt != None else 0
            self._count_use_spell += 1
        elif state_attack == TypeActionsCharacters.Attack:
            damage_dealt = pickChar.attack(self._enemy)
            self._damage_dealt += damage_dealt if damage_dealt != None else 0
            self._count_use_attack += 1
        elif state_attack == TypeActionsCharacters.ReturnPick:
            self.Iteration()
        self._damage_taken = self._enemy.use_attack(pickChar)
        self._team.Tick_Team()
        self._enemy.life_cycle_tick()
        print("══════════════════════════════════════════════════")
