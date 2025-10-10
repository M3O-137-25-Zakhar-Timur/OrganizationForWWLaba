class Effect():
    def __init__(self, duration:int):
        self._name_effect = ""
        self._duration = duration
    def use_effect(self):
        pass

class Effect_Empty(Effect):
    def __init__(self, duration):
        self._name_effect = "Нет эффектов"
        self._duration = duration
    def use_effect(self):
        def new_life_cycle(self):
            pass
        return new_life_cycle
class Effect_Heal(Effect):
    def __init__(self, duration):
        self._name_effect = "Эффект восстанавления здоровья"
        self._duration = duration
    def use_effect(self):
        def new_life_cycle(self):
            self._health += 30
            self.set_effect(Effect_Empty())
        return new_life_cycle
class Effect_ManaExp(Effect):
    def __init__(self, duration):
        self._name_effect = "Эффект восстанавления маны"
        self._duration = duration
    def use_effect(self):
        def new_life_cycle(self):
            self._mana += 30
            self.set_effect(Effect_Empty())
        return new_life_cycle
