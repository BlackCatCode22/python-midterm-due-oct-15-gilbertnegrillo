from Animal import Animal  # import Animal class from Animal.py file


class Hyena(Animal):  # create Hyena class
    # create static class variable to keep track of the number of hyenas created.
    num_of_hyenas = 0

    def __init__(self, name, age, birth_season, color, weight, originating_zoo):
        # increment the static variable num_of_hyenas when a new Hyena object is created
        Hyena.num_of_hyenas += 1

        # call the constructor of the parent class with "Hyena" as the species
        super().__init__("Hyena", name, age, birth_season, color, weight, originating_zoo)
