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

    # [ (name, species, personality, hobby, motto ),
    #   (name, species, personality, hobby, motto )
    # ]
        
    for data_line in all_data(filename):
        # data_line = (name, species, personality, hobby, motto)
        if data_line[0] == villager_name:
            return data_line[4]
    
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
# take a villager's name and find their personality
# go through all the lines, and for each villager whose personality matches, add them to the set
    villagers_with_personality = set() # set of all villagers with personality

    all_villagers = all_data(filename)
    
    for name, _, personality, _, _ in all_villagers:
        if name == villager_name:
            target_personality = personality # string, personality we're searching for
        
    for name, _, personality, _, _ in all_villagers:
        if personality == target_personality:
            villagers_with_personality.add(name)
    
    return villagers_with_personality
print(find_likeminded_villagers("villagers.csv", "Klaus"))
  
