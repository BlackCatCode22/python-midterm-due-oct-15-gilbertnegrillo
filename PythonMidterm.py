#  Name: Gilbert Negrillo

#  Class: CIT-95

#  Date: October 9, 2023

# References: GitHub Google Classroom midterm program check-in and video,
# ChatGPT, Python midterm approved solution video

from datetime import date  # import datetime module
from Animal import Animal  # import Animal class from Animal.py file
from Hyena import Hyena  # import Hyena class from Hyena.py file
from Lion import Lion  # import Lion class from Lion.py file
from Tiger import Tiger  # import Tiger class from Tiger.py file
from Bear import Bear  # import Bear clas from Bear.py file


def gen_birth_day(years_old, birth_season):  # gen_birth_day function
    #  takes two parameters
    birth_year = 2023 - int(years_old.strip())  # calculate birthday

    birth_year = birth_year - 1

    #  If/elif statement
    if birth_season == "spring,":
        month_day = "03-21"
    elif birth_season == "summer,":
        month_day = "06-21"
    elif birth_season == "fall,":
        month_day = "09-21"
    elif birth_season == "winter,":
        month_day = "12-21"
    else:
        month_day = "01-01"

    animal_birthday = str(birth_year) + "-" + month_day

    return animal_birthday


def gen_unique_animal_id(species_name, num_of_species):  # gen_unique_animal_id() function
    #  takes two parameters

    # if/elif statement
    if species_name == "Hyena":
        prefix = "Hy"
    elif species_name == "Lion":
        prefix = "Li"
    elif species_name == "Tiger":
        prefix = "Ti"
    elif species_name == "Bear":
        prefix = "Be"
    else:
        prefix = "Er"

    return prefix + "0" + str(num_of_species)


def gen_animal_name(species, num_of_animals):  # gen_animal_name() function
    # takes two parameters

    # if/elif statement
    if species == "Hyena":
        hyena_names = ["Shenzi", "Banzai", "Ed", "Zig", "Bud",
                       "Lou", "Kamari", "Wema", "Nne", "Madoa", "Prince Nevarah"]
        name_index = num_of_animals % len(hyena_names)
        return hyena_names[name_index]
    elif species == "Lion":
        lion_names = ["Scar", "Mufasa", "Simba", "Kiara", "King", "Drooper",
                      "Kimba", "Nala", "Leo", "Samson", "Elsa", "Cecil"]
        name_index = num_of_animals % len(lion_names)
        return lion_names[name_index]
    elif species == "Tiger":
        tiger_names = ["Tony", "Tigger", "Amber", "Cosimia", "Cuddles",
                       "Dave", "Jiba", "Rajah", "Rayas", "Ryker"]
        name_index = num_of_animals % len(tiger_names)
        return tiger_names[name_index]
    elif species == "Bear":
        bear_names = ["Yogi", "Smokey", "Paddington", "Lippy", "Bungle",
                      "Baloo", "Rupert", "Winnie the Pooh", "Snuggles", "Bert"]
        name_index = num_of_animals % len(bear_names)
        return bear_names[name_index]
    else:
        return "Unknown"


