class Human:
    name = ''
    status = 'Life'
    health = 0
    usual_damage = 0
    items = None

    def fight(self, public):
        if public.status == 'Life':
            if self.items is not None:
                damage = self.items.damage
            else:
                damage = self.usual_damage
            public.health -= damage
            public.check()

    def check(self):
        if self.health <= 0:
            self.health = 0
            self.status = 'Death'

    def give_item(self, tool):
        self.items = tool

    def __repr__(self):
        return 'Human: {}, Status: {}, Health: {}'.format(
            self.name, self.status, self.health)
