from Animal import Animal  # import Animal module from Animal.py file


class Bear(Animal):  # create Bear class
    # create static class variable to keep track of the number of bears created.
    num_of_bears = 0

    def __init__(self, name, age, birth_season, color, weight, originating_zoo):
        # increment the static variable num_of_bears when a new Bear object is created
        Bear.num_of_bears += 1

        # call the constructor of the parent class with "Bear" as the species
        super().__init__("Bear", name, age, birth_season, color, weight, originating_zoo)