def gen_zoo_habitat(species):
    if species == "Hyena":
        print(f"\nHyena Habitat\n")
        for hyena in hyena_habitat:
            print(f"{hyena.unique_id}; {hyena.name}; {hyena.age} years old; birthdate "
                  f"{hyena.birth_date}; {hyena.color} color; {hyena.gender}; "
                  f"{hyena.weight} pounds; from {hyena.originating_zoo}; arrived {hyena.arrival_date}\n")
        return f"Number of Hyenas: {Hyena.num_of_hyenas}"
    elif species == "Lion":
        print(f"\nLion Habitat\n")
        for lion in lion_habitat:
            print(f"{lion.unique_id}; {lion.name}; {lion.age} years old; birthdate "
                  f"{lion.birth_date}; {lion.color} color; {lion.gender}; "
                  f"{lion.weight} pounds; from {lion.originating_zoo}; arrived {lion.arrival_date}\n")
        return f"Number of Lions: {Lion.num_of_lions}"
    elif species == "Tiger":
        print(f"\nTiger Habitat\n")
        for tiger in tiger_habitat:
            print(f"{tiger.unique_id}; {tiger.name}; {tiger.age} years old; birthdate "
                  f"{tiger.birth_date}; {tiger.color} color; {tiger.gender}; "
                  f"{tiger.weight} pounds; from {tiger.originating_zoo}; arrived {tiger.arrival_date}\n")
        return f"Number of Tigers: {Tiger.num_of_tigers}"
    elif species == "Bear":
        print(f"\nBear Habitat\n")
        for bear in bear_habitat:
            print(f"{bear.unique_id}; {bear.name}; {bear.age} years old; birthdate "
                  f"{bear.birth_date}; {bear.color} color; {bear.gender}; "
                  f"{bear.weight} pounds; from {bear.originating_zoo}; arrived {bear.arrival_date}\n")
        return f"Number of Bears: {Bear.num_of_bears}"
    

input_file_path = open("C:/Users/bertn/PyCharmProjects/python-midterm-due-oct-15-gilbertnegrillo/arrivingAnimals.txt",
                       "r")  # open arrivingAnimals.txt file and read
# the information
Lines = input_file_path.readlines()  # use readlines() function to read the
# contents line by line
count = 0
for line in Lines:  # for/in loop
    count += 1
    print(line.strip())

try:  # Try block
    with open('arrivingAnimals.txt', 'r') as file:  # open arrivingAnimals.txt file and parse each line
        for line in file:  # for/in loop
            data = line.strip().split(', ')  # use split() function to split into individual data pieces.
            age = data[0]  # get age data
            species = data[1]  # get species data
            birth_season = [2]  # get birth_season data
            color = [3]  # get color data
            weight = [4]  # get weight data
            originating_zoo = [5]  # get originating_zoo data

except FileNotFoundError:  # Except block
    print(f"Error: The file '{input_file_path}' was not found")

except IOError as e:
    print(f"An error occurred: {str(e)}")


# initialize lists for each species
hyena_habitat = []
lion_habitat = []
tiger_habitat = []
bear_habitat = []

print()

# create hyena object
hyena = Hyena("Banzai", 4, "spring", "tan", 70, "Friguia Park, Tunisia")
hyena.unique_id = gen_unique_animal_id("Hyena", hyena.num_of_hyenas)  # call gen_unique_animal_id function.
# Takes two arguments.
hyena.name = gen_animal_name("Hyena", 1)  # call gen_animal_name function.
# Takes two arguments.
hyena.gender = "female"  # set hyena gender using gender method
hyena.birth_date = gen_birth_day(str(3), "spring,")  # call gen_birth_day function.
# Takes two arguments.
hyena.arrival_date = date.today()  # arrival date
# use date.today() from datetime module
hyena_habitat.append(hyena)  # append first hyena object to hyena_habitat
# output information about hyena object
print(f"Hyena name: {hyena.name}")
print(f"Species: {hyena.species}")
print(f"Gender: {hyena.gender}")
print(f"Age: {hyena.age} years old")
print(f"Color: {hyena.color} color")
print(f"Weight: {hyena.weight} pounds")
print(f"Originating Zoo: from {hyena.originating_zoo}")
print(f"Unique ID: {hyena.unique_id}")
print(f"Birthdate: {hyena.birth_date}")
print(f"Arrival date: {hyena.arrival_date}")
print(f"{hyena.unique_id}; {hyena.name}; {hyena.age} years old; birthdate "
      f"{hyena.birth_date}; {hyena.color} color; {hyena.gender}; "
      f"{hyena.weight} pounds; from {hyena.originating_zoo}; arrived {hyena.arrival_date}\n")
