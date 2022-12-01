class Candidate:
    def __init__(self, name, party):
        self._name = name
        self._party = party
        self._votes = 0

    @property
    def name(self):
        return self._name

    @property
    def party(self):
        return self._party

    @property
    def votes(self):
        return self._votes

    def vote(self):
        self._votes += 1


candidates = []
candidates.append(Candidate("Gohan", "Blue"))
candidates.append(Candidate("Nico", "Red"))

while True:
    if input("Añadir un candidato? (Y/N)\n> ").upper() == "N":
        break
    name = input("Ingrese nombre\n> ")
    party = input("Ingrese partido\n> ")
    candidates.append(Candidate(name, party))

while True:
    print("\nElija un candidato para votar")
    for i in range(len(candidates)):
        print(
            f"({i}) Para votar por: "
            + candidates[i].name
            + "		Party: "
            + candidates[i].party
            + "		Votes: "
            + str(candidates[i].votes)
        )
    candidates[int(input("> "))].vote()
