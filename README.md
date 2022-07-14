# Timer-za-sifru-sa-generatorom
Program generise random sifru, i korisnik bira interval za koji ce ta sifra biti dostupna klikom na dugme 

Ovaj jednostavni program nam omogućava da eliminišemo iskušenja neke distrakcije koje možemo zaključati pod šifrom. npr. neki uredjaj kao što je telefon.
Šifra i vreme isteka su oboje enkodirani u tekstualnom fajlu kako ne bi došlo do lakog pristupa šifri ili menjanju vremena, ako korisnik obriše vreme opet će morati da sačeka minimalni period od 3 sata ako želi da vidi svoju šifru. Šifra je nasumično generisana i sadrži od 10-15 karaktera/brojeva kako bi se što teže naučila napamet.

Takodje program se može kompajlovati u c/c++ preko [nuitka](https://nuitka.net/) alata radi još bolje sigurnosti i eliminisanja svakog iskušenja.
