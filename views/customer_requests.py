CUSTOMERS = [
    {
        "id": 1,
        "email": "ryan@me.com",
        "name": "Ryan Tanay"
    },
    {
        "id": 2,
        "email": "leslieK@park.gov",
        "name": "Leslie Knope"
    },
    {
        "id": 3,
        "email": "annP@park.gov",
        "name": "Ann Perkins"
    },
    {
        "id": 4,
        "email": "donnaM@park.gov",
        "name": "Donna Meagle"
    }
]


def get_all_customers():
    """Returns list of dictionaries in CUSTOMERS variable"""
    return CUSTOMERS

# Function with a single parameter.
# id of location needs to be passed as an argument.


def get_single_customer(id):
    """Looks up single animal"""
    # Variable to hold the found location, if it exists
    requested_customer = None

    # Iterate the LOCATION list above. Very similar to the
    # for..of loops you used in JavaScript.
    # It iterates the entire list with a for..in loop.
    # For each location, it checks if its id property
    # is the same as the id that was passed into the function as a parameter.
    for customer in CUSTOMERS:
        # Finally, it returns the value of requested_location.
        # It will either be None, or the dictionary that it found.
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer


def create_customer(customer):
    """Args: customer (json string), returns new dictionary with id property added"""
    # Get the id value of the last location in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer


def delete_customer(id):
    """DELETE animal"""
    # Initial -1 value for animal index, in case one isn't found
    customer_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the animal. Store the current index.
            customer_index = index

    # If the animal was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)


def update_customer(id, new_customer):
    """UPDATE customer"""
    # function iterates list of animals until it finds right one
    # then, replaces it with what the client sent as the replacement"""
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the animal. Update the value.
            CUSTOMERS[index] = new_customer
            break
