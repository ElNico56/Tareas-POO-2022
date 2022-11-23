class Candidate:
    def __init__(self, name, party):
        self.name = name
        self.party = party
        self.votes = 0

    def vote(self):
        self.votes += 1


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
