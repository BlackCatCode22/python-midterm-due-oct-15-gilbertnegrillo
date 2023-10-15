class Animal:  # create animal class
    # static class variable to keep track of the number of animals.
    num_of_animals = 0

    def __init__(self, species, name=None, age=99, birth_season="season", color=" a color", weight="99 pounds",
                 originating_zoo=" from where?"):
        self.species = species
        self.name = name
        self.age = age
        self.birth_season = birth_season
        self.color = color
        self.weight = weight
        self.originating_zoo = originating_zoo

        # increment static variable when a new object is created
        Animal.num_of_animals += 1

    @classmethod
    def create_with_species_and_name_only(cls, species: object, name: object) -> object:
        return cls(species, name)

animal_01 = Animal.create_with_species_and_name_only('Hyena', 'Kamari')

animal_02 = Animal('Lion', 'Kiara', 6, 'spring', 'tan', 305, 'Zanzibar, Tanzania')

animal_03 = Animal.create_with_species_and_name_only("Hyena", "Ed")

print("\n\n Color of animal 03 is: " + animal_03.color)

animals = []

for i in range(10):
    if i % 2 == 0:
        animal = Animal.create_with_species_and_name_only('Hyena', f'Name{i}')
    else:
        animal = Animal('Lion', f'Name{i}', i, 'spring', 'tan', 100 + i, 'Zoo{i}')

    animals.append(animal)

print(f'Number of animals created: {Animal.num_of_animals}')

for i, animal in enumerate(animals, start=1):
    print(f'Animal {i}: {animal.species}, {animal.name}, {animal.age} years old')

print(f'Number of animals created: {Animal.num_of_animals}')