from Arena import Arena
from IPython.display import clear_output
arena = Arena()
while True:
    print('''
        1. Create pokemon
        2. Show Existing pokemon
        3. Battle
        4. Quit
    ''')
    choice = int(input('Enter your choice:'))
    if choice == 1:
        arena.create_pokemon()
    elif choice == 2:
        arena.show_all()
        pass
    elif choice == 3:
        clear_output()
        arena.battle()
        pass
    else:
        break