
class Strategy():
    def __init__(self,number_strategy:int):
        self.stat_value = None
        match number_strategy:
            case 1:
                self.stat_value = ValuesTypeStrategy(
                    300,
                    200,
                    [1,2,3],
                    35,
                    20
                )
            case 2:
                self.stat_value = ValuesTypeStrategy(
                    3000,
                    20,
                    [3,1,2],
                    10,
                    50
                )

class ValuesTypeStrategy():
    def __init__(self,MAX_HEALTH, MAX_MANA,list_skills, base_damage,up_damage):
        self._MAX_HEALTH = MAX_HEALTH
        self._MAX_MANA = MAX_MANA
        self._list_skills = list_skills
        self._base_damage = base_damage
        self._up_damage = up_damage
    def get_MAX_HEALTH(self):
        return self._MAX_HEALTH
    def get_MAX_MANA(self):
        return self._MAX_MANA
    def get_list_skills(self):
        return self._list_skills
    def get_base_damage(self):
        return self._base_damage
    def get_up_damage(self):
        return self._up_damage
