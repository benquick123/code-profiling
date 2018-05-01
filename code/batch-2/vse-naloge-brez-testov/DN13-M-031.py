class Minobot():

    def __init__(self):
        self.state = [(complex(), 1)]

    # ¯\_(ツ)_/¯
    def pass_state(func):
        def wrapper(self, *args, **kwargs):
            return func(self, *self.state[-1], *args, **kwargs)
        return wrapper

    # ¯\_(ツ)_/¯
    def save_state(func):
        def wrapper(self, *args, **kwargs):
            self.state.append(func(self, *args, **kwargs))
            return self.state[-1]
        return wrapper

    @save_state
    @pass_state
    def naprej(self, coords, direction, d):
        return (coords + d * direction, direction)

    @save_state
    @pass_state
    def desno(self, coords, direction):
        return (coords, direction * -1j)
    
    @save_state
    @pass_state
    def levo(self, coords, direction):
        return (coords, direction * 1j)

    @pass_state
    def koordinate(self, coords, direction):
        return coords.real, coords.imag

    @pass_state
    def razdalja(self, coords, direction):
        return abs(coords.real) + abs(coords.imag)

    def razveljavi(self):
        if len(self.state) > 1: 
            self.state.pop()








