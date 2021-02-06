import datetime 

def SacuvajRacune(imeFajla,sviRacuni):
    fajl=open(imeFajla,"w")
    for racun in sviRacuni:
        stavkeRacuna=racun["stavke"]
        counter=0
        upis=""
        upis+=str(racun["sifra"])+"|"+racun["prodavac"]+"|"
        for stavka in stavkeRacuna:
            upis+=stavka["sifra"]+"-"+str(stavka["kolicina"])+"-"+str(stavka["cena"])
            if counter!=len(stavkeRacuna)-1:
                upis+=","
            counter=counter+1
        upis+="|"+str(racun["cena"])+"|"+racun["datum"].strftime('%d/%m/%Y')+"\n"
        fajl.write(upis)
    fajl.close()

def UcitajRacune(imeFajla,sviRacuni):
    fajl=open(imeFajla,"r")
    linije=fajl.readlines()
    for linija in linije:
        linija=linija.strip()
        parts=linija.split("|")
        sveStavke=[]
        prodavac=parts[1]
        datumStr=parts[4]
        datum = datetime.datetime.strptime(datumStr, "%d/%m/%Y")
        sifra=int(parts[0])
        stavke=parts[2].split(",")
        for s in stavke:
            stavka={}
            pp=s.split("-")
            stavka["kolicina"]=int(pp[1])
            stavka["cena"]=float(pp[2])
            stavka["sifra"]=pp[0]
            sveStavke.append(stavka)

        noviRacun={"sifra":sifra,"datum":datum,"prodavac":prodavac,"stavke":sveStavke,"cena":float(parts[3])}
        sviRacuni.append(noviRacun)
    fajl.close()

def SacuvajAkcije(imeFajla,sveAkcije):
    fajl=open(imeFajla,"w")
    for akcija in sveAkcije:
        upis=""
        upis+=str(akcija["sifra"])+"|"
        svePonude=akcija["ponude"]
        counter=0
        for ponuda in svePonude:
            upis+=ponuda["sifra"]+"-"+str(ponuda["cena"])
            if counter!=len(svePonude)-1:
                upis+=","
            counter+=1
        upis+="|"+akcija["datum"].strftime('%d/%m/%Y')+"\n"
        fajl.write(upis)
    fajl.close()


def UcitajAkcije(imeFajla,sveAkcije):
    fajl=open(imeFajla,"r")
    linije=fajl.readlines()
    for linija in linije:
        linija=linija.strip()
        parts=linija.split("|")
        ponude=parts[1].split(",")
        listaPonuda=[]
        for ponuda in ponude:
            kv=ponuda.split("-")
            p={}
            p["sifra"]=kv[0]
            p["cena"]=float(kv[1])
            listaPonuda.append(p)
        datum = datetime.datetime.strptime(parts[2], "%d/%m/%Y")
        novaAkcija={"sifra":int(parts[0]),"ponude":listaPonuda,"datum":datum}
        sveAkcije.append(novaAkcija)
    fajl.close()


def UcitajKnjige(imeFajla,sveKnjige):
    fajl=open(imeFajla,"r")
    linije=fajl.readlines()
    for linija in linije:
        linija=linija.strip()
        parts=linija.split("|")
        if parts[9]=="1":
            continue
        knjiga={"sifra":parts[0],"obrisan":"0","naslov":parts[1],"isbn":parts[2],"autor":parts[3],"izdavac":parts[4],"brStrana":int(parts[5]),"godina":int(parts[6]),"cena":float(parts[7]),"kategorija":parts[8]}
        sveKnjige.append(knjiga)
    fajl.close()


def SacuvajKnjige(imeFajla,sveKnjige):
    fajl=open(imeFajla,"w")
    for knjiga in sveKnjige:
        upis=knjiga["sifra"]+"|"+knjiga["naslov"]+"|"+knjiga["isbn"]+"|"+knjiga["autor"]+"|"+knjiga["izdavac"]+"|"+str(knjiga["brStrana"])+"|"+str(knjiga["godina"])+"|"+str(knjiga["cena"])+"|"+knjiga["kategorija"]+"|"+str(knjiga["obrisan"])+"\n"
        fajl.write(upis)
    fajl.close()

def UcitajKorisnike(imeFajla,sviKorisnici):
    fajl=open(imeFajla,"r")
    linije=fajl.readlines()
    for linija in linije:
        delovi=linija.strip().split("|")
        korisnik={"uloga":delovi[0],"user":delovi[1],"pass":delovi[2],"ime":delovi[3],"prezime":delovi[4]}
        sviKorisnici.append(korisnik)
    fajl.close()

def SacuvajKorisnike(imeFajla,sviKorisnici):
    fajl=open(imeFajla,"w")
    for korisnik in sviKorisnici:
        upis=korisnik["uloga"]+"|"+korisnik["user"]+"|"+korisnik["pass"]+"|"+korisnik["ime"]+"|"+korisnik["prezime"]+"\n"
        fajl.write(upis)
    fajl.close()
