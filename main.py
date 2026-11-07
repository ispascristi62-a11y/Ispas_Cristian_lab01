def citeste_sir_consola():
    print("--- Citire șir de la tastatură ---")
    intrare = input("Introduceți numerele separate prin spațiu: ")
    sir = [float(x) for x in intrare.split()]
    return sir


def citeste_matrice_consola():
    print("\n--- Citire matrice de la tastatură ---")
    linii = int(input("Introduceți numărul de linii: "))
    coloane = int(input("Introduceți numărul de coloane: "))

    matrice = []
    for i in range(linii):
        linie_input = input(
            f"Introduceți elementele liniei {i + 1} ({coloane} numere separate prin spațiu): "
        )
        elemente = [float(x) for x in linie_input.split()]
        matrice.append(elemente)

    return matrice


# === ADAUGAT PENTRU CERINȚA 2 ===
def citeste_sir_fisier():
    print("\n--- Citire șir din fișier ---")
    nume_fisier = input(
        "Introduceți numele fișierului (ex: date.txt): "
    ).strip()

    try:
        with open(nume_fisier, "r") as f:
            continut = f.read()
            sir = [float(x) for x in continut.split()]
            return sir
    except FileNotFoundError:
        print(f"Eroare: Fișierul '{nume_fisier}' nu a fost găsit!")
        return None


def afiseaza_sir(sir):
    if sir is not None:
        print("\nȘirul citit este:")
        print(" ".join(str(x) for x in sir))


def afiseaza_matrice(matrice):
    if matrice is not None:
        print("\nMatricea citită este:")
        for linie in matrice:
            print("\t".join(str(x) for x in linie))


if __name__ == "__main__":
    # Poți testa consola (sau o poți lăsa comentată dacă testezi doar fișierul)
    sir = citeste_sir_consola()
    afiseaza_sir(sir)

    # Noul test pentru fișier (citește din date.txt)
    sir_fisier = citeste_sir_fisier()
    afiseaza_sir(sir_fisier)