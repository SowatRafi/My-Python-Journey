class UK():
    def capital_City(self):
        print("London is the capital of UK")

    def language(self):
        print("English is the primary language.")


class FRN():
    def capital_City(self):
        print("Paris is the capital of UK")

    def language(self):
        print("French is the primary language.")


def Europe(eu):
    eu.capital_City()
    eu.language()


country1 = UK()
# country1.capital_City()

country2 = FRN()
# country2.capital_City()
#
# for c in (country1, country2):
#     c.capital_City()
#     c.language()

Europe(country1)
Europe(country2)