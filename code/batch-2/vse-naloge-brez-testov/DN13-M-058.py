class Minobot:
    def __init__(self):
        self.x, self.y = 0, 0
        self.direction = "E"

    def levo(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "E"
        else:
            self.direction = "N"

    def desno(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        else:
            self.direction = "N"

    def naprej(self, d):
        if self.direction == "N":
            self.y += d
        elif self.direction == "E":
            self.x += d
        elif self.direction == "S":
            self.y -= d
        else:
            self.x -= d

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)


