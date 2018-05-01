def preberi(ime_datoteke):
    krizisca={}
    i=1
    file=open(ime_datoteke).readlines()
    minimums=[]
    for pot in file:
        neurejeno= [int(k) for k in pot.split()]
        minimum=min(neurejeno)
        for krizisce in neurejeno:
            if krizisce==minimum:
                krizisca[i]=[neurejeno[k] for k in range(neurejeno.index(minimum),len(neurejeno))]
                krizisca[i]+=[neurejeno[k] for k in range(0,neurejeno.index(minimum))]
        i+=1
    return krizisca

def mozna_pot(pot, zemljevid):
    koraki=zip(pot,pot[1:])
    for korak in koraki:
        if korak[1] in zemljevid[korak[0]]:
            continue
        else:
            return False
    for k in pot[1:len(pot)-2]:
        if len(zemljevid[k])==1:
            return False
    if len(zemljevid[pot[len(pot)-1]])==1 and len(zemljevid[pot[0]])==1:
        return True
    return False
def hamiltonova(pot, zemljevid):
    konci=[]
    brez_koncev=[]
    if mozna_pot(pot,zemljevid):
      for krizisce in zemljevid:
          if len(zemljevid[krizisce])==1:
              konci.append(krizisce)
          else:
              brez_koncev.append(krizisce)

      pot.sort()
      for konec in konci:
          try:
              pot.remove(konec)
          except:
              continue

      if pot == brez_koncev:
          return True
      else:
          return False

    else:
        return False
    return True



