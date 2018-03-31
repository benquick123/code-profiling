def premozenje(oseba, denar):
    if len(otroci[oseba]) == 0:
        return denar[oseba]

    rez = denar[oseba]
    for os in otroci[oseba]:
        rez += premozenje(os, denar)
    return rez

def najbogatejsi(oseba, denar):
    max = (oseba, denar[oseba])
    for nam in otroci[oseba]:
        oseb = najbogatejsi(nam, denar)
        if max[1] < oseb[1]:
            max = oseb
        else:
            return max
    return max