"""
Contains the player, the enemy and the show scores table classes
"""
from random import randint

from Modul.Game.exceptions import EnemyDown, GameOver, InvalidLiteral
from Modul.Game.settings import DEFAULT_LIVES_COUNT, ALLOWED_MOVES


class Enemy:
    """
    The enemy class
    """

    lives = 1
    level = 1

    def __init__(self, name, level):
        """
        Construction the name and level of the enemy
        :param name: name enemy
        :param level: level enemy
        """
        self.name = name
        self.lives = level

    @staticmethod
    def select_attack():
        """
        Method for generate random int number
        :return: number from 1 to 3
        """
        return randint(1, 3)

    def decrease_lives(self, player_obj):
        """
        Method for decrease lives from enemy and add to player
        :param player_obj: player object
        :return: exception EnemyDown
        """
        self.lives -= 1
        if self.lives <= 0:
            self.level += 1
            raise EnemyDown
        player_obj.score += 1


class Player:
    """
    The player class
    """
    allowed_attack = 0
    score = 0
    lives = DEFAULT_LIVES_COUNT
    level = 1

    def __init__(self, name):
        """
        Construction the name player
        :param name: player name
        """
        self.name = name

    @staticmethod
    def fight(attack, defense):
        """
        :return result of round
        """
        if attack == defense:
            return 0
        if ((defense - attack) == 1) or ((attack - defense) == 2):
            return 1
        if ((defense - attack) == -1) or ((attack - defense) == -2):
            return -1

    def decrease_lives(self):
        """
        Method for decrease lives from player
        :return: exception Game over
        """
        self.lives -= 1
        if self.lives <= 0:
            GameOver.scores(self)
            raise GameOver

    def attack(self, enemy_obj):
        """
        Method for determining the result of a player's attack
        :param enemy_obj: Enemy object
        :return: message with result of attack
        """
        if self.allowed_attack in ALLOWED_MOVES:
            result = self.fight(int(self.allowed_attack), enemy_obj.select_attack())
            if result == 0:
                print("It's a draw!")
            elif result == 1:
                print("You attacked successfully!")
                Enemy.decrease_lives(enemy_obj, self)
            else:
                print("You missed!")
        else:
            raise InvalidLiteral

    def defence(self, enemy_obj):
        """
        Method for determining the result of a player's defence
        :param enemy_obj: Enemy object
        :return: message with result of defence
        """
        if self.allowed_attack in ALLOWED_MOVES:
            result = Player.fight(enemy_obj.select_attack(), int(self.allowed_attack))
            if result == 0:
                print("It's a draw!")

            elif result == 1:
                print("Enemy attacked successfully!")
                self.decrease_lives()
            else:
                print("Enemy missed!")
        else:
            raise InvalidLiteral


class Scores:
    """
    only ten the best players
    """

    @staticmethod
    def show_score():
        """
        Method for generate and print scores table
        :return: scores table
        """

        with open('scores.txt', 'r') as scores:
            scores = [i.split() for i in sorted(scores.readlines(), reverse=True)]
            scores_table = range(1, 11 if len(scores) > 10 else len(scores)+1)
            for i in zip(scores_table, scores):
                print(f'{i[0]}. {i[1][1]} : {i[1][0]} | {i[1][2]} {i[1][3]}')
