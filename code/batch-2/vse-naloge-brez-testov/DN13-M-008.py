class Minobot:
    def __init__(self):
        self.smer = 90
        self.x = 0
        self.y = 0
        self.stack = []

    def naprej(self, d):
        if self.smer == 0:
            self.stack.append(("+y", d))
            self.y += d
        elif self.smer == 90:
            self.stack.append(("+x", d))
            self.x += d
        elif self.smer == 180:
            self.stack.append(("-y", d))
            self.y -= d
        else:
            self.stack.append(("+x", d))
            self.x -= d

    def desno(self):
        self.stack.append("desno")
        if self.smer == 270:
            self.smer = 0

        else:
            self.smer += 90

    def levo(self):
        self.stack.append("levo")
        if self.smer == 0:
            self.smer = 270

        else:
            self.smer -= 90

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def razveljavi(self):
        if not self.stack:
            return
        if self.stack[-1] == "levo":
            self.desno()
            self.stack.pop()
        if self.stack[-1] == "desno":
            self.levo()
            self.stack.pop()
        if self.stack[-1][0] == "+y":
            self.y -= self.stack[-1][1]
        if self.stack[-1][0] == "+x":
            self.x -= self.stack[-1][1]
        if self.stack[-1][0] == "-y":
            self.y += self.stack[-1][1]
        if self.stack[-1][0] == "-x":
            self.x += self.stack[-1][1]
        self.stack.pop()

