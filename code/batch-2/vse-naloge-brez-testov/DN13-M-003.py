class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.orientacija = "desno"
        self.zgodovina = []

    def naprej(self, d):
        if self.orientacija == "desno":
            self.x += d
        if self.orientacija == "levo":
            self.x -= d
        if self.orientacija == "gor":
            self.y += d
        if self.orientacija == "dol":
            self.y -= d
        self.zgodovina.append(str(d))

    def desno(self ):
        usmeritve = ["desno", "dol", "levo", "gor"]
        i_usmeritev = usmeritve.index(self.orientacija)
        self.orientacija = usmeritve[(i_usmeritev + 1) % 4]
        self.zgodovina.append("desno")

    def levo(self):
        usmeritve = ["desno", "dol", "levo", "gor"]
        i_usmeritev = usmeritve.index(self.orientacija)
        self.orientacija = usmeritve[(i_usmeritev - 1) % 4]
        self.zgodovina.append("levo")

    def koordinate(self):
        return self.x, self.y

    def razdalja(self):
        manhatten = abs(self.x) + abs(self.y)
        return manhatten

    def zgodovina(self):
        return self.zgodovina

    def razveljavi(self):
        if self.zgodovina:
            if self.zgodovina[-1].isdigit():
                d = int(self.zgodovina[-1])
                if self.orientacija == "desno":
                    self.x -= d
                if self.orientacija == "levo":
                    self.x += d
                if self.orientacija == "gor":
                    self.y -= d
                if self.orientacija == "dol":
                    self.y += d
            if self.zgodovina[-1] == "desno":
                usmeritve = ["desno", "dol", "levo", "gor"]
                i_usmeritev = usmeritve.index(self.orientacija)
                self.orientacija = usmeritve[(i_usmeritev - 1) % 4]
            if self.zgodovina[-1] == "levo":
                usmeritve = ["desno", "dol", "levo", "gor"]
                i_usmeritev = usmeritve.index(self.orientacija)
                self.orientacija = usmeritve[(i_usmeritev + 1) % 4]
            self.zgodovina = self.zgodovina[ : -1]






