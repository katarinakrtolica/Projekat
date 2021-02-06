from PomocneFunkcije import *
import datetime
import DataImportExport
def PretragaAkcija(akcije,knjige):
    print()
    print("1. Pretraga po sifri")
    print("2. Pretraga po naslovu ")
    print("3. Pretraga po autoru")
    print("4. Pretraga po kategoriji ")
    izbor=input("Unesite izbor: ")
    if izbor=="1":
        sifra=input("Unesite sifru: ")
        search=PretraziAkcije(akcije,knjige,"sifra",int(sifra))
        IspisiAkcije(search,knjige)
    elif izbor=="2":
        naslov=input("Unesite naslov: ")
        search=PretraziAkcije(akcije,knjige,"naslov",naslov)
        IspisiAkcije(search,knjige)
    elif izbor=="3":
        autor=input("Unesite autora: ")
        search=PretraziAkcije(akcije,knjige,"autor",autor)
        IspisiAkcije(search,knjige)
    elif izbor=="4":
        kategorija=input("Unesite kategoriju: ")
        search=PretraziAkcije(akcije,knjige,"kategorija",kategorija)
        IspisiAkcije(search,knjige)
    else:
        print("Pogresna opcija!!!")

def PretragaKnjiga(knjige):
    print("1. Pretraga po sifri")
    print("2. Pretraga po naslovu ")
    print("3. Pretraga po autoru")
    print("4. Pretraga po kategoriji ")
    print("5. Pretraga po izdavacu ")
    print("6. Pretraga po opsegu cene ")
    izbor=input("Unesite opciju: ")
    if izbor=="1":
        sifra=input("Unesite sifru: ")
        search=PretraziKnjige(knjige,"sifra",sifra)
        IspisiKnjige(search)
    elif izbor=="2":
        naslov=input("Unesite naslov: ")
        search=PretraziKnjige(knjige,"naslov",naslov)
        IspisiKnjige(search)
    elif izbor=="3":
        autor=input("Unesite autora: ")
        search=PretraziKnjige(knjige,"autor",autor)
        IspisiKnjige(search)
    elif izbor=="4":
        kategorija=input("Unesite kategoriju: ")
        search=PretraziKnjige(knjige,"kategorija",kategorija)
        IspisiKnjige(search)
    elif izbor=="5":
        izdavac=input("Unesite izdavaca: ")
        search=PretraziKnjige(knjige,"izdavac",izdavac)
        IspisiKnjige(search)
    elif izbor=="6":
        g=float(input("Unesite gornji limit  cene: "))
        d=float(input("Unesite donji limit cene: "))
        cene=[d, g]
        search=PretraziKnjige(knjige,"cena",cene)
        IspisiKnjige(search)
    else:
        print("Pogresna opcija")
    
def PregledAkcija(akcije,knjige):
    print("1. Ispisi nesortirane")
    print("2. Ispisi sortirane")
    opcija=input("Unesite opciju: ")
    if opcija=="1":
        IspisiAkcije(akcije,knjige)
    elif opcija=="2":
        key=input("Unesite key, sifra ili datum: ")
        if SortAkcije(akcije,key)==True:
            IspisiAkcije(akcije,knjige)
        else:
            print("Nepostojeci kljuc!!!")
    else:
        print("Nepostojeca opcija!!!")

def PregledKnjiga(knjige):
    print("1. Ispisi nesortirane")
    print("2. Ispisi sortirane")
    opcija=input("Unesite opciju: ")
    if opcija=="1":
       IspisiKnjige(knjige)
    elif opcija=="2":
        key=input("Unesite key naslov V cena V izdavac V autor V kategorija: ")
        if SortKnjige(knjige,key)==True:
           IspisiKnjige(knjige)
        else:
            print("Niste uneli validan kljuc")
    else:
        print("Nepostojeca opcija")

def Login(korisnici):
    counter=0
    while counter<3:
        korisnickoIme=input("Unesite vase korisnicko ime: ")
        sifra=input("Unesite vasu lozinku: ")
        for korisnik in korisnici:
            if korisnik["user"]==korisnickoIme and korisnik["pass"]==sifra:
                return korisnik
        print("Pogresili ste korisnicko ime ili lozinku!!!")
        counter+=1
    print("Previse puta ste uneli pogresno korisnicko ime ili lozinku, morate sacekati pre sledece prijave!")


