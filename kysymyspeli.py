# Tästä lähtee meidän superhieno kyssäripeli

def main():
    index = 1
    pisteet = 0
    while index < 3:
        vastaus = input(print("Voiko Google Cloud SDKn asentaa PClle ? k=kyllä, e=ei"))
        if vastaus == "k" or vastaus == "K":
            pisteet += 1
        else:
            print("Ei pistetä")
        index += 1
        vastaus = input(print("Luotko virtuaali koneet VM instancessa ? k=kyllä, e=ei"))
        if vastaus == "k" or vastaus == "K":
            pisteet += 1
        else:
            print("Ei pistetä")
        index += 1
        vastaus = input(print("Oliko ensimmäinen Checkpoin vaikea ? k=kyllä, e=ei"))
        if vastaus == "e" or vastaus == "E":
            pisteet += 1
        else:
            print("Ei pistetä")
        index += 1
    print(f"Sain näin paljon pisteitä (max 3 pistettä) {pisteet}")
        



if __name__ == "__main__":
    main()