def main():
    menu = MenuGelateria()
    nGusti = input("Quanti gusti vuoi creare? ")
    print(f"=== CREAZIONE {nGusti} GUSTI BASE ===")
    for i in range(nGusti):
        nome = input(f"Gusto base {i+1} nome: ")
        prezzo = float(input(f"Prezzo {i+1} prezzo: "))
        allergeni = input("Allergeni separati da virgola (lascia vuoto se nessuno): ").split(",")
        allergeni = [a.strip() for a in allergeni if a]
        menu.aggiungi_gusto(Gusto(nome, prezzo, allergeni))
        
    nGustiPremium = input("Quanti gusti vuoi creare? ")


    print(f"=== CREAZIONE {nGustiPremium} GUSTI PREMIUM ===")
    for i in range(nGustiPremium):
        nome = input(f"Gusto premium {i+1} nome: ")
        prezzo = float(input(f"Gusto premium {i+1} prezzo: "))
        allergeni = input("Allergeni separati da virgola (lascia vuoto se nessuno): ").split(",")
        allergeni = [a.strip() for a in allergeni if a]
        ingredienti = input("Ingredienti speciali separati da virgola: ").split(",")
        ingredienti = [ing.strip() for ing in ingredienti if ing]
        sovrapprezzo = float(input("Sovrapprezzo: "))
        menu.aggiungi_gusto(GustoPremium(nome, prezzo, allergeni, ingredienti, sovrapprezzo))

    print("=== CREAZIONE 1 GUSTO VEGANO ===")
    nome = input("Gusto vegano nome: ")
    prezzo = float(input("Gusto vegano prezzo: "))
    allergeni = input("Allergeni separati da virgola (lascia vuoto se nessuno): ").split(",")
    allergeni = [a.strip() for a in allergeni if a]
    base = input("Base vegetale (es. soia, mandorla, cocco): ")
    menu.aggiungi_gusto(GustoVegano(nome, prezzo, allergeni, base))

    # Menu interattivo
    while True:
        print("\n--- MENU GELATERIA ---")
        print("1. Visualizza gusti")
        print("2. Rimuovi un gusto")
        print("3. Esci")
        scelta = input("Scegli un'opzione: ")

        match scelta:
            case "1":
                print("\nElenco gusti:")
                menu.lista_gusti()
            case "2":
                nome_rimozione = input("Nome gusto da rimuovere: ")
                menu.rimuovi_gusto(nome_rimozione)
                print(f"Gusto '{nome_rimozione}' rimosso (se presente).")
            case "3":
                print("Arrivederci!")
                break
            case _:
                print("Opzione non valida, riprova.")


if __name__ == "__main__":
    main()