print(f"Number of hyenas: {hyena.num_of_hyenas}")

print()

# create second hyena object
hyena2 = Hyena("Ed", 12, "fall", "brown", 150, "Friguia Park, Tunisia")
hyena2.unique_id = gen_unique_animal_id("Hyena", hyena2.num_of_hyenas)
hyena2.name = gen_animal_name("Hyena", 2)
hyena2.gender = "male"
hyena2.birth_date = gen_birth_day(str(11), "fall,")
hyena2.arrival_date = date.today()
hyena_habitat.append(hyena2)  # append second hyena object to hyena_habitat
# output information about hyena object
print(f"Hyena name: {hyena2.name}")
print(f"Species: {hyena2.species}")
print(f"Gender: {hyena2.gender}")
print(f"Age: {hyena2.age} years old")
print(f"Color: {hyena2.color} color")
print(f"Weight: {hyena2.weight} pounds")
print(f"Originating Zoo: from {hyena2.originating_zoo}")
print(f"Unique ID: {hyena2.unique_id}")
print(f"Birthdate: {hyena2.birth_date}")
print(f"Arrival date: {hyena2.arrival_date}")
print(f"{hyena2.unique_id}; {hyena2.name}; {hyena2.age} years old; birthdate "
      f"{hyena2.birth_date}; {hyena2.color} color; {hyena2.gender}; "
      f"{hyena2.weight} pounds; from {hyena2.originating_zoo}; arrived {hyena2.arrival_date}\n")
print(f"Number of hyenas: {hyena2.num_of_hyenas}")

print()

# create third hyena object.
hyena3 = Hyena("Zig", 4, "spring", "black", 120, "Friguia Park, Tunisia")
hyena3.unique_id = gen_unique_animal_id("Hyena", hyena3.num_of_hyenas)
hyena3.name = gen_animal_name("Hyena", 3)
hyena3.gender = "male"
hyena3.birth_date = gen_birth_day(str(3), "spring,")
hyena3.arrival_date = date.today()
hyena_habitat.append(hyena3)  # append third hyena object to hyena_habitat
# output information about hyena object
print(f"Hyena name: {hyena3.name}")
print(f"Species: {hyena3.species}")
print(f"Gender: {hyena3.gender}")
print(f"Age: {hyena3.age} years old")
print(f"Color: {hyena3.color} color")
print(f"Weight: {hyena3.weight} pounds")
print(f"Originating Zoo: from {hyena3.originating_zoo}")
print(f"Unique ID: {hyena3.unique_id}")
print(f"Birthdate: {hyena3.birth_date}")
print(f"Arrival date: {hyena3.arrival_date}")
print(f"{hyena3.unique_id}; {hyena3.name}; {hyena3.age} years old; birthdate "
      f"{hyena3.birth_date}; {hyena3.color} color; {hyena3.gender}; "
      f"{hyena3.weight} pounds; from {hyena3.originating_zoo}; arrived {hyena3.arrival_date}\n")
print(f"Number of hyenas: {hyena3.num_of_hyenas}")

print()

# create fourth hyena object
hyena4 = Hyena("Bud", 8, "unknown", "black and tan striped", 105, "Friguia Park, Tunisia")
hyena4.unique_id = gen_unique_animal_id("Hyena", hyena4.num_of_hyenas)
hyena4.name = gen_animal_name("Hyena", 4)
hyena4.gender = "female"
hyena4.birth_date = gen_birth_day(str(7), "unknown,")
hyena4.arrival_date = date.today()
hyena_habitat.append(hyena4)  # append fourth hyena object to hyena_habitat
# output information about hyena object
print(f"Hyena name: {hyena4.name}")
print(f"Species: {hyena4.species}")
print(f"Gender: {hyena4.gender}")
print(f"Age: {hyena4.age} years old")
print(f"Color: {hyena4.color} color")
print(f"Weight: {hyena4.weight} pounds")
print(f"Originating Zoo: from {hyena4.originating_zoo}")
print(f"Unique ID: {hyena4.unique_id}")
print(f"Birthdate: {hyena4.birth_date}")
print(f"Arrival date: {hyena4.arrival_date}")
print(f"{hyena4.unique_id}; {hyena4.name}; {hyena4.age} years old; birthdate "
      f"{hyena4.birth_date}; {hyena4.color} color; {hyena4.gender}; "
      f"{hyena4.weight} pounds; from {hyena4.originating_zoo}; arrived {hyena4.arrival_date}\n")
