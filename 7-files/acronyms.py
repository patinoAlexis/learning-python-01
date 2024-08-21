## Important notes:
# 1. Like other languages is important to add the try catch statement when opening files. We don't
# want to have a program that crashes when the file is not found or when the file is not accessible
# 2. The reading and writing of files looks very straight forward, not many comments about it.

# save all changes
#1
def main():
    # Ask the user what they want to do
    action = input("Do you want to add or search for an acronym? \n f) Find \n a) Add ").lower()
    if action == 'f':
        # If the user wants to search for an acronym
        finded = find_acronym()
        if finded:
            print("The acronym is already in the list")
        elif finded is not None:
            print("The acronym is not in the list")

    elif action == 'a':
        # If the user wants to add an acronym
        add_acronym()
        print("The acronym has been added")


## Function to make sure the acronym is not already inserted\
def find_acronym():
    # Ask for the acronym to search
    acronym = input("What is the acronym you are looking for? ").upper()

    # return if finded is true or false
    try:
        with open('acronyms.txt', 'r') as file:
            for line in file:
                if acronym in line:
                    return True
    except FileNotFoundError:
        print("The file does not exist")
        return None
    return False

## Adding new acronym
def add_acronym():
    # Ask for the acronym to add
    acronym = input("What is the acronym you want to add? ").upper()
    # We then ask for the definition of the acronym
    definition = input("What is the definition of the acronym? ")
    # Open the file we use as a db and save changes
    with open('acronyms.txt', 'a') as file:
        file.write(f"{acronym} : {definition}\n")


main()