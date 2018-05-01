
class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'E'

        self.log = [(self.x, self.y, self.direction)]

    def update(self):
        self.log.append((self.x, self.y, self.direction))

    def naprej(self, d):
        if self.direction == 'N':
            self.y += d
        elif self.direction == 'E':
            self.x += d
        elif self.direction == 'S':
            self.y -= d
        else:
            self.x -= d

        self.update()

    def desno(self):
        directions = ['N', 'E', 'S', 'W']
        self.direction = directions[(directions.index(self.direction) + 1) % len(directions)]

        self.update()

    def levo(self):
        directions = ['N', 'E', 'S', 'W']
        self.direction = directions[(directions.index(self.direction) - 1) % len(directions)]

        self.update()

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def razveljavi(self):
        if len(self.log) != 1:
            self.log.pop()
            self.x = self.log[-1][0]
            self.y = self.log[-1][1]
            self.direction = self.log[-1][2]

