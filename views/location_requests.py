LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike",
        "status": "open"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive",
        "status": "open"
    }
]


def get_all_locations():
    # This Python module has one method defined in it.
    # Want to make that method available to any other Python code.
    # To do that, you import it into the __init__.py module.
    """Method -- gets all objects in the array"""
    return LOCATIONS

# Function with a single parameter.
# id of location needs to be passed as an argument.


def get_single_location(id):
    """Looks up single animal"""
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the LOCATION list above. Very similar to the
    # for..of loops you used in JavaScript.
    # It iterates the entire list with a for..in loop.
    # For each location, it checks if its id property
    # is the same as the id that was passed into the function as a parameter.
    for location in LOCATIONS:
        # Finally, it returns the value of requested_location.
        # It will either be None, or the dictionary that it found.
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location


def create_location(location):
    """function--take new dictionary representation sent by the client
        and append it to the LOCATIONS list"""
    # Get the id value of the last location in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    location["id"] = new_id

    # Add the animal dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location


def delete_location(id):
    """DELETE location"""
    # Initial -1 value for animal index, in case one isn't found
    location_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    # enumerate allows you to loop thru element and index at same time
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the animal. Store the current index.
            location_index = index

    # If the animal was found, use pop(int) to remove it from list
    if location_index >= 0:
        LOCATIONS.pop(location_index)


def update_location(id, new_location):
    """UPDATE location"""
    # function iterates list of animals until it finds right one
    # then, replaces it with what the client sent as the replacement"""
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the animal. Update the value.
            LOCATIONS[index] = new_location
            break
