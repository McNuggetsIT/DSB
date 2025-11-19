class Gusto:
    def __init__(self,nome,prezzo,allrg):
        self._nome = nome
        self._prezzo = prezzo
        self._allrg = allrg
    
    def get_nome(self):
        return self._nome
    
    def get_prezzo(self):
        return self._prezzo
    
    def get_allrg(self):
        return self._allrg
    
    def set_nome(self, n_nome):
        if n_nome:
            self._nome = n_nome
            
    def set_prezzo(self, n_prezzo):
        if n_prezzo:
            self._prezzo = n_prezzo
            
    def set_allrg(self, n_allrg):
        if n_allrg:
            self._allrg = n_allrg
            
    def descrizione(self):
        allergeni_str = ", ".join(self._allrg) if self._allrg else "Nessuno"
        return f"Gusto: {self._nome} | Prezzo: €{self._prezzo:.2f} | Allergeni: {allergeni_str}"