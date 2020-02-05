class Player:
    def __init__(self, name):
        self.name = name
        self.pokemon = None

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return  self.name
