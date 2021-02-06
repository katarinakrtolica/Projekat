from DataImportExport import *
import Funkcionalnosti
from Meniji import *


def main():
    akcije=[]
    racuni=[]
    korisnici=[]
    knjige=[]
    UcitajAkcije("akcije.txt",akcije)
    UcitajKnjige("knjige.txt",knjige)
    UcitajKorisnike("korisnici.txt",korisnici)
    UcitajRacune("racuni.txt",racuni)

    user=Funkcionalnosti.Login(korisnici)
    while user==None:
        print("Niste se prijavili")
        user=Funkcionalnosti.Login(korisnici)
    if user["uloga"].lower()=="prodavac":
        while True:
            opcija=MeniProdavac()
            if opcija=="1":
                Funkcionalnosti.PregledKnjiga(knjige)
            elif opcija=="2":
                Funkcionalnosti.PretragaKnjiga(knjige)
            elif opcija=="3":
                Funkcionalnosti.PregledAkcija(akcije,knjige)
            elif opcija=="4":
                Funkcionalnosti.PretragaAkcija(akcije,knjige)
            elif opcija=="5":
                Funkcionalnosti.Prodaja(knjige,akcije,racuni,user)
            elif opcija=="6":
                Funkcionalnosti.DodajKnjigu(knjige)
            elif opcija=="7":
                Funkcionalnosti.IzmenaKnjige(knjige)
            elif opcija=="8":
                Funkcionalnosti.ObrisiKnjigu(knjige)
            elif opcija=="0":
                break
            else:
                print("Pogresna opcija")
    elif user["uloga"].lower()=="menadzer":
        while True:
            opcija=MeniMenadzer()
            if opcija=="1":
                Funkcionalnosti.PregledKnjiga(knjige)
            elif opcija=="2":
                Funkcionalnosti.PretragaKnjiga(knjige)
            elif opcija=="3":
                Funkcionalnosti.PregledAkcija(akcije,knjige)
            elif opcija=="4":
                Funkcionalnosti.PretragaAkcija(akcije,knjige)
            elif opcija=="5":
                Funkcionalnosti.Registracija(korisnici)
            elif opcija=="6":
                Funkcionalnosti.PrikaziKorisnike(korisnici)
            elif opcija=="7":
                Funkcionalnosti.DodavanjeAkcije(akcije,knjige)
            elif opcija=="8":
                Funkcionalnosti.KreirajIzvestaj(knjige,racuni)
            elif opcija=="0":
                break
            else:
                print("Pogresna opcija")
    else:
         while True:
            opcija=MeniAdministrator()
            if opcija=="1":
                Funkcionalnosti.PregledKnjiga(knjige)
            elif opcija=="2":
                Funkcionalnosti.PretragaKnjiga(knjige)
            elif opcija=="3":
                Funkcionalnosti.PregledAkcija(akcije,knjige)
            elif opcija=="4":
                Funkcionalnosti.PretragaAkcija(akcije,knjige)
            elif opcija=="5":
                Funkcionalnosti.Registracija(korisnici)
            elif opcija=="6":
                Funkcionalnosti.PrikaziKorisnike(korisnici)
            elif opcija=="7":
                Funkcionalnosti.DodajKnjigu(knjige)
            elif opcija=="8":
                Funkcionalnosti.IzmenaKnjige(knjige)
            elif opcija=="9":
                Funkcionalnosti.ObrisiKnjigu(knjige)
            elif opcija=="0":
                break
            else:
                print("Pogresna opcija")
    SacuvajKnjige("knjige.txt",knjige)
    SacuvajAkcije("akcije.txt",akcije)
    SacuvajRacune("racuni.txt",racuni)
    SacuvajKorisnike("korisnici.txt",korisnici)




    
main()
    
