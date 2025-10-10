from LR2.Scripts.Items.Item import *
from LR2.Scripts.Effect.effect import Effect


class Potion(Item):
    def __init__(self, effect:Effect):
        self._effect = effect
    def take_potion(self):
        return self._effect