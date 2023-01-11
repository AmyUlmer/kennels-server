ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "locationId": 1,
        "customerId": 4,
        "status": "Admitted"
    },
    {
        "id": 2,
        "name": "Roman",
        "species": "Dog",
        "locationId": 1,
        "customerId": 2,
        "status": "Admitted"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "locationId": 2,
        "customerId": 1,
        "status": "Admitted"
    }
]


def get_all_animals():
    # This Python module has one method defined in it.
    # Want to make that method available to any other Python code.
    # To do that, you import it into the __init__.py module.
    """Method -- gets all objects in the array"""
    return ANIMALS

# Function with a single parameter.
# id of animal needs to be passed as an argument.


def get_single_animal(id):
    """Looks up single animal"""
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    # It iterates the entire list with a for..in loop.
    # For each animal, it checks if its id property
    # is the same as the id that was passed into the function as a parameter.
    for animal in ANIMALS:
        # Finally, it returns the value of requested_animal.
        # It will either be None, or the dictionary that it found.
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal


def create_animal(animal):
    """function--take new dictionary representation sent by the client
        and append it to the ANIMALS list"""
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal


def delete_animal(id):
    """DELETE animal"""
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    # pop() list method removes an object from a list and returns it to us
    # provide the argument, which is the index position
    if animal_index >= 0:
        ANIMALS.pop(animal_index)


def update_animal(id, new_animal):
    """UPDATE animal"""
    #function iterates list of animals until it finds right one
    #then, replaces it with what the client sent as the replacement"""
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Update the value.
            ANIMALS[index] = new_animal
            break
