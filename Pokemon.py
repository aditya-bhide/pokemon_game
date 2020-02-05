class Attack:
    def __init__(self):
        self.name = None
        self.damage = None


class Pokemon:
    def __init__(self):
        self.name = 'Pokemon1'
        self.type = 'Fire'
        self.damage_levels = [(1, 100), (20, 80), (30, 70), (45, 55)]
        self.attacks = []
        self.HP = 400
        self.MP = 400

    def show_specs(self):
        print('Name:', self.name)
        print('Type:', self.type)
        self.show_attacks()

    def show_attacks(self):
        print('Attacks:')
        for i, j in enumerate(self.attacks):
            print('\t', str(i+1)+'.', j.name, ':', j.damage)

