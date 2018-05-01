from math import fabs

class Minobot:
    def __init__(self):
        self.position = (0,0)
        self.direction = 1
        self.prev_actions = []
    
    def naprej(self, d):
        self.prev_actions.append((self.position, self.direction))
        switch = {0: lambda pos: (pos[0], pos[1] + d),
                    1: lambda pos: (pos[0] + d, pos[1]),
                    2: lambda pos: (pos[0], pos[1] - d),
                    3: lambda pos: (pos[0] - d, pos[1])
                    }
        self.position = switch[self.direction % 4](self.position)

    def desno(self):
        self.prev_actions.append((self.position, self.direction))
        self.direction = (self.direction + 1) % 4

    def levo(self):
        self.prev_actions.append((self.position, self.direction))
        self.direction = (self.direction - 1) % 4

    def koordinate(self):
        return self.position

    def razdalja(self):
        return fabs(self.position[0]) + fabs(self.position[1])

    def razveljavi(self):
        if len(self.prev_actions):
            self.position, self.direction = self.prev_actions[-1][0], self.prev_actions[-1][1]
            self.prev_actions.pop()

