#kalkulator

prvi_broj = input("Unesite prvi broj")
drugi_broj = int(input("Unesite drugi broj: "))
operacija = input("Unesite operaciju (+, -, /")

def zbroji(broj_jedan, broj_dva):
    return(broj_jedan + broj_dva)

def oduzmi(broj_jedan, broj_dva):
    return(broj_jedan - broj_dva)

def množi(broj_jedan, broj_dva):
    return(broj_jedan * broj_dva)

def dijeli(broj_jedan, broj_dva):
    if broj_dva > 0:
        return(broj_jedan / broj_dva)