def KreirajIzvestaj(knjige,racuni):
    print("1. Prodaja svih knjiga")
    print("2. Prodaja svih knjiga odabranog autora")
    print("3. Prodaja svih knjiga odabranog izdavaca")
    opcija=input("Unesite opciju: ")
    if opcija=="1":
        for knjiga in knjige:
            zarada=0
            counter=0
            for racun in racuni:
                for stavka in racun["stavke"]:
                    if stavka["sifra"]==knjiga["sifra"]:
                        counter+=stavka["kolicina"]
                        zarada+=stavka["kolicina"]*stavka["cena"]
            linija="Naslov: "+knjiga["naslov"]+" , Autor: "+knjiga["autor"]+" , Broj prodatih primeraka: "+str(counter)+" , Zarada: "+str(zarada)
            print(linija)
    elif opcija=="2":
        autor=input("Unesite autora: ")
        counter=0
        zarada=0
        for knjiga in knjige:
            if knjiga["autor"].lower()!=autor.lower():
                continue
            for racun in racuni:
                for stavka in racun["stavke"]:
                    if stavka["sifra"]==knjiga["sifra"]:
                        counter+=stavka["kolicina"]
                        zarada+=stavka["kolicina"]*stavka["cena"]
            linija="Naslov: "+knjiga["naslov"]+", Autor: "+knjiga["autor"]+", Broj prodatih primeraka: "+str(counter)+", Zarada: "+str(zarada)
            print(linija)
    elif opcija=="3":
        izdavac=input("Unesite izdavaca: " )
        counter=0
        zarada=0
        for knjiga in knjige:
            if knjiga["izdavac"].lower()!=izdavac.lower():
                continue
            for racun in racuni:
                for stavka in racun["stavke"]:
                    if stavka["sifra"]==knjiga["sifra"]:
                        counter+=stavka["kolicina"]
                        zarada+=stavka["kolicina"]*stavka["cena"]
            linija="Naslov: "+knjiga["naslov"]+", Autor: "+knjiga["autor"]+", Broj prodatih primeraka: "+str(counter)+", Zarada: "+str(zarada)
            print(linija)

def DodavanjeAkcije(akcije,knjige):
    ponude=[]
    s=AutomatskaSifraAkcije(akcije)
    while 1>0:
        print("1. Dodaj knjigu u akciju ")
        print("2. Sacuvaj akciju ")
        print("3. Odustani")
        opcija=input("Unesite opciju: ")
        if opcija=="1":
            IspisiKnjige(knjige)
            sifra=input("Unesite sifru knjige: ")
            knjiga=NadjiKnjigu(knjige,sifra)
            if knjiga==None:
                print("Ne postoji knjiga sa unetom sifrom!")
            else:
                cena=float(input("Unesite novu cenu: "))
                p={"sifra":sifra,"cena":cena}
                ponude.append(p)
        elif opcija=="2":
            if len(ponude)==0:
                print("Morate dodati bar jednu knjigu u akciju: ")
                return
            d=input("Unesite datum trajanja akcije u formatu dd/mm/yyyy")
            datum=datetime.datetime.strptime(d, "%d/%m/%Y")
            akcija={"sifra":s,"ponude":ponude,"datum":datum}
            akcije.append(akcija)
            return
        elif opcija=="3":
            print("Odustali ste od kreiranja akcije")
            return
        else:
            print("Nepostojeca opcija")

    
def ObrisiKnjigu(knjige):
    IspisiKnjige(knjige)
    sifra=input("Unesite sifru knjige: ")
    knjiga=NadjiKnjigu(knjige,sifra)
    if knjiga==None:
        print("Ne postoji knjiga sa unetom sifrom!!!")
    else:
        knjiga["obrisan"]="1"
        DataImportExport.SacuvajKnjige("knjige.txt",knjige)
        for i in range(len(knjige)):
            if knjige[i]["sifra"]==sifra:
                del knjige[i]


def IzmenaKnjige(knjige):
    IspisiKnjige(knjige)
    sifra=input("Unesite sifru knjige: ")
    knjiga=NadjiKnjigu(knjige,sifra)
    if knjiga==None:
        print("Ne postji knjiga sa unetom sifrom!!!")
        return

    naslov=input("Unesite naslov: ")
    if naslov!="":
        knjiga["naslov"]=naslov
    autor=input("Unesite autora: ")
    if autor!="":
        knjiga["autor"]=autor
    isbn=input("Unesite isbn : ")
    if isbn!="":
        knjiga["isbn"]=isbn
    strane=input("Unesite broj strana: ")
    if strane!="":
        knjiga["brStrana"]=int(strane)
    izdavac=input("Unesite izdavaca: ")
    if izdavac!="":
        knjiga["izdavac"]=izdavac
    godinaIzdanja=input("Unesite godinu izdanja: ")
    if godinaIzdanja!="":
        knjiga["godina"]=int(godinaIzdanja)
    cena=input("Unesite cenu: ")    
    if cena!="":
        knjiga["cena"]=float(cena)    
    kategorija=input("Unesite kategoriju: ")
    if kategorija!="":
        knjiga["kategorija"]=kategorija
    
    print("Knjiga uspesno izmenjena!!!")


def DodajKnjigu(knjige):
    sifra=input("Unesite sifru: ")
    naslov=input("Unesite naslov: ")
    autor=input("Unesite autora: ")
    brStrana=input("Unesite broj strana: ")
    godina=input("Unesite godinu izdanja: ")
    izdavac=input("Unesite izdavaca: ")
    kategorija=input("Unesite kategoriju: ")
    isbn=input("Unesite isbn: ")
    cena=input("Unesite cenu: ")        
    if sifra=="" or naslov=="" or isbn=="" or autor=="" or brStrana=="" or godina=="" or cena=="" or kategorija=="" or izdavac=="":
        print("Niste uneli sve podatke!!!")
        return
    godina=int(godina)
    cena=float(cena)
    brStrana=int(brStrana)
    knjiga={"obrisan":"0","sifra":sifra,"naslov":naslov,"isbn":isbn,"autor":autor,"izdavac":izdavac,"brStrana":brStrana,"godina":godina,"cena":cena,"kategorija":kategorija}
    knjige.append(knjiga)
    print("Knjiga uspesno dodata!!!")

