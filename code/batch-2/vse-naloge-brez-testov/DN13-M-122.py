
class Minobot:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = 'R'
        self.directions = 'RDLU' #"URDL"
        self.moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        self.idirection = int(self.directions.index(self.direction))

    def naprej(self, d):

        dx, dy = self.moves[self.idirection]
        self.x += dx * d
        self.y += dy * d

    def desno(self):
        self.direction = self.directions[(self.idirection + 1) % 4]
        self.moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        self.idirection = int(self.directions.index(self.direction))

    def levo(self):
        self.direction = self.directions[(self.idirection - 1) % 4]
        self.moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        self.idirection = int(self.directions.index(self.direction))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def koordinate(self):
        return self.get_x(), self.get_y()

    def razdalja(self):
        return abs(self.get_x()) + abs(self.get_y())

