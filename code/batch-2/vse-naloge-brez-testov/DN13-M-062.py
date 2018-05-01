class Minobot():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.pointing = "RIGHT"
        self.way_pairs_right = {
            "RIGHT":"DOWN",
            "DOWN": "LEFT",
            "LEFT":"UP",
            "UP":"RIGHT"
        }
        self.way_pairs_left = {
            "RIGHT":"UP",
            "DOWN": "RIGHT",
            "LEFT":"DOWN",
            "UP":"LEFT"
        }

    def naprej(self,d):
        if self.pointing == "RIGHT":
            self.x += d
        elif self.pointing == "LEFT":
            self.x -= d
        elif self.pointing == "UP":
            self.y += d
        elif self.pointing == "DOWN":
            self.y -= d


    def desno(self):
        self.pointing = self.way_pairs_right[self.pointing]


    def levo(self):
        self.pointing = self.way_pairs_left[self.pointing]

    def koordinate(self):
        return (self.x, self.y)

    def razdalja(self):
        return (abs(self.y)+abs(self.x))



