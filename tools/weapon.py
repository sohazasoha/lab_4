from tools import tool


class Weapon(tool.Tool):
    damage = 0
    speed = 0
    num_bullets = 0

    def __init__(self):
        super().__init__()
        self.type = 'weapon'

    def __repr__(self):
        return '{0} '.format(" ".join([self.name]))

    def getting_text(self):
        return (f'Weapon: {0}, Damage: {1}, Shoot speed: {2}, '
                f'Number of bullets: {3}', self.name, self.damage,
                self.speed, self.num_bullets)


class Gun(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'Gun'
        self.damage = 15
        self.speed = 2
        self.num_bullets = 32


class Knife(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'Knife'
        self.damage = 7
        self.speed = 4
        self.num_bullets = 1


class SniperRifle(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'Sniper Rifle'
        self.damage = 70
        self.speed = 1
        self.num_bullets = 8


class MachinePistol(Weapon):
    def __init__(self):
        super().__init__()
        self.name = 'Machine Pistol'
        self.damage = 10
        self.speed = 10
        self.num_bullets = 124
