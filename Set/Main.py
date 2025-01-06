from Set import Set;
def main():
    antallOperasjoner = int(input("Skriv inn onsket antall operasjoner: "));
    print("Oppretter sett");
    settet = Set();
    print("Naa kommer en loop der du kan utfore " + str(antallOperasjoner) + " operasjon paa settet");
    for i in range(0, antallOperasjoner):
        operasjon = input();
        operasjon = operasjon.split(" ");
        if (operasjon[0] == "contains"):
            #print("valgt contains ");
            searchedElement = int(operasjon[1]);
            print(settet.contains(searchedElement));

        elif (operasjon[0] == "insert"):
            insertedElement = int(operasjon[1]);
            settet.insert(insertedElement);

        elif (operasjon[0] == "remove"): 
            removedElement = int(operasjon[1]);
            settet.remove(removedElement);

        elif (operasjon[0] == "size"):
            print(settet.size());

        else:
            print("ukjent input");
main();