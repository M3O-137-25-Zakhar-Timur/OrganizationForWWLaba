from LR2.Scripts.Entity.basic_entity import Character

class Command():
    def __init__(self):

        self._characters: list[Character] = []

    def AddClass(self, hero: Character):
        self._characters.append(hero)
    def GetLengthTeam(self):
        list_team = []
        for char in self._characters:
            if char.is_life():
                list_team.append(char._number)
        return list_team
    def GetTeam(self): return self._characters
    def ShowInfoTeam(self):
        if not self._characters:
            print("Команда пуста")
            return

        # Получаем информацию о всех героях в виде списков строк
        all_heroes_info = []
        for number, character in enumerate(self._characters, 1):
            hero_info = character.ShowInformation().split('\n')
            all_heroes_info.append(hero_info)

        # Определяем максимальное количество строк среди всех героев
        max_lines = max(len(hero_info) for hero_info in all_heroes_info)

        # Определяем ширину каждой колонки
        column_widths = []
        for hero_info in all_heroes_info:
            max_width = max(len(line) for line in hero_info) if hero_info else 0
            column_widths.append(max_width + 4)  # Добавляем отступ между колонками

        # Выводим все герои в строку
        for line_num in range(max_lines):
            line_parts = []
            for i, hero_info in enumerate(all_heroes_info):
                if line_num < len(hero_info):
                    line_part = hero_info[line_num].ljust(column_widths[i])
                else:
                    line_part = "".ljust(column_widths[i])
                line_parts.append(line_part)

            print("".join(line_parts))