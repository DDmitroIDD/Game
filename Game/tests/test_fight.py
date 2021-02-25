import unittest

from Modul.Game.models import Player, Enemy
from Modul.Game.settings import ALLOWED_MOVES


class FightTest(unittest.TestCase):

    def test_number(self):
        requests = [Player.fight(1, 1), Player.fight(1, 2), Player.fight(1, 3), Player.fight(2, 1), Player.fight(2, 2),
                    Player.fight(2, 3), Player.fight(3, 1), Player.fight(3, 2), Player.fight(3, 3), ]
        returns = [0, 1, -1, -1, 0, 1, 1, -1, 0]
        self.assertListEqual(requests, returns, )


class AttackEnemyTest(unittest.TestCase):

    def test_attack_enemy(self):
        self.assertIn(str(Enemy.select_attack()), ALLOWED_MOVES)


