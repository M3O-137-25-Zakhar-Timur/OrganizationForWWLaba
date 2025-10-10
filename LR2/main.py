
'''
абилки 
Воин - делает удар мега магический щитом, наносит 10 * сила + атака и восстанавливает 20 здоровья себе.

Лекарь - развеивает положительные эффекты с босса, лечит себя на 5 * интеллект

Маг - 

'''

from LR2.Interfaces.Interfaces import *
from LR2.Scripts.Entity.basic_entity import *
from LR2.Scripts.command.command import *
from LR2.Scripts.Entity.hero_classes import *
from LR2.Scripts.Battle.battle import Battle


team = Command()
boss = Boss("Габзабрик",None, Strategy(1))

war = Warrior("Дима",1)
mage = Mage("Толик",2)
healer = Healer("Маша",3)

team.AddClass(war)
team.AddClass(mage)
team.AddClass(healer)

battle_iteration = Battle(team, boss)

while boss.IsLife():
    battle_iteration.Iteration()

    if not(boss.IsLife()):
        print("ВЫ ПОБЕДИЛИ БОССА")
        battle_iteration.ShowInfoAboutBattle()


