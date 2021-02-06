def IspisiKorisnike(sviKorisnici):
    print("------------Korisnici--------------")
    for korisnik in sviKorisnici:
        ispis=korisnik["uloga"]+"|"+korisnik["user"]+"|"+korisnik["ime"]+"|"+korisnik["prezime"]
        print(ispis)
    print("------------------------------------")

def AutomatskaSifraAkcije(sveAkcije):
    if len(sveAkcije)==0:
        return 1
    sveSifre=[]
    for akcija in sveAkcije:
        sveSifre.append(akcija["sifra"])
    m=max(sveSifre)
    m=m+1
    return m

def AutomatskaSifraRacuni(sviRacuni):
    if len(sviRacuni)==0:
        return 1
    sveSifre=[]
    for racun in sviRacuni:
        sveSifre.append(racun["sifra"])
    m=max(sveSifre)
    m=m+1
    return m

def NadjiAkciju(sveAkcije,sifra):
    for akcija in sveAkcije:
        if akcija["sifra"]==sifra:
            return akcija
    return None

def SortKorisnici(sviKorisnici,key):
    if key!="ime" and key!="prezime" and key!="uloga":
        return False
    for i in range(len(sviKorisnici)-1):
        for j in range(i+1,len(sviKorisnici)):
            if sviKorisnici[j][key]<sviKorisnici[i][key]:
                temp=sviKorisnici[i]
                sviKorisnici[i]=sviKorisnici[j]
                sviKorisnici[j]=temp
    return True

def IspisiAkcije(sveAkcije,sveKnjige):
    print("--------Akcije----------")
    for akcija in sveAkcije:
        linija=str(akcija["sifra"])+"|"
        ponude=akcija["ponude"]
        for ponuda in ponude:
            sifra=ponuda["sifra"]
            knjiga=NadjiKnjigu(sveKnjige,sifra)
            linija+=knjiga["naslov"]+" - "+str(ponuda["cena"])+" "
        datum=akcija["datum"]
        linija+="|"+datum.strftime('%d/%m/%Y')+"\n"
        print(linija)
    print("----------------------")
def SortAkcije(sveAkcije,key):
    if key!="sifra" and key!="datum":
        return False
    for i in range(len(sveAkcije)-1):
        for j in range(i+1,len(sveAkcije)):
            if sveAkcije[j][key]<sveAkcije[i][key]:
                temp=sveAkcije[i]
                sveAkcije[i]=sveAkcije[j]
                sveAkcije[j]=temp
    return True

def PretraziAkcije(sveAkcije,sveKnjige,key,value):
    search=[]
    for akcija  in sveAkcije:
        if key=="sifra":
            if value==akcija["sifra"]:
                search.append(akcija)
        elif key=="naslov" or key=="autor" or key=="kategorija":
            ponude=akcija["ponude"]
            for ponuda in ponude:
                sifra=ponuda["sifra"]
                knjiga=NadjiKnjigu(sveKnjige,sifra)
                if knjiga[key].lower().find(value.lower())!=-1:
                    search.append(akcija)
                    break

    return search

def PretraziKnjige(sveKnjige,key,value):
    search=[]
    for knjiga in sveKnjige:
        if key=="cena":
            if knjiga[key]>=value[0] and knjiga[key]<=value[1]:
                search.append(knjiga)
        else:
            if knjiga[key].lower().find(value.lower())!=-1:
                search.append(knjiga)
    return search


def NadjiKnjigu(sveKnjige,s):
    for knjiga in sveKnjige:
        if knjiga["sifra"]==s:
            return knjiga
    return None

def IspisiKnjige(sveKnjige):
    print("--------Knjige--------")
    for knjiga in sveKnjige:
        ispis=knjiga["sifra"]+"|"+knjiga["naslov"]+"|"+knjiga["autor"]+"|"+knjiga["izdavac"]+"|"+str(knjiga["cena"])+"|"+knjiga["kategorija"]
        print(ispis)
    print("----------------------")

def SortKnjige(knjige,key):
    if key!="naslov" and key!="kategorija" and key!="autor" and key!="izdavac" and key!="cena":
        return False
    for i in range(len(knjige)-1):
        for j in range(i+1,len(knjige)):
            if knjige[j][key]<knjige[i][key]:
                temp=knjige[i]
                knjige[i]=knjige[j]
                knjige[j]=temp
    return True