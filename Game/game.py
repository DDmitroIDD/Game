"""
The main executable file in which the gameplay starts
"""

import names

import Modul.Game.settings as settings
from Modul.Game.exceptions import GameOver, EnemyDown, InvalidLiteral
from Modul.Game.models import Player, Enemy, Scores



def play():
    """
    Input player names, input commands for settings game and create player object and enemy object.

    :return: Result of game
    """
    level = 1
    player_name = input('Please enter your name ')
    print(f"  Welcome to the game \"RPS\" {player_name}\n"
          f"_________________________________________\n")
    player = Player(player_name)
    enemy_name = names.get_first_name(gender='male')
    enemy = Enemy(enemy_name, level)

    while True:
        command = input(f"{player_name}, Please enter \"START\" to start the game\n"
                        "or enter \"HELP\" to show any commands ")

        if command.lower() == "start":
            print(f'Your enemy name is {enemy_name}!')

            try:

                player.allowed_attack = input('Please make a choice for attack: '
                                              '\'1\' - Wizard, \'2\' - Warrior,'
                                              ' \'3\' - Rogue ')
                player.attack(enemy)
                print(f'Your lives: {player.lives} | {enemy_name} lives: {enemy.lives}\n')
                player.allowed_attack = input('Please make a choice for defence: '
                                              '\'1\' - Wizard, \'2\' - Warrior,'
                                              ' \'3\' - Rogue ')
                player.defence(enemy)
                print(f'Your lives: {player.lives} | {enemy_name} lives: {enemy.lives}\n')
            except EnemyDown:
                player.score += 5
                player.level += 1
                level += 1
                print(f'\n********************************************\n'
                      f' You killed {enemy_name}. Your score: '
                      f'{player.score}. Level: {player.level}.\n'
                      f'********************************************\n')
                enemy_name = names.get_first_name(gender='male')
                enemy = Enemy(enemy_name, level)
                print(f'\nYour enemy name is {enemy_name}!\n')
            except InvalidLiteral:
                print('\nThere is no lizard and Spock in this game\n')

        if command.lower() == "show scores":
            print('\n')
            Scores.show_score()
            print('\n')

        if command.lower() == "help":
            print(f'\nAllowed commands: {", ".join(settings.ALLOWED_COMMANDS)}.\n')

        if command.lower() == "exit":
            raise KeyboardInterrupt


if __name__ == '__main__':
    try:
        play()
    except GameOver:
        print('GAME OVER')
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye')