def MeniProdaja():
    print("1. Dodaj u korpu")
    print("2. Prikazi stanje korpe")
    print("3. Potvrdi kupovinu: ")
    print("4. Odustani od kupovine: ")
    opcija=input("Unesite opciju: ")
    return opcija

def DodajUKorpu(korpa,knjige,akcije):
    while 1>0:
        print("1. Dodaj preko sifre")
        print("2. Dodaj preko akcije")
        print("3. Zavrsi dodavanje u korpu ")
        opcija=input("Unesite opciju: ")
        if opcija=="1":
            IspisiKnjige(knjige)
            sifra=input("Unesite sifru: ")
            book=NadjiKnjigu(knjige,sifra)
            if book==None:
                print("Uneli ste sifru knjige koja ne postoji!!!")
            else:
                kolicina=int(input("Unesite broj primeraka: "))
                stavka={"kolicina":kolicina,"cena":book["cena"],"sifra":book["sifra"]}
                korpa.append(stavka)
        elif opcija=="2":
            IspisiAkcije(akcije,knjige)
            sifra=int(input("Unesite sifru: "))
            akcija=NadjiAkciju(akcije,sifra)
            if akcija==None:
                print("Ne postoji akcija sa unetom sifrom")
            elif akcija["datum"]<datetime.datetime.now():
                print("Akcija vise ne vazi!!!")
            else:
                ponude=akcija["ponude"]
                for ponuda in ponude:
                    stavka={}
                    stavka["sifra"]=ponuda["sifra"]
                    stavka["kolicina"]=1
                    stavka["cena"]=ponuda["cena"]
                    korpa.append(stavka)
        elif opcija=="3":
            return korpa
        else:
            print("Pogresna opcija")


def Prodaja(knjige,akcije,racuni,prodavac):
    stavke=[]
    ukupnaCena=0
    while 1>0:
        opcija=MeniProdaja()
        if opcija=="1":
            DodajUKorpu(stavke,knjige,akcije)
        elif opcija=="2":
            uk=0
            for stavka in stavke:
                linija=str(stavka["kolicina"])+" - "+str(stavka["cena"])
                uk+=stavka["kolicina"]*stavka["cena"]
                print(linija)
            print("Ukupna cena u korpi : "+str(uk))
        elif opcija=="3":
            sifraRacuna=AutomatskaSifraRacuni(racuni)
            for stavka in stavke:
                ukupnaCena+=stavka["cena"]*stavka["kolicina"]
            datum = datetime.datetime.now()
            racun={"sifra":sifraRacuna,"prodavac":prodavac["user"],"datum":datum,"stavke":stavke,"cena":ukupnaCena}
            racuni.append(racun)
            return
        elif opcija=="4":
            print("Kupovina se prekida!!!")
            return
        else:
            print("Pogresna opcija")

def PrikaziKorisnike(korisnici):
    print("1. Sortiraj po imenu")
    print("2. Sortiraj po prezimenu ")
    print("3. Sortiraj po tipu korisnika")
    print("4. Ne sortiraj ")
    opcija=input("Unesite opciju: ")
    if opcija=="1":
        SortKorisnici(korisnici,"ime")
        IspisiKorisnike(korisnici)
    elif opcija=="2":
        SortKorisnici(korisnici,"prezime")
        IspisiKorisnike(korisnici)
    elif opcija=="3":
        SortKorisnici(korisnici,"uloga")
        IspisiKorisnike(korisnici)
    elif opcija=="4":
        IspisiKorisnike(korisnici)
    else:
        print("Pogresna opcija")

def Registracija(korisnici):
    korisnickoIme=input("Unesite korisnicko ime: ")
    if korisnickoIme=="":
        print("Polje ne sme biti prazno!!!")
        return None
    for korisnik in korisnici:
        if korisnik["user"]==korisnickoIme:
            print("Zauzeto korisnicko ime: ")
            return None
    lozinka=input("Unesite lozinku: ")
    if lozinka=="":
        print("Polje ne sme biti prazno")
        return None
    ime=input("Unesite ime: ")
    if ime=="":
        print("Polje ne sme biti prazno")
        return None
    prezime=input("Unesite prezime")
    if prezime=="":
        print("Polje ne sme biti prazno")
        return None


    print("1. Menadzer")
    print("2. Prodavac")
    opcija=input("unesite opciju: ")
    while opcija!="1" and opcija!="2":
        print("1. Menadzer")
        print("2. Prodavac")
        opcija=input("unesite opciju: ")

    if opcija=="2":
        uloga="Prodavac"
    else:
        uloga="Menadzer"
    noviKorisnik={"uloga":uloga,"user":korisnickoIme,"pass":lozinka,"ime":ime,"prezime":prezime}
    korisnici.append(noviKorisnik)
