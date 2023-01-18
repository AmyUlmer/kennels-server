# expanded animal response -- client wants the location and customer name for an animal.
# go to the get_single_animal function. You need to augment this function
# to make the requested_animal dictionary more robust.
# import single location and single customer from correct locations.
# dot at the beginning is important because the other modules are in the same directory
# how you tell Python where to look for the module.
# sqlite3 package is built into Python and will allow you to query your database
# json package is also built into Python and allows you to serialize Python data structures to JSON format, and vice versa.
# import the Animal class so that you can create instances of it for each row of data that gets returned from the database.
import sqlite3
import json
from models import Animal 
from .location_requests import get_single_location
from .customer_requests import get_single_customer

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
    """Returns list of dictionaries stored in ANIMALS variable"""
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.breed,
            a.status,
            a.location_id,
            a.customer_id
        FROM animal a
        """)

        # Initialize an empty list to hold all animal representations
        animals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            animal = Animal(row['id'], row['name'], row['breed'],
                            row['status'], row['location_id'],
                            row['customer_id'])

            animals.append(animal.__dict__)

    return animals

# Function with a single parameter.
# id of animal needs to be passed as an argument.
def get_single_animal(id):
    """Finds the matching animal dictionary for the specified animal id
    Args:
        id (int): animal id
    Returns:
        object: animal dictionary
    """

    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    # It iterates the entire list with a for..in loop.
    # For each animal, it checks if id property
    # is the same as the id that was passed into the function as a parameter.
    for animal in ANIMALS:
        # Finally, it returns the value of requested_animal.
        # It will either be None, or the dictionary that it found.
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    # invoke the imported methods to get the related resources
    # for the animal and attach them to the dictionary you found

            # Add the animal's location
            matching_location = get_single_location(
                requested_animal["locationId"])
            requested_animal["location"] = matching_location

            # Add the animal's owner
            matching_customer = get_single_customer(
                requested_animal["customerId"])
            requested_animal["customer"] = matching_customer

            # related location and customer dictionaries are embedded directly on the animal.
            # delete customerId and locationId keys
            requested_animal.pop("locationId")
            requested_animal.pop("customerId")

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
    # function iterates list of animals until it finds right one
    # then, replaces it with what the client sent as the replacement"""
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Update the value.
            ANIMALS[index] = new_animal
            break
