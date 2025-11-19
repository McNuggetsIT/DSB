# DSB

D'Avanzo Sorrentino Brescia repository

🧩 Component 1: Gusto

Classe base sviluppata da D'Avanzo.  
Contiene attributi privati (`_nome`, `_prezzo_base`, `_allergeni`) con getter/setter e il metodo `descrizione()` per mostrare le info del gusto.  
Serve da base per le estensioni `MenuGusto` e `SottoClassi` come `gustoPremium` e `gustoVegano`.

Component 2:

Sviluppato da Sorrentino Gianmarco.
Creazione sottoclasse GustoPremium(Gusto) che eredita da gusto gli attributi nome , prezzo base e allergeni, aggiungendo due suoi attributi ovvero ingredienti speciali e sovrapprezzo.
Inoltre è stato definito un metodo descrizione premium che ci mostra la descrizione base presente nel componente Gusto aggiungendoci gli ingredienti speciali e il sovraprezzo

Creazione sottoclasse GustoVegano(Gusto) anche essa eredita gli attributi dalla classe padre Gusto , aggiungedoci però
l'attributo base vegetale. Anche qui è stato definito un metodo descrizione vegano che ci mostra sempre la descrizione base ma aggiungendo appunto base vegetale
