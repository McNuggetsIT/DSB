from moduli.gusto import Gusto

class GustoPremium(Gusto):
    def __init__(self, nome, prezzo_base, allrg ,ingredienti_speciali,sovraprezzo):
        super().__init__(nome,prezzo_base,allrg)
        self.__ingredienti_speciali = ingredienti_speciali
        self.__sovrapprezzo = sovraprezzo
        
    def descrizione_premium(self):
        super().descrizione()
        return f"Descrizione extra: Gusto:{self._nome} Prezzo:{self._prezzo_base:.2f} allrg:{self._allrg} Ingredienti Speciali: {self.__ingredienti_speciali} Sovrapprezzo: {self.__sovrapprezzo}"
    


class GustoVegano(Gusto):
    def __init__(self,nome,prezzo_base,allrg,base_vegetale):
        super().__init__(nome,prezzo_base,allrg)
        self._base_vegetale = base_vegetale
        
    def descrizione_vegano(self):
        super().descrizione()
        return f"Descrizine Vegano: Gusto:{self._nome} Prezzo:{self._prezzo_base:.2f} allrg:{self._allrg} Base Vegetale: {self._base_vegetale}"