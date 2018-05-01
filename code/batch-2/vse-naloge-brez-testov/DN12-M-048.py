
import collections

def order_intersections(connected_intersections):
    min_index = connected_intersections.index(min(connected_intersections))
    return connected_intersections[min_index:] + connected_intersections[:min_index]

def preberi(ime_datoteke):
    file = open(ime_datoteke, "r")

    intersections = collections.defaultdict(list)
    intersection_number = 1
    for line in file:
        # Convert list of chars to list of ints
        inter_numbers = list(map(int, line.split()))

        intersections[intersection_number] = order_intersections(inter_numbers)
        intersection_number += 1

    file.close()

    return intersections

def mozna_pot(pot, zemljevid):
    # Check if we don't start and end at the entrance
    if len(zemljevid[pot[0]]) != 1 or len(zemljevid[pot[-1]]) != 1:
        return False

    for i in range(0, len(pot) - 1):
        if i != 0 and len(zemljevid[pot[i]]) == 1:
            return False

        if pot[i] not in zemljevid[pot[i + 1]]:
            return False

    return True

def get_entry_nodes(path, map):
    entry_nodes = []
    for node in path:
        if len(map[node]) == 1:
            entry_nodes.append(node)

    return entry_nodes

def hamiltonova(pot, zemljevid):
    # Check if the path has any duplicates
    if len(pot) != len(set(pot)):
        return False

    # Check the path includes all non entry nodes
    if set(pot) - set(get_entry_nodes(pot, zemljevid)) != \
       zemljevid.keys() - set(get_entry_nodes(zemljevid.keys(), zemljevid)):
        return False

    return mozna_pot(pot, zemljevid)

def navodila(pot, zemljevid):
    instructions = []
    for i in range(1, len(pot) - 1):
        # Entry point into the node
        entry_node_index = zemljevid[pot[i]].index(pot[i - 1])

        # Exit point out of the node
        exit_node_index = zemljevid[pot[i]].index(pot[i + 1])

        exit_number = (exit_node_index - entry_node_index) % len(zemljevid[pot[i]])
        instructions.append(exit_number)

    return instructions

def prevozi(zacetek, navodila, zemljevid):
    # Path will always contain the entry node and the connecting one
    path = [zacetek, zemljevid[zacetek][0]]

    for rotation_number in navodila:
        # We need to take into account the entry point into the node and add the number of rotations from the
        # instructions (which can overshot so we take the remainder similar to the navodila())
        exit_number = (zemljevid[path[-1]].index(path[-2]) + rotation_number) % len(zemljevid[path[-1]])
        next_node = zemljevid[path[-1]][exit_number]
        path.append(next_node)

    return path

def sosedi(doslej, zemljevid):
    doslej = list(doslej)
    non_duplicate_neighbors = []

    # Add all connected nodes except the ones that are in the instructions (path nodes)
    for node in doslej[::-1]:
        for connected_node in zemljevid[node]:
            if connected_node not in doslej:
                non_duplicate_neighbors.append(connected_node)

    non_duplicate_neighbors = set(non_duplicate_neighbors[::-1])
    return non_duplicate_neighbors

def razdalja(x, y, zemljevid, path = []):
    path = path + [x]

    if x == y:
        # -1 because we are searching how many connections not how many nodes
        return len(path) - 1

    min_distance = None
    for node in zemljevid[x]:
        if node not in path:
            distance = razdalja(node, y, zemljevid, path)

            if distance:
                if not min_distance or distance < min_distance:
                    min_distance = distance

    return min_distance

