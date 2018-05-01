def besedilo(tvit):
   return (':'.join(tvit.split(':')[1:])).strip()

#print(besedilo("ana: kdo so te: @berta, @cilka, @dani?"))

def zadnji_tvit(tviti):
  slovar={}
  for tvit in tviti:
    a=tvit.split(':')
    avtor=a[0]
    besedilo=(':'.join(a[1:])).strip()
    slovar[avtor]=besedilo
  return slovar



def prvi_tvit(tviti):
  slovar={}
  for tvit in tviti:
    a=tvit.split(':')
    avtor=a[0]
    if avtor not in slovar:
      besedilo=(':'.join(a[1:])).strip()
      slovar[avtor]=besedilo
  return slovar

#print(prvi_tvit(tviti))

def prestej_tvite(tviti):
  slovar={}
  for tvit in tviti:
    a=tvit.split(':')
    avtor=a[0]
    if avtor not in slovar:
      slovar[avtor]=1
    else:
      slovar[avtor]=slovar[avtor]+1
  return slovar

#print(prestej_tvite(tviti))


def izloci_besedo(beseda):
  a=-1
  b=-1
  for i, e in enumerate(beseda):
    if e.isalnum():
      a=i
      break
  if a == -1:
    return ''
  for i, e in enumerate(beseda[::-1]):
    if e.isalnum():
      b=i
      break
  dejanski_index_b=len(beseda)-1-b
  return beseda[a:dejanski_index_b+1]

def se_zacne_z(tvit, c):
  return [izloci_besedo(e) for e in tvit.split(' ') if len(e)>0 and e[0]==c]



def omembe(tviti):
  slovar={}
  for tvit in tviti:
    a=tvit.split(':')
    avtor=a[0]
    if avtor not in slovar:
      slovar[avtor]=se_zacne_z(besedilo(tvit), '@')
    else:
      slovar[avtor]+=(se_zacne_z(besedilo(tvit), '@'))
  return {key:slovar[key] for key in slovar}


#print(omembe(tviti))

def neomembe(ime, omembe):
  return list(set(omembe.keys()).difference(omembe[ime]+[ime]))

#print(neomembe('sandra', omembe(tviti)))

def se_poznata(ime1, ime2, omembe):
  return (ime1 in omembe and ime2 in omembe[ime1]) or (ime2 in omembe and ime1 in omembe[ime2])

#print(se_poznata('ema', 'benjamin', omembe(tviti)))

def hashtagi(tviti):
  slovar={}
  for tvit in tviti:
    a=tvit.split(':')
    avtor=a[0]
    for has in se_zacne_z(tvit, '#'):
      if has in slovar:
        slovar[has].add(avtor)
      else:
        slovar[has]=set([avtor])
  return {key:sorted(list(slovar[key])) for key in slovar}