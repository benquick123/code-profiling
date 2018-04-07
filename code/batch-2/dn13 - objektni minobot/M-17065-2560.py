from math import fabs


class Minobot:
    def __init__(self):
        self.x = 0
        self.y = 0

        self.direction = 0

        self.x_direction_coefficient = [1, 0, -1, 0]
        self.y_direction_coefficient = [0, -1, 0, 1]

        self.states = []

    def get_current_state(self):
        return {'x': self.x, 'y': self.y, 'direction': self.direction}

    def save_current_state(self):
        self.states.append(self.get_current_state())

    def change_direction(self, direction):
        self.save_current_state()

        self.direction = (self.direction + direction) % 4

    def levo(self):
        self.change_direction(-1)

    def desno(self):
        self.change_direction(1)

    def naprej(self, d):
        self.save_current_state()

        if self.x_direction_coefficient[self.direction]:
            self.x += d * self.x_direction_coefficient[self.direction]
        else:
            self.y += d * self.y_direction_coefficient[self.direction]

    def razveljavi(self):
        if self.states:
            previous_state = self.states.pop()

            self.x = previous_state['x']
            self.y = previous_state['y']

            self.direction = previous_state['direction']

    def razdalja(self):
        return abs(self.x) + abs(self.y)

    def koordinate(self):
        return self.x, self.y


