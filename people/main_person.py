from people import human


class MainPerson(human.Human):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.health = 60
        self.usual_damage = 4

    def __repr__(self):
        return 'Main Person: {}, Status: {}, Health: {}, Items: {}'.format(
            self.name, self.status, self.health, self.items)
