# Domača Naloga: Krožiščca

# Naloga 1

def preberi(ime_datoteke):
    with open(ime_datoteke) as f:
        first = {i: list(map(int, a.strip('\n').split())) for i, a in enumerate(f, start=1)}
        return {a: b[b.index(min(b)):] + b[:b.index(min(b))] for a, b in first.items()}

# Naloga 2

# Naloga 3

