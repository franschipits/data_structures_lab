"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    data = open(filename)
    for line in data:
        speciesnames = line.rstrip().split("|")[1]
        species.add(speciesnames)

   

    return species
#print(all_species("villagers.csv"))

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

   
    data = open(filename)
    for line in data: 
        names = line.split("|")[0]
        species = line.split("|")[1]
        if search_string == species or search_string == "All":
            villagers.append(names)
    return sorted(villagers)

#print(get_villagers_by_species("villagers.csv", "Cat"))

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """
    Fitness = []
    Nature = []
    Education = []
    Music = []
    Fashion = []
    Play = []

    
    data = open(filename)
    for line in data:
        names = line.split("|")[0]
        hobby = line.split("|")[3]

        if hobby == "Fitness":
            Fitness.append(names)

        elif hobby == "Nature":
            Nature.append(names)

        elif hobby == "Education":
            Education.append(names)

        elif hobby == "Music":
            Music.append(names)

        elif hobby == "Fashion":
            Fashion.append(names)

        elif hobby == "Play":
            Play.append(names)


    return [Fashion, Nature, Education, Music, Fashion, Play]

#print(all_names_by_hobby("villagers.csv"))

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

   
    data = open(filename)
    for line in data:
        # names = line.split("|")[0]
        # species = line.split("|")[1]
        # personality = line.split("|")[2]
        # hobby = line.split("|")[3]
        # motto = line.split("|")[4]

        #all_data.append(tuple(names, species, personality, hobby, motto))
        all_data.append(tuple(line.split("|")))

    return all_data
#print(all_data("villagers.csv"))

def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """
    # data = open(filename)
    # for line in data: 
    #     names = line.split("|")[0]
    #     motto = line.split("|")[4]
    #     if villager_name in names:
    #         return motto
    #     elif villager_name not in names:
    #         return None
        
    for name, _, _, _, motto in all_data(filename):
        if name == villager_name:
            return motto
    
# print(find_motto("villagers.csv", "Klaus"))


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """
    likeminded = set()

    target_personality = None
    for villager_data in all_data(filename):
        name, _, personality = villager_data[:3]

        if name == villager_name:
            target_personality = personality
            break

    if target_personality:
        for villager_data in all_data(filename):
            name, _, personality = villager_data[:3]
            if personality == target_personality:
                likeminded.add(name)

    return likeminded

# print(find_likeminded_villagers("villagers.csv", "Klaus"))
  
