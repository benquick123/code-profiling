from itertools import chain
import string

def unikati(s):
    return [i for j,i in enumerate(s) if j == s.index(i)]

def avtor(tweet):
    return tweet.split(sep = ":")[0]

def vsi_avtorji(tweets):
    return unikati([avtor(i) for i in tweets])

def izloci_besedo(s):
    return s.strip("".join( [i for i in s if not i.isalnum()] ))

def se_zacne_z(tweet, c):
    return [izloci_besedo(i) for i in tweet.split() if i[0] == c]

def zberi_se_zacne_z(tweets, c):
    return unikati(tuple(chain( *[se_zacne_z(t, c) for t in tweets] )))

def vse_afne(tweets):
    return zberi_se_zacne_z(tweets, "@")

def vsi_hashtagi(tweets):
    return zberi_se_zacne_z(tweets, "#")

def vse_osebe(tweets):
    return sorted(unikati( vsi_avtorji(tweets) + vse_afne(tweets) ))

def custva(tweets, hashtags):
    return sorted(vsi_avtorji( [t for t in tweets 
                                  if any(ht for ht in hashtags if "#" + ht in t)] ))
                            
def se_poznata(tweets, person1, person2):
    return any(t for t in tweets
                 if person1 == avtor(t) and person2 in se_zacne_z(t, "@") 
                 or person2 == avtor(t) and person1 in se_zacne_z(t, "@"))




