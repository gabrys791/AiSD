#zad1
# def zadanie1(imie,nazwisko):
#     litera=imie[0]
#     return litera+'.'+nazwisko
#
# imie='Gabriel'
# nazwisko='Majewski'
# print(zadanie1(imie,nazwisko))
#zad2
# def zadanie1(imie,nazwisko):
#     litera=(imie[0]).upper()
#     return litera+'.'+nazwisko.capitalize()
#
# imie='Gabriel'
# nazwisko='Majewski'
# print(zadanie1(imie,nazwisko))
#zad3
# def zadanie3(rok,rok2,wiek):
#     rok=str(rok)
#     tyl=rok2-wiek
#
#     if tyl<10:
#         tyl = str(tyl)
#         return rok+'0'+tyl
#     else:
#         tyl = str(tyl)
#         return rok+tyl
#
# print(zadanie3(20,22,20))
#zad4
# def zadanie1(imie,nazwisko):
#     litera=(imie[0]).upper()
#     return litera+'.'+nazwisko.capitalize()
# def zadanie4(imie,nazwisko,zadanie1):
#     return zadanie1(imie,nazwisko)
#
# imie='gabriel'
# nazwisko='majewski'
# print(zadanie4(imie,nazwisko,zadanie1))
#zad5
# def zadanie5(liczba1,liczba2):
#     if liczba1>0 and liczba2>0 and liczba2!=0:
#         wynik=liczba1/liczba2
#         return wynik
#
# liczba1=5
# liczba2=2
# print(zadanie5(liczba1,liczba2))
#zad6
# suma=0
# while suma<100:
#     a=input("podaj liczbę: ")
#     a=int(a)
#     suma=suma+a
#zad7
lista=['hej','jestem','gabrys']
def krotka(lista):
    krot=tuple(lista)
    return krot
print(krotka(lista))