print(f"Number of hyenas: {hyena4.num_of_hyenas}")

print()

lion = Lion("Mufasa", 6, "spring", "tan", 300, "Zanzibar, Tanzania")
lion.unique_id = gen_unique_animal_id("Lion", lion.num_of_lions)  # call gen_unique_animal_id function.
# Takes two arguments.
lion.name = gen_animal_name("Lion", 1)  # call gen_animal_name function.
# Takes two arguments.
lion.gender = "female"  # set lion gender using gender method
lion.birth_date = gen_birth_day(str(5), "spring,")  # call gen_birth_day function.
# Takes two arguments.
lion.arrival_date = date.today()  # arrival date
# use date.today() from datetime module
lion_habitat.append(lion)  # append first lion object to lion_habitat
# output information about lion object
print(f"Lion name: {lion.name}")
print(f"Species: {lion.species}")
print(f"Gender: {lion.gender}")
print(f"Age: {lion.age} years old")
print(f"Color: {lion.color} color")
print(f"Weight: {lion.weight} pounds")
print(f"Originating Zoo: from {lion.originating_zoo}")
print(f"Unique ID: {lion.unique_id}")
print(f"Birthdate: {lion.birth_date}")
print(f"Arrival date: {lion.arrival_date}")
print(f"{lion.unique_id}; {lion.name}; {lion.age} years old; birthdate "
      f"{lion.birth_date}; {lion.color} color; {lion.gender}; "
      f"{lion.weight} pounds; from {lion.originating_zoo}; arrived {lion.arrival_date}\n")
print(f"Number of lions: {lion.num_of_lions}")

print()

lion2 = Lion("Simba", 12, "winter", "dark tan", 375, "KopeLion, Tanzania")
lion2.unique_id = gen_unique_animal_id("Lion", lion2.num_of_lions)
lion2.name = gen_animal_name("Lion", 2)
lion2.gender = "female"
lion2.birth_date = gen_birth_day(str(11), "winter,")
lion2.arrival_date = date.today()
lion_habitat.append(lion2)  # append second lion object to lion_habitat
# output information about lion object
print(f"Lion name: {lion2.name}")
print(f"Species: {lion2.species}")
print(f"Gender: {lion2.gender}")
print(f"Age: {lion2.age} years old")
print(f"Color: {lion2.color} color")
print(f"Weight: {lion2.weight} pounds")
print(f"Originating Zoo: from {lion2.originating_zoo}")
print(f"Unique ID: {lion2.unique_id}")
print(f"Birthdate: {lion2.birth_date}")
print(f"Arrival date: {lion2.arrival_date}")
print(f"{lion2.unique_id}; {lion2.name}; {lion2.age} years old; birthdate "
      f"{lion2.birth_date}; {lion2.color} color; {lion2.gender}; "
      f"{lion2.weight} pounds; from {lion2.originating_zoo}; arrived {lion2.arrival_date}\n")
print(f"Number of lions: {lion2.num_of_lions}")

print()

