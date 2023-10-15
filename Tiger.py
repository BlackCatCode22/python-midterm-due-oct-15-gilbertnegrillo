from Animal import Animal  # import Animal module from Animal.py file


class Tiger(Animal):  # create Tiger class
    # create static class variable to keep track of the number of tigers created.
    num_of_tigers = 0

    def __init__(self, name, age, birth_season, color, weight, originating_zoo):
        # increment the static variable num_of_tigers when a new Tiger object is created
        Tiger.num_of_tigers += 1

        # call the constructor of the parent class with "Tiger" as the species
        super().__init__("Tiger", name, age, birth_season, color, weight, originating_zoo)
