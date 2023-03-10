EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis",
        "status": "not working"
    }
]


def get_all_employees():
    # This Python module has one method defined in it.
    # Want to make that method available to any other Python code.
    # To do that, you import it into the __init__.py module.
    """Method -- gets all objects in the array"""
    return EMPLOYEES

# Function with a single parameter.
# id of location needs to be passed as an argument.


def get_single_employee(id):
    """Looks up single employee"""
    # Variable to hold the found location, if it exists
    requested_employee = None

    # Iterate the LOCATION list above. Very similar to the
    # for..of loops you used in JavaScript.
    # It iterates the entire list with a for..in loop.
    # For each location, it checks if its id property
    # is the same as the id that was passed into the function as a parameter.
    for employee in EMPLOYEES:
        # Finally, it returns the value of requested_location.
        # It will either be None, or the dictionary that it found.
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    """function--take new dictionary representation sent by the client
        and append it to the LOCATIONS list"""
    # Get the id value of the last location in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    employee["id"] = new_id

    # Add the animal dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee


def delete_employee(id):
    """DELETE employee"""
    # Initial -1 value for animal index, in case one isn't found
    employee_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the animal. Store the current index.
            employee_index = index

    # If the animal was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)


def update_employee(id, new_employee):
    """UPDATE employee"""
    # function iterates list of animals until it finds right one
    # then, replaces it with what the client sent as the replacement"""
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the animal. Update the value.
            EMPLOYEES[index] = new_employee
            break