lion3 = Lion("Kiara", 22, "fall", "golden", 450, "Zanzibar, Tanzania")
lion3.unique_id = gen_unique_animal_id("Lion", lion3.num_of_lions)
lion3.name = gen_animal_name("Lion", 3)
lion3.gender = "male"
lion3.birth_date = gen_birth_day(str(21), "fall,")
lion3.arrival_date = date.today()
lion_habitat.append(lion3)  # append third lion object to lion_habitat
# output information about lion object
print(f"Lion name: {lion3.name}")
print(f"Species: {lion3.species}")
print(f"Gender: {lion3.gender}")
print(f"Age: {lion3.age} years old")
print(f"Color: {lion3.color} color")
print(f"Weight: {lion3.weight} pounds")
print(f"Originating Zoo: from {lion3.originating_zoo}")
print(f"Unique ID: {lion3.unique_id}")
print(f"Birthdate: {lion3.birth_date}")
print(f"Arrival date: {lion3.arrival_date}")
print(f"{lion3.unique_id}; {lion3.name}; {lion3.age} years old; birthdate "
      f"{lion3.birth_date}; {lion3.color} color; {lion3.gender}; "
      f"{lion3.weight} pounds; from {lion3.originating_zoo}; arrived {lion3.arrival_date}\n")
print(f"Number of lions: {lion3.num_of_lions}")

print()

lion4 = Lion("King", 4, "spring", "tan and brown", 275, "KopeLion, Tanzania")
lion4.unique_id = gen_unique_animal_id("Lion", lion4.num_of_lions)
lion4.name = gen_animal_name("Lion", 4)
lion4.gender = "female"
lion4.birth_date = gen_birth_day(str(3), "spring,")
lion4.arrival_date = date.today()
lion_habitat.append(lion4)  # append fourth lion object to lion_habitat
# output information about lion object
print(f"Lion name: {lion4.name}")
print(f"Species: {lion4.species}")
print(f"Gender: {lion4.gender}")
print(f"Age: {lion4.age} years old")
print(f"Color: {lion4.color} color")
print(f"Weight: {lion4.weight} pounds")
print(f"Originating Zoo: from {lion4.originating_zoo}")
print(f"Unique ID: {lion4.unique_id}")
print(f"Birthdate: {lion4.birth_date}")
print(f"Arrival date: {lion4.arrival_date}")
print(f"{lion4.unique_id}; {lion4.name}; {lion4.age} years old; birthdate "
      f"{lion4.birth_date}; {lion4.color} color; {lion4.gender}; "
      f"{lion4.weight} pounds; from {lion4.originating_zoo}; arrived {lion4.arrival_date}\n")
print(f"Number of lions: {lion4.num_of_lions}")

print()

tiger = Tiger("Tigger", 2, "spring", "gold and tan", 270, "Dhaka, Bangladesh")
tiger.unique_id = gen_unique_animal_id("Tiger", tiger.num_of_tigers)  # call gen_unique_animal_id function.
# Takes two arguments.
tiger.name = gen_animal_name("Tiger", 1)  # call gen_animal_name function.
# Takes two arguments.
tiger.gender = "male"  # set tiger gender using gender method
tiger.birth_date = gen_birth_day(str(1), "spring,")  # call gen_birth_day function.
# Takes two arguments.
tiger.arrival_date = date.today()  # arrival date
# use date.today() from datetime module
tiger_habitat.append(tiger)  # append first tiger object to tiger_habitat
# output information about tiger object
print(f"Tiger name: {tiger.name}")
print(f"Species: {tiger.species}")
print(f"Gender: {tiger.gender}")
print(f"Age: {tiger.age} years old")
print(f"Color: {tiger.color} color")
print(f"Weight: {tiger.weight} pounds")
print(f"Originating Zoo: from {tiger.originating_zoo}")
print(f"Unique ID: {tiger.unique_id}")
print(f"Birthdate: {tiger.birth_date}")
print(f"Arrival date: {tiger.arrival_date}")
print(f"{tiger.unique_id}; {tiger.name}; {tiger.age} years old; birthdate "
      f"{tiger.birth_date}; {tiger.color} color; {tiger.gender}; "
      f"{tiger.weight} pounds; from {tiger.originating_zoo}; arrived {tiger.arrival_date}\n")
