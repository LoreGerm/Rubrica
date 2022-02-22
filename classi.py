import json
import fun


class Persona:
    nome = ""
    cognome = ""
    telefono = ""

    def Mod_Nome(self,nome):
        self.nome = nome

    def Mod_Cogn(self,cognome):
        self.cognome = cognome

    def Mod_Tell(self,telefono):
        self.telefono = telefono

    def Crea(self, nome, cognome, telefono):
        self.nome = nome
        self.cognome = cognome
        self.telefono = telefono
    
    def Model_to_dict(self):
        dict = {
            "nome" : self.nome,
            "cognome" : self.cognome,
            "telefono" : self.telefono
        }
        return dict

    def Dict_to_model(self, dict):
        self.nome = dict["nome"]
        self.cognome = dict["cognome"]
        self.telefono = dict["telefono"]




class Rubrica:
    nome = "rubrica.dat"
    r = json.loads(fun.Stampa(fun.rubrica))
    p = Persona()

    def Aggiungi(self,n,c,t):
        trov = False
        self.p.Crea(n,c,t)
        trov = fun.Ricerca("telefono", self.r, self.p.telefono)
        if trov[0] == False:
            self.r.append(self.p.Model_to_dict())
            fun.Over_write(fun.rubrica, self.r)
            print("\n")
        else:
            print("Contatto già registrato", "\n")

    def Ricerca(self, x):
        if self.r == []:
            print("NON CI SONO CONTATTI", "\n")
        else:
            if x == "1":
                y = input("Inserisci il nome: ")
                trov = fun.Ricerca("nome", self.r, y)
                if trov[0] == False:
                    print("Contatto non trovato")
                else:
                    for i in range(1,len(trov)):
                            print(self.r[trov[i]])
                print("\n")
            else:
                if x == "2":
                    y = input("inserisci il cognome: ")
                    trov = fun.Ricerca("cognome", self.r, y)
                    if trov[0] == False:
                        print("Contatto non trovato")
                    else:
                        for i in range(1,len(trov)):
                            print(self.r[trov[i]])
                    print("\n")
                else:
                    if x == "3":
                        y = input("Inserisci il telefono: ")
                        trov = fun.Ricerca("telefono", self.r, y)
                        if trov[0] == False:
                            print("Contatto non trovato")
                        else:
                            for i in range(1,len(trov)):
                                print(self.r[trov[i]])
                        print("\n")
                    else:
                        print("La scelta non è disponibile", "\n")

    def Modifica(self, n, c, t):
        if self.r == []:
            print("NON CI SONO CONTATTI", "\n")
        else:
            trov_n = fun.Ricerca("nome", self.r, n)
            trov_c = fun.Ricerca("cognome", self.r, c)
            trov_t = fun.Ricerca("telefono", self.r, t)
            if trov_n[0] and trov_c[0] and trov_t[0]:
                print(" Modifica: ", "\n", "1 - Nome", "\n", "2 - Cognome", "\n", "3 - Numero", "\n")
                x = input()
                if x == "1":
                    fun.Mod("nome",self.r,trov_n)
                    fun.Over_write(fun.rubrica, self.r)
                    print("Contatto modificato")
                else:
                    if x == "2":
                        fun.Mod("cognome",self.r,trov_c)
                        fun.Over_write(fun.rubrica, self.r)
                        print("Contatto modificato")
                    else:
                        if x == "3":
                            fun.Mod("telefono",self.r,trov_t)
                            fun.Over_write(fun.rubrica, self.r)
                            print("Contatto modificato")
                        else:
                            print("La scelta non è disponibile", "\n")
        print("\n")

    def Elimina(self, n, c, t):
        cest = json.loads(fun.Stampa(fun.cestino))
        trov_n = fun.Ricerca("nome", self.r, n)
        trov_c = fun.Ricerca("cognome", self.r, c)
        trov_t = fun.Ricerca("telefono", self.r, t)
        if trov_n[0] and trov_c[0] and trov_t[0]:
            cest.append(self.r.pop(trov_n[1]))
            fun.Over_write(fun.cestino, cest)
            fun.Over_write(fun.rubrica, self.r)
        else:
            print("Contatto non trovato")
            print("\n")

    def Stampa(self):
        if self.r == []:
            return "Rubrica vuota"
        else:
            a = fun.Stampa(fun.rubrica)
            return a

    def Reset(self):
        cest = json.loads(fun.Stampa(fun.cestino))
        if self.r == []:
            print("Non ci sono contatti", "\n")
        else:
            cest.append(self.r)
            self.r = []
            fun.Over_write(fun.cestino, cest)
            fun.Over_write(fun.rubrica, self.r)
            print("Rubrica Eliminata", "\n")

    def Backup(self):
        if self.r == []:
            print("Non ci sono contatti")
        else:
            b = input("Nome del file in cui eseguire il backup: ")
            b += ".dat"
            fun.Over_write(b, self.r)
            print("Backup effetuato")
        print("\n")