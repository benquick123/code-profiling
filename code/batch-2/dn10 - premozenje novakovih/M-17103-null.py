def premozenje(oseba, denar):
    if len(otroci[oseba]) == 0:
        return denar[oseba]

    rez = denar[oseba]
    for os in otroci[oseba]:
        rez += premozenje(os, denar)
    return rez

def najbogatejsi(oseba, denar):
    maximum = oseba, denar[oseba]
    for ime in otroci[oseba]:
        maks = najbogatejsi(ime, denar)
        if maximum[1] < maks[1]:
            maximum = maks
    return maximum