print(f"Number of tigers: {tiger.num_of_tigers}")

print()

tiger2 = Tiger("Amber", 4, "spring", "black stripes", 400, "Dhaka, Bangladesh")
tiger2.unique_id = gen_unique_animal_id("Tiger", tiger2.num_of_tigers)
tiger2.name = gen_animal_name("Tiger", 2)
tiger2.gender = "female"
tiger2.birth_date = gen_birth_day(str(3), "spring,")
tiger2.arrival_date = date.today()
tiger_habitat.append(tiger2)  # append second tiger object to tiger_habitat
# output information about tiger object
print(f"Tiger name: {tiger2.name}")
print(f"Species: {tiger2.species}")
print(f"Gender: {tiger2.gender}")
print(f"Age: {tiger2.age} years old")
print(f"Color: {tiger2.color} color")
print(f"Weight: {tiger2.weight} pounds")
print(f"Originating Zoo: from {tiger2.originating_zoo}")
print(f"Unique ID: {tiger2.unique_id}")
print(f"Birthdate: {tiger2.birth_date}")
print(f"Arrival date: {tiger2.arrival_date}")
print(f"{tiger2.unique_id}; {tiger2.name}; {tiger2.age} years old; birthdate "
      f"{tiger2.birth_date}; {tiger2.color} color; {tiger2.gender}; "
      f"{tiger2.weight} pounds; from {tiger2.originating_zoo}; arrived {tiger2.arrival_date}\n")
print(f"Number of tigers: {tiger2.num_of_tigers}")

print()

tiger3 = Tiger("Cosimia", 18, "fall", "gold and tan", 300, "Bardia, Nepal")
tiger3.unique_id = gen_unique_animal_id("Tiger", tiger3.num_of_tigers)
tiger3.name = gen_animal_name("Tiger", 3)
tiger3.gender = "male"
tiger3.birth_date = gen_birth_day(str(17), "fall,")
tiger3.arrival_date = date.today()
tiger_habitat.append(tiger3)  # append third tiger object to tiger_habitat
# output information about tiger object
print(f"Tiger name: {tiger3.name}")
print(f"Species: {tiger3.species}")
print(f"Gender: {tiger3.gender}")
print(f"Age: {tiger3.age} years old")
print(f"Color: {tiger3.color} color")
print(f"Weight: {tiger3.weight} pounds")
print(f"Originating Zoo: from {tiger3.originating_zoo}")
print(f"Unique ID: {tiger3.unique_id}")
print(f"Birthdate: {tiger3.birth_date}")
print(f"Arrival date: {tiger3.arrival_date}")
print(f"{tiger3.unique_id}; {tiger3.name}; {tiger3.age} years old; birthdate "
      f"{tiger3.birth_date}; {tiger3.color} color; {tiger3.gender}; "
      f"{tiger3.weight} pounds; from {tiger3.originating_zoo}; arrived {tiger3.arrival_date}\n")
print(f"Number of tigers: {tiger3.num_of_tigers}")

print()

tiger4 = Tiger("Cuddles", 3, "spring", "black stripes", 285, "Bardia, Nepal")
tiger4.unique_id = gen_unique_animal_id("Tiger", tiger4.num_of_tigers)
tiger4.name = gen_animal_name("Tiger", 4)
tiger4.gender = "female"
tiger4.birth_date = gen_birth_day(str(2), "spring,")
tiger4.arrival_date = date.today()
tiger_habitat.append(tiger4)  # append fourth tiger object to tiger_habitat
# output information about tiger object
print(f"Tiger name: {tiger4.name}")
print(f"Species: {tiger4.species}")
print(f"Gender: {tiger4.gender}")
print(f"Age: {tiger4.age} years old")
print(f"Color: {tiger4.color} color")
print(f"Weight: {tiger4.weight} pounds")
print(f"Originating Zoo: from {tiger4.originating_zoo}")
print(f"Unique ID: {tiger4.unique_id}")
print(f"Birthdate: {tiger4.birth_date}")
print(f"Arrival date: {tiger4.arrival_date}")
print(f"{tiger4.unique_id}; {tiger4.name}; {tiger4.age} years old; birthdate "
      f"{tiger4.birth_date}; {tiger4.color} color; {tiger4.gender}; "
      f"{tiger4.weight} pounds; from {tiger4.originating_zoo}; arrived {tiger4.arrival_date}\n")
