import classi as cl


x = "-1"

while x != "0":
    print("1 - Aggiungi contatto")
    print("2 - Ricerca contatto")
    print("3 - Modifica contatto")
    print("4 - Elimina contatto")
    print("5 - Stampa rubrica")
    print("6 - Elimina la rubrica")
    print("7 - Backup rubrica")
    print("0 - Esci")
    x = input()

    ru = cl.Rubrica()

    if x == "1":
        ru.Aggiungi(input("Nome: "), input("Cognome: "), input("Telefono: "))
    else:
        if x == "2":
            ru.Ricerca(input("Cerca per: 1 - Nome    2 - Cognome    3 - Numero:   "))
        else:
            if x == "3":
                ru.Modifica(input("Nome contatto da modificare: "), input("Cognome contatto da modificare: "), input("Telefono contatto da modificare: "))
            else:
                if x == "4":
                    ru.Elimina(input("Nome contatto da eliminare: "), input("Cognome contatto da eliminare: "), input("Telefono contatto da eliminare: "))
                else:
                    if x == "5":
                        print(ru.Stampa(), "\n")
                    else:
                        if x == "6":
                            ru.Reset()
                        else:
                            if x == "7":
                                ru.Backup()
                            else:
                                if x != "0":
                                    print("La scelta non è disponibile")
