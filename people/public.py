from people import human


class Public(human.Human):
    def __init__(self):
        super().__init__()


class Policemen(Public):
    def __init__(self):
        super().__init__()
        self.name = 'Policeman'
        self.health = 120
        self.usual_damage = 20


class Mafia(Public):
    def __init__(self):
        super().__init__()
        self.name = 'Mafia'
        self.health = 200
        self.usual_damage = 10


class StreetWalkers(Public):
    def __init__(self):
        super().__init__()
        self.name = 'Street Walker'
        self.health = 35
        self.usual_damage = 1