print(f"Number of tigers: {tiger4.num_of_tigers}")

print()

bear = Bear("Smokey", 7, "spring", "brown", 320, "Alaska Zoo, Alaska")
bear.unique_id = gen_unique_animal_id("Bear", bear.num_of_bears)  # call gen_unique_animal_id function.
# Takes two arguments.
bear.name = gen_animal_name("Bear", 1)  # call gen_animal_name function.
# Takes two arguments.
bear.gender = "male"  # set bear gender using gender method
bear.birth_date = gen_birth_day(str(6), "spring,")  # call gen_birth_day function.
# Takes two arguments.
bear.arrival_date = date.today()  # arrival date
# use date.today() from datetime module
bear_habitat.append(bear)  # append first bear object to bear_habitat
# output information about bear object
print(f"Bear name: {bear.name}")
print(f"Species: {bear.species}")
print(f"Gender: {bear.gender}")
print(f"Age: {bear.age} years old")
print(f"Color: {bear.color} color")
print(f"Weight: {bear.weight} pounds")
print(f"Originating Zoo: from {bear.originating_zoo}")
print(f"Unique ID: {bear.unique_id}")
print(f"Birthdate: {bear.birth_date}")
print(f"Arrival date: {bear.arrival_date}")
print(f"{bear.unique_id}; {bear.name}; {bear.age} years old; birthdate "
      f"{bear.birth_date}; {bear.color} color; {bear.gender}; "
      f"{bear.weight} pounds; from {bear.originating_zoo}; arrived {bear.arrival_date}\n")
print(f"Number of bears: {bear.num_of_bears}")

print()

bear2 = Bear("Paddington", 25, "spring", "black", 425, "Woodland park zoo, Washington")
bear2.unique_id = gen_unique_animal_id("Bear", bear2.num_of_bears)
bear2.name = gen_animal_name("Bear", 2)
bear2.gender = "female"
bear2.birth_date = gen_birth_day(str(24), "spring,")
bear2.arrival_date = date.today()
bear_habitat.append(bear2)  # append second bear object to bear_habitat
# output information about bear object
print(f"Bear name: {bear2.name}")
print(f"Species: {bear2.species}")
print(f"Gender: {bear2.gender}")
print(f"Age: {bear2.age} years old")
print(f"Color: {bear2.color} color")
print(f"Weight: {bear2.weight} pounds")
print(f"Originating Zoo: from {bear2.originating_zoo}")
print(f"Unique ID: {bear2.unique_id}")
print(f"Birthdate: {bear2.birth_date}")
print(f"Arrival date: {bear2.arrival_date}")
print(f"{bear2.unique_id}; {bear2.name}; {bear2.age} years old; birthdate "
      f"{bear2.birth_date}; {bear2.color} color; {bear2.gender}; "
      f"{bear2.weight} pounds; from {bear2.originating_zoo}; arrived {bear2.arrival_date}\n")
print(f"Number of bears: {bear2.num_of_bears}")

print()

