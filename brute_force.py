import hashlib
import string
from random import *
from itertools import chain, product
from sys import stdout

# Ask for password hash
# password_hash = input("Enter the password hash: ")

# Get all ASCII characters
ascii_charset_all = string.printable

# Get only letters of ASCII
ascii_charset_letters = string.ascii_letters

# Initiate character container
possible_characters = []

# Append all possible characters into the container
for char in ascii_charset_all:
    possible_characters.append(char)
# print(possible_characters)

# Initiate an empty guess
guess = ""

# Loop to generate guesses util one is the right guess


def bruteforce(charset, minlength, maxlength):
    return (''.join(candidate)
            for candidate in chain.from_iterable(product(charset, repeat=i)
                                                 for i in range(minlength, maxlength + 1)))


def main():
    #ret = list(bruteforce('abcde', 2))
    # print(ret)
    # print(string.ascii_lowercase)
    # print(string.ascii_uppercase)

    # Max length for the brute force
    maxlength = 3

    # Min length for the brute force
    minlength = 1

    # Number of iterations
    n = 0

    # Store the found password
    brute_forced_password = ""
    brute_forced_password_hash = ""

    # Container for the hashed passwords provided by the user
    user_input_container = []

    # Dict for found passwords
    found_password_dict = {}

    print("Welcome to hashed password brute forcer!\n")

    # Request to choose the char set
    chosen_charset = input(
        "Write 'letters' if you want only ASCII letters and 'all' for all ASCII characters: ")
    if chosen_charset == "all":
        ascii_charset = ascii_charset_all
    elif chosen_charset == "letters":
        ascii_charset = ascii_charset_letters
    else:
        print("Command not understood, defaulting to all ASCII characters")
        ascii_charset = ascii_charset_all

    # Request file path from the user or to type a password hash
    user_input = input(
        "Give a filepath by typing 'filepath' or give a hashed password by just pressing enter: ")
    if user_input == "filepath":
        user_filepath = input("\nProvide a full filepath: ")
        try:
            user_hashed_file = open(user_filepath, 'r')
            for line in user_hashed_file:
                line = line.strip()
                user_input_container.append(line)
            print("\nFile opened and read succesfully!\n")
        except Exception as exc:
            print(f"Something went wrong opening or reading the file: {exc}")

    else:
        user_hashed_password = input("\nProvide a hashed password: ")
        user_input_container.append(user_hashed_password)
        print("\nPassword read!")

    # Print out the uder input
    print("\nINPUT:\n{}\n".format(user_input_container))

    # Ask for the min and max length of the password
    print("\nProvide password max and min length:\n")
    while(1):
        minlength = input("Give password minimum length (int): ")
        minlength = int(minlength)
        print("Password min length: {}".format(minlength))
        if isinstance(minlength, int):
            maxlength = input("Give password maximum length (int): ")
            maxlength = int(maxlength)
            print("Password max length: {}".format(maxlength))
            if isinstance(maxlength, int):
                break

    print("\n!-------------------------------------------------!\n")
    print("Beginning to brute force...\n")

    '''
    test_hash = hashlib.sha1(bytes('abc', 'ascii')).hexdigest()
    test_hash2 = hashlib.sha1(bytes('abd1', 'ascii')).hexdigest()
    test_hash3 = hashlib.sha1(bytes('cbaf', 'ascii')).hexdigest()
    test_hash4 = hashlib.sha1(bytes('12a', 'ascii')).hexdigest()
    test_hash5 = hashlib.sha1(bytes('123', 'ascii')).hexdigest()
    #print("Test hash: \n{}\n\n".format(test_hash))
    print("\nTest hashes:\n\n")
    print(test_hash)
    print(test_hash2)
    print(test_hash3)
    print(test_hash4)
    print(test_hash5)
    '''

    # Looping attempts and testing if it matches the given hash
    for attempt in bruteforce(ascii_charset, minlength, maxlength):
        stdout.write("\r%d attempts" % n)
        stdout.flush()

        # Transform the attempt into a hash
        attempt_hash = hashlib.sha1(bytes(attempt, 'ascii')).hexdigest()
        for password_hash in user_input_container:
            if attempt_hash == password_hash:
                print(
                    "\n\n!------------------------------------------------------------------!\n")
                print(
                    "\n\tPassword: {}, found after {} attempts.\n\n".format(attempt, n))
                print(
                    "!------------------------------------------------------------------!\n")
                brute_forced_password = attempt
                brute_forced_password_hash = attempt_hash
                found_password_dict[password_hash] = brute_forced_password
                # break
            else:
                n = n + 1
                continue
        if len(found_password_dict) == len(user_input_container):
            break
        else:
            continue

    stdout.write("\n")

    # print("Found hash: {}\nThe given hash: {}".format(
    #    attempt_hash, test_hash))
    print("Dictionary of found passwords:")
    print(found_password_dict)


if __name__ == "__main__":
    main()
