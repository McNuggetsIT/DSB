#---------------------------------------------------------
#---------------------------------------------------------
#---------------CLASSE MENUGELATERIA BRESCIA -------------
#---------------------------------------------------------

class MenuGelateria:
    def __init__(self):
        self._gusti = []

    def aggiungi_gusto(self, gusto):
        self._gusti.append(gusto)

    def rimuovi_gusto(self, nome_gusto):
        nuovi_gusti = []
        for g in self._gusti:
            if g.get_nome() != nome_gusto:
                nuovi_gusti.append(g)
        self._gusti = nuovi_gusti

    def lista_gusti(self):
        # Stampa la descrizione di tutti i gusti
        for g in self._gusti:
            print(g.descrizione())
            
