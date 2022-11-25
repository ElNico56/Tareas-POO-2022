from currency import Country


def main():
    countries = []
    countries.append(Country("Chile", "Peso Chileno", 'CLP'))
    countries.append(Country("España", "Peseta Española", 'ESP'))
    countries.append(Country("Estados Unidos de America", "Dolar Estado Unidense", 'USD'))
    countries.append(Country("Argentina", "Peso Argentino", 'ARS'))
    countries.append(Country("Australia", "Dolar Australiano", 'AUD'))

    while True:
        for i, country in enumerate(countries):
            print(f"\nPais #{i}")
            country.print()
        if input("Desea cambiar el nombre de alguna moneda? (Y/N)\n> ").upper() == "N":
            break
        index = int(input("Que pais desea modificar? (Numero)\n> "))
        countries[index].set_currency(input("Nombre de la nueva moneda\n> "), input("Codigo de la nueva moneda\n> "))

if __name__ == "__main__":
    main()
