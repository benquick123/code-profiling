from collections import deque

def preberi(fname):
    with open(fname) as f:
        content = f.readlines()
        # remove whitespace characters like `\n` at the end of each line
        content = [x.strip() for x in content]

    zemljevid = {}
    for i,line in enumerate(content):
        line = line.split(" ")
        line = list(map(int, line))
        tmpMin = int(line[0])
        indeksMin = 0

        # find min element in line
        for j,el in enumerate(line):
            el = int(el)
            if (el < tmpMin):
                tmpMin = el
                indeksMin = j

        # rotate elements, so that min is on first place
        line = deque(line)
        line.rotate(len(line)-indeksMin)
        line = list(line)
        zemljevid[i+1] = line

    return zemljevid

def mozna_pot(pot, zemljevid):
    status = "True"
    final_nodes = finalNodes(zemljevid)
    prev_node = pot[0]
    # Check if I can come from start node to next
    if (pot[1] != zemljevid[pot[0]][0]):
        return False

    # Check if path starts and ends with a final node
    if (pot[0] not in final_nodes or pot[len(pot)-1] not in final_nodes):
        return False

    # Remove first node
    pot = pot[1:]

    for i,node in enumerate(pot):
        if (i == len(pot)-1):
            break
        # Check if I want to go to the same node
        if (node == prev_node):
            return False

        # Check if current node is final
        if (node in final_nodes):
            return False

        # Check if I can come from current node to next node in our path
        if (pot[i+1] not in zemljevid[node]):
            return False

    return status

def finalNodes( zemljevid):
    final_nodes = []
    for key,val in zemljevid.items():
        if (len(zemljevid[key]) == 1):
            final_nodes.append(key)

    return final_nodes

def hamiltonova(pot, zemljevid):
    status = "True"
    final_nodes = finalNodes(zemljevid)
    prev_node = pot[0]
    # Visited nodes
    visited = [pot[0]]

    # Check if I can come from start node to next
    if (pot[1] != zemljevid[pot[0]][0]):
        return False

    # Check if path starts and ends with a final node
    if (pot[0] not in final_nodes or pot[len(pot) - 1] not in final_nodes):
        return False

    # Remove first node
    pot = pot[1:]

    for i, node in enumerate(pot):
        # Dodaj trenutno vozlisce v ze obiskana
        if (node in visited):
            return False
        else:
            visited.append(node)

        if (i == len(pot) - 1):
            break

        # Check if I want to go to the same node
        if (node == prev_node):
            return False

        # Check if current node is final
        if (node in final_nodes):
            return False

        # Check if I can come from current node to next node in our path
        if (pot[i + 1] not in zemljevid[node]):
            return False

    # We visited all nodes except final ones
    if (len(visited)-2 == len(zemljevid)-len(final_nodes)):
        return "True"
    else:
        return False

# zemljevid = preberi("zemljevid.txt")
# print(zemljevid)
# status = mozna_pot([1, 3, 7, 3, 4, 2], zemljevid)
# status = mozna_pot([4,1,2], zemljevid)
# status = hamiltonova([1, 3, 8, 16, 9, 14, 11, 6, 4, 5, 10, 13, 12], zemljevid)
# print(status)