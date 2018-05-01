def premozenje(oseba,denar):
    sestevek = denar[oseba]
    for otrok in otroci[oseba]:
        sestevek = sestevek + premozenje(otrok,denar)
    return sestevek


def najbogatejsi(oseba,denar):
    m = denar[oseba]
    ime = oseba
    for otrok in otroci[oseba]:
        najbogatejsi(otrok,denar)
        if denar[otrok] > m:
            m = denar[otrok]
            ime = otrok
    return (ime ,m)


def uravnotezeni(oseba,denar):
    if len(otroci[oseba]) == 0:
        return True
    vrednost = premozenje(otroci[oseba][0], denar)
    for otrok in otroci[oseba]:
        if not uravnotezeni(otrok, denar):
            return False
        if vrednost != premozenje(otrok, denar):
            return False
    return True

def neuravnotezeni(oseba, denar):
    if len(otroci[oseba]) == 0:
        return None
    vrednost = premozenje(otroci[oseba][0], denar)
    for otrok in otroci[oseba]:
        neuravn = neuravnotezeni(otrok, denar)
        if neuravn:
            return neuravn
        if vrednost != premozenje(otrok, denar):
            return oseba
    return None