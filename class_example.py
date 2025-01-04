class AnimalParty:
    def __init__(self):
        self.x = 0
        print("I'm a constructor", self.x)

    def party(self):
        self.x += 1
        print("so far: ", self.x)

    def __del__(self):
        print("I'm a destructor", self.x)

an = AnimalParty()

an.party()
an.party()
an.party()