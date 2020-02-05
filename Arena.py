from Player import Player
from Pokemon import Pokemon, Attack
import handlepickle as pkl
from IPython.display import clear_output
import random as rand
import time
import os
import copy


class Arena:
    def __init__(self):
        if os.path.exists('pokemons.pkl'):
            self.pokemons = pkl.read_pickle('pokemons.pkl')
        else:
            self.pokemons = []
        self.player1 = Player('Player1')
        self.player2 = Player('Player2')
        self.p1_turn = False
        self.battle_begin = False
        self.damage_p1 = 0
        self.damage_p2 = 0
        self.battle_init = False

    def create_pokemon(self):
        pok = Pokemon()
        pok.name = input('Enter pokemon name: ')
        pok.type = input('Enter pokemon type: ')
        for i in range(4):
            attack = Attack()
            attack.name = input('Enter the name of attack' + str(i) + ' for damage range ' + str(pok.damage_levels[i]))
            attack.damage = pok.damage_levels[i]
            pok.attacks.append(attack)
        self.pokemons.append(pok)
        pkl.pickler(self.pokemons, 'pokemons.pkl')
        print('Successful created: ')
        pok.show_specs()
        time.sleep(2)
        clear_output()

    def show_all(self):
        if len(self.pokemons) == 0:
            clear_output()
            print('Nothing to show')
            return
        print('\n\nExisting pokemons are:')
        for i, j in enumerate(self.pokemons):
            print('\n' + str(i + 1) + '.')
            j.show_specs()

        if not self.battle_init:
            select = int(input('Press:\n 1. Create new pokemon\n 2. Continue\n'))
            if select == 1:
                self.create_pokemon()
                time.sleep(1.5)
            elif select == 2:
                pass
            clear_output()

    def battle(self):
        self.battle_init = True
        if len(self.pokemons) == 0:
            print('Nothing to choose for pokemons. First create pokemon.')
            return
        self.choose_pokemons()
        self.fight()
        self.battle_init = False

    def set_emoji(self, damage):
        if damage > 80:
            return '\U0001F635'
        elif damage > 60:
            return '\U0001F630'
        elif damage > 40:
            return '\U0001F623'
        elif damage > 20:
            return '\U0001F628'
        elif damage > 0:
            return '\U0001F601'

    def battle_ui(self):
        clear_output()
        if not self.battle_begin:
            print('Player1 \t\t\t Player2')
            print(self.player1.pokemon.name, '\t\t\t', self.player2.pokemon.name)
            print('HP: ', self.player1.pokemon.HP, '\t\t\t', 'HP: ', self.player2.pokemon.HP)
            print('MP: ', self.player1.pokemon.MP, '\t\t\t', 'MP: ', self.player2.pokemon.MP)
            return
        else:
            if self.p1_turn:
                print('Player1 \t\t\t Player2')
                print(self.player1.pokemon.name, '\t\t\t', self.player2.pokemon.name, self.set_emoji(self.damage_p2))
                print('HP: ', self.player1.pokemon.HP, '\t\t\t', 'HP: ', self.player2.pokemon.HP, '   -',
                      self.damage_p2)
                print('MP: ', self.player1.pokemon.MP, '\t\t\t', 'MP: ', self.player2.pokemon.MP)
            else:
                print('Player1 \t\t\t Player2')
                print(self.player1.pokemon.name, self.set_emoji(self.damage_p1), '\t\t', self.player2.pokemon.name)
                print('HP: ', self.player1.pokemon.HP, '   -', self.damage_p1, '\t\t\t', 'HP: ',
                      self.player2.pokemon.HP)
                print('MP: ', self.player1.pokemon.MP, '\t\t\t', 'MP: ', self.player2.pokemon.MP)
        time.sleep(1.25)
        clear_output()
        print('Player1 \t\t\t Player2')
        print(self.player1.pokemon.name, '\t\t\t', self.player2.pokemon.name)
        print('HP: ', self.player1.pokemon.HP, '\t\t\t', 'HP: ', self.player2.pokemon.HP)
        print('MP: ', self.player1.pokemon.MP, '\t\t\t', 'MP: ', self.player2.pokemon.MP)

    def fight(self):
        self.p1_turn = rand.choices([True, False])
        if self.p1_turn:
            print('Player 1 attacks first')
        else:
            print('Player 2 attacks first')
        print("GET READY!!!")
        time.sleep(1.5)
        self.battle_ui()
        self.battle_begin = True
        while True:
            if self.p1_turn:
                self.player1.pokemon.show_attacks()
                select_attack = int(input("Select your attack player 1:"))
                self.damage_p2 = rand.randrange(self.player1.pokemon.attacks[select_attack - 1].damage[0],
                                                self.player1.pokemon.attacks[select_attack - 1].damage[1])
                self.player2.pokemon.HP -= self.damage_p2
                self.battle_ui()
                if self.player2.pokemon.HP <= 0:
                    print('Player 1 wins!!!')
                    break
                self.p1_turn = False

            if not self.p1_turn:
                self.player2.pokemon.show_attacks()
                select_attack = int(input("Select your attack player 2:"))
                self.damage_p1 = rand.randrange(self.player2.pokemon.attacks[select_attack - 1].damage[0],
                                                self.player2.pokemon.attacks[select_attack - 1].damage[1])
                self.player1.pokemon.HP -= self.damage_p1
                self.battle_ui()
                if self.player1.pokemon.HP <= 0:
                    print('Player 1 wins!!!')
                    break
                self.p1_turn = True
        self.battle_begin = True
        time.sleep(2)
        clear_output()

    def choose_pokemons(self):
        print('Player 1 choose your pokemon by number: ')
        self.show_all()
        select = int(input('I choose '))
        select -= 1
        self.player1.pokemon = copy.copy(self.pokemons[select])
        clear_output()
        print('Player 1 selected: ')
        self.player1.pokemon.show_specs()
        print('Player 2 choose your pokemon by number: ')
        self.show_all()
        select = int(input('I choose '))
        select -= 1
        self.player2.pokemon = copy.copy(self.pokemons[select])
        print('Player 2 selected: ')
        self.player2.pokemon.show_specs()
        clear_output()
