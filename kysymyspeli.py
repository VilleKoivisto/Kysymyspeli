# Tästä lähtee meidän superhieno kyssäripeli

def main():
    laskuri = 0

    print("Let the games begin")
    while True:
        kysymys1 = input("Kissa vai Koira? (1) = Kissa, (2) = Koira: ")
        if kysymys1 == "1":
            print("Väärä vastaus :(")
        elif kysymys1 == "2":
            print("Oikea vastaus!!!!")
            laskuri += 1
        else:
            print("Valitse numero 1 tai 2")

        kysymys2 = input("Vasen vai Oikea? (1) = Vasen, (2) = Oikea: ")
        if kysymys2 == "1":
            print("Väärä vastaus :(")
        elif kysymys2 == "2":
            print("Oikea vastaus!!!!")
            laskuri += 1
        else:
            print("Valitse numero 1 tai 2")

        kysymys3 = input("Salaatti vai Pitsa? (1) = Salaatti, (2) = Pitsa: ")
        if kysymys3 == "1":
            print("Väärä vastaus :(")
        elif kysymys3 == "2":
            print("Oikea vastaus!!!!")
            laskuri += 1
        else:
            print("Valitse numero 1 tai 2")
        break
    print(f"Kokonaispistemääräsi on {laskuri} pistettä!")
    if laskuri == 3:
        print("Täydet pisteet, avaa olut hyvillä mielin!")
    elif laskuri == 2:
        print("Hyvät pojot, juo puolikas olut")
    elif laskuri == 1:
        print("Pystyt parempaan!")
    else:
        print("daaaaaaamn...")




if __name__ == "__main__":
    main()