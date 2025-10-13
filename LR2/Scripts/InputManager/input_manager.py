from LR2.Interfaces.Interfaces import IAttacker, ISkillUser
from LR2.Scripts.Entity.basic_entity import Character
from LR2.Scripts.Types.types import TypeVerifyInput, TypeActionsCharacters
from LR2.Scripts.command.command import Command


class InputManager():
    def __init__(self, team: Command):
        self.team = team

    def _print_header(self, text):
        print(f"\n{'═' * 50}")
        print(f"🎯 {text}")
        print(f"{'═' * 50}")

    def _print_success(self, text):
        print(f"✅ {text}")

    def _print_error(self, text):
        print(f"❌ {text}")

    def _print_warning(self, text):
        print(f"⚠️  {text}")

    def _print_info(self, text):
        print(f"💡 {text}")

    def InputCharPick(self):
        while True:
            self.team.ShowInfoTeam()
            self._print_header("ВЫБОР ПЕРСОНАЖА")
            print("🎮 Доступные персонажи:")
            for i in range(1, len(self.team.GetTeam()) + 1):
                print(f"   {i}️⃣  Герой #{i}")

            self._print_info(f"Выберите персонажа для хода (1-{len(self.team.GetTeam())}):")

            try:
                input_pick = int(input("📝 Ваш выбор: "))

                if input_pick in self.team.GetLengthTeam():
                    self._print_success(f"Выбран персонаж #{input_pick}")
                    return input_pick
                else:
                    self._print_error("Персонажа с таким номером не существует!")

            except ValueError:
                self._print_error("Пожалуйста, введите число!")
            except Exception:
                self._print_error("Ошибка ввода!")

    def VerifyPick(self):
        while True:
            self._print_header("ПОДТВЕРЖДЕНИЕ ВЫБОРА")
            print("🔄 Варианты подтверждения:")
            print("   🟢 'y' - Да, подтвердить")
            print("   🔴 'n' - Нет, отменить")
            print("   🟡 'off' - Отключить подтверждение")

            verify_input = input("📝 Ваш выбор (y/n/off): ").lower()

            if verify_input == "y":
                self._print_success("Выбор подтвержден!")
                return TypeVerifyInput.yes
            elif verify_input == "n":
                self._print_warning("Выбор отменен!")
                return TypeVerifyInput.no
            elif verify_input == "off":
                self._print_info("Подтверждение выбора отключено")
                return TypeVerifyInput.off_verify
            else:
                self._print_error("Неверный ввод! Пожалуйста, используйте y, n или off")

    def PrintCanAtions(self, can_attack, can_spell):
        self._print_header("ДОСТУПНЫЕ ДЕЙСТВИЯ")

        if not can_attack and not can_spell:
            self._print_warning("Этот персонаж не может атаковать или использовать заклинания!")
            return None

        actions = []
        if can_attack:
            actions.append("⚔️  АТАКА (A)")
        if can_spell:
            actions.append("🔮 ЗАКЛИНАНИЕ (S)")

        print("🎮 Доступные действия:")
        for action in actions:
            print(f"   {action}")

    def InputAttack(self, teammate: Character):
        while True:
            can_attack = issubclass(teammate.__class__, IAttacker)
            can_spell = issubclass(teammate.__class__, ISkillUser) and teammate.can_use_skill()

            self.PrintCanAtions(can_attack, can_spell)

            if not can_attack and not can_spell:
                self._print_warning("Персонаж не может совершать действий")
                return TypeActionsCharacters.ReturnPick

            try:
                self._print_info("Выберите действие:")

                if can_attack and can_spell:
                    input_attack = input("📝 Ваш выбор (A/S): ").upper()
                elif can_attack:
                    input_attack = input("📝 Ваш выбор (A): ").upper()
                else:
                    input_attack = input("📝 Ваш выбор (S): ").upper()

                if can_attack and (input_attack == "A" or input_attack == "А"):
                    self._print_success("Выбрана атака! ⚔️")
                    return TypeActionsCharacters.Attack
                elif can_spell and input_attack == "S":
                    self._print_success("Выбрано заклинание! 🔮")
                    return TypeActionsCharacters.Spell
                else:
                    self._print_error("Неверная команда!")

            except Exception:
                self._print_error("Ошибка ввода!")