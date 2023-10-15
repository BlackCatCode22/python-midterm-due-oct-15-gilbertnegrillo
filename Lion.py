from Animal import Animal  # import Animal module from Animal.py file


class Lion(Animal):  # crate Lion class
    # create static class variable to keep track of the number of lions created.
    num_of_lions = 0

    def __init__(self, name, age, birth_season, color, weight, originating_zoo):
        # increment the static variable num_of_lions when a new Lion object is created
        Lion.num_of_lions += 1

        # call the constructor of the parent class with "Lion" as the species
        super().__init__("Lion", name, age, birth_season, color, weight, originating_zoo)
