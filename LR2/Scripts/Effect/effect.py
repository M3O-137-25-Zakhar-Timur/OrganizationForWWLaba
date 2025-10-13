

class Effect():
    def __init__(self, duration:int):
        self._name = ""
        self._duration = duration
    def use_effect(self, char):
        pass
    def get_name_effect(self): return self._name

class Effect_Empty(Effect):
    def __init__(self, duration = 0):
        self._name = ""
        self._duration = duration
    def use_effect(self, char):
        return self

class Effect_Heal(Effect):
    def __init__(self, duration):
        self._name = "HEAL"
        self._duration = duration

    def use_effect(self, char):
        char.get_health(30, self)
        self._duration -= 1

        return self if self._duration > 0 else Effect_Empty()


class Effect_ManaExp(Effect):
    def __init__(self, duration):
        self._name = "MANA"
        self._duration = duration

    def use_effect(self, char):
        if self._duration <= 0:
            return Effect_Empty()

        char.get_mana(30,self)
        self._duration -= 1

        return self if self._duration > 0 else Effect_Empty()
