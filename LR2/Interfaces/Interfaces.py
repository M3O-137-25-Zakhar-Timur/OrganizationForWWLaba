class ISkillUser():
    def use_skill(self,enemy, team):
        pass
    def can_use_skill(self):
        pass
class IAttacker():
    def attack(self,enemy):
        pass
class IUserPotion():
    def use_potion(self, potion):
        pass