bear3 = Bear("Lippy", 4, "fall", "black", 355, "Woodland park zoo, Washington")
bear3.unique_id = gen_unique_animal_id("Bear", bear3.num_of_bears)
bear3.name = gen_animal_name("Bear", 3)
bear3.gender = "female"
bear3.birth_date = gen_birth_day(str(3), "fall,")
bear3.arrival_date = date.today()
bear_habitat.append(bear3)  # append third bear object to bear_habitat
# output information about bear object
print(f"Bear name: {bear3.name}")
print(f"Species: {bear3.species}")
print(f"Gender: {bear3.gender}")
print(f"Age: {bear3.age} years old")
print(f"Color: {bear3.color} color")
print(f"Weight: {bear3.weight} pounds")
print(f"Originating Zoo: from {bear3.originating_zoo}")
print(f"Unique ID: {bear3.unique_id}")
print(f"Birthdate: {bear3.birth_date}")
print(f"Arrival date: {bear3.arrival_date}")
print(f"{bear3.unique_id}; {bear3.name}; {bear3.age} years old; birthdate "
      f"{bear3.birth_date}; {bear3.color} color; {bear3.gender}; "
      f"{bear3.weight} pounds; from {bear3.originating_zoo}; arrived {bear3.arrival_date}\n")
print(f"Number of bears: {bear3.num_of_bears}")

print()

bear4 = Bear("Bungle", 4, "spring", "brown", 405, "Alaska Zoo, Alaska")
bear4.unique_id = gen_unique_animal_id("Bear", bear4.num_of_bears)
bear4.name = gen_animal_name("Bear", 4)
bear4.gender = "male"
bear4.birth_date = gen_birth_day(str(3), "spring,")
bear4.arrival_date = date.today()
bear_habitat.append(bear4)  # append fourth bear object to bear_habitat
# output information about bear object
print(f"Bear name: {bear4.name}")
print(f"Species: {bear4.species}")
print(f"Gender: {bear4.gender}")
print(f"Age: {bear4.age} years old")
print(f"Color: {bear4.color} color")
print(f"Weight: {bear4.weight} pounds")
print(f"Originating Zoo: from {bear4.originating_zoo}")
print(f"Unique ID: {bear4.unique_id}")
print(f"Birthdate: {bear4.birth_date}")
print(f"Arrival date: {bear4.arrival_date}")
print(f"{bear4.unique_id}; {bear4.name}; {bear4.age} years old; birthdate "
      f"{bear4.birth_date}; {bear4.color} color; {bear4.gender}; "
      f"{bear4.weight} pounds; from {bear4.originating_zoo}; arrived {bear4.arrival_date}\n")
print(f"Number of bears: {bear4.num_of_bears}")

all_animals = [hyena_habitat, lion_habitat, tiger_habitat, bear_habitat]  # initialize a list to hold all animals

print(gen_zoo_habitat("Hyena"))  # call gen_zoo_habitat function and takes "Hyena" as argument.
# print hyena habitat
print(gen_zoo_habitat("Lion"))  # call gen_zoo_habitat function and takes "Lion" as argument
# prints lion habitat
print(gen_zoo_habitat("Tiger"))  # call gen_zoo_habitat function and takes "Tiger" as argument
# prints tiger habitat.
print(gen_zoo_habitat("Bear"))  # call gen_zoo_habitat function and takes "Bear" as argument
# prints bear habitat

print(f"\nNumber of animals created: {Animal.num_of_animals}")  # print static variable of num_of_animals

try:  # try block
    with open('outputFile.txt', 'w') as output_file:  # open outputFile.txt and write
        # all the animals organized by species.
        for index, species_habitat in enumerate(all_animals):  # for/in loop
            species_name = ["Hyena", "Lion", "Tiger", "Bear"][index]
            output_file.write(f"\n{species_name} Habitat:\n\n")

            for animal in species_habitat:  # for/in loop.
                # iterate through animals in the species habitat.
                output_file.write(f"{animal.unique_id}; {animal.name}; {animal.age} years old; birthdate "
                                  f"{animal.birth_date}; {animal.color} color; {animal.gender}; {animal.weight}"
                                  f" pounds; from {animal.originating_zoo}; arrived {animal.arrival_date}\n")

except Exception as e:  # except block
    print(f"An error occurred: {str(e)}")
