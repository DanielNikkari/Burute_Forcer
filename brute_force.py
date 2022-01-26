import hashlib
import string
from random import *
from itertools import chain, product
from sys import stdout
import os
import json

# Ask for password hash
# password_hash = input("Enter the password hash: ")

# Get root directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

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
                                                 for i in range(minlength - 1, maxlength + 1)))


# import wordlists
def wordlists(directory):
    wordlists_container = []
    for wordlist in os.listdir(directory):
        # print(wordlist)
        if wordlist.endswith('txt'):
            with open(directory + wordlist, "r") as wordlist_file:
                for line in wordlist_file:
                    line = line.strip()
                    # print(line)
                    wordlists_container.append(line)
                    # print(len(wordlists_container))
    print("Length of the loaded wordlist: {}".format(len(wordlists_container)))
    return wordlists_container


def main():
    # ret = list(bruteforce('abcde', 2))
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

    # Wordlist in use flag
    wordlist_flag = False

    print("\nWelcome to hashed password brute forcer!\n")
    print("Your root directory: {}\n".format(ROOT_DIR))

    # Ask if the user wants use wordlists
    while(1):
        wordlist_input = input("Do you want to use wordlists? (y/n): ")
        if wordlist_input == 'y':
            wordlists_path = input(
                "Provide full path to the wordlists directory: ")
            try:
                wordlists_container = wordlists(wordlists_path)
                wordlist_flag = True
                # print(f"Wordlist flag: {wordlist_flag}")
                break
            except Exception as exc:
                print(
                    f"Something went wrong opening or reading the file: {exc}")
        elif wordlist_input == 'n':
            break
        else:
            print("Command '{}' not understood. Check the spelling...".format(
                wordlist_input))

    # Request to choose the char set
    while(1):
        chosen_charset = input(
            "Write 'letters' if you want only ASCII letters and 'all' for all ASCII characters: ")
        if chosen_charset == "all":
            ascii_charset = ascii_charset_all
            break
        elif chosen_charset == "letters":
            ascii_charset = ascii_charset_letters
            break
        else:
            print("Command '{}' not understood. Check the spelling...".format(
                chosen_charset))

    # Request file path from the user or to type a password hash
    while(1):
        user_input = input(
            "\nGive a filepath by typing 'filepath' or give a hashed password by typing 'password': ")
        if user_input == "filepath":
            user_filepath = input("Provide a full filepath: ")
            try:
                user_hashed_file = open(user_filepath, 'r')
                for line in user_hashed_file:
                    line = line.strip()
                    user_input_container.append(line)
                print("File opened and read succesfully!\n")
                user_hashed_file.close()
                break
            except Exception as exc:
                print(
                    f"Something went wrong opening or reading the file: {exc}")

        elif user_input == "password":
            user_hashed_password = input("Provide a hashed password: ")
            user_input_container.append(user_hashed_password)
            print("Password read!")
            break

        else:
            print("Command '{}' not understood. Check the spelling...".format(
                user_input))

    # Print out the uder input
    print("INPUT:\n{}\n".format(user_input_container))

    # Ask for the min and max length of the password
    print("Provide password min and max length:")
    while(1):
        minlength = input("Give password minimum length (int): ")
        if minlength.isnumeric():
            minlength = int(minlength)
        if isinstance(minlength, int):
            print("Password min length: {}".format(minlength))
            break

    while(1):
        maxlength = input("Give password maximum length (int): ")
        if maxlength.isnumeric():
            maxlength = int(maxlength)
        if isinstance(maxlength, int):
            print("Password max length: {}".format(maxlength))
            break
    
    output_file_name = input("Provide the name of the outputfile (add .txt to the end): ")

    print("\n!-------------------------------------------------!\n")
    print("Beginning to brute force...\n")

    # For debugging
    '''
    test_hash = hashlib.sha1(bytes('abcde', 'ascii')).hexdigest()
    test_hash2 = hashlib.sha1(bytes('abd1', 'ascii')).hexdigest()
    test_hash3 = hashlib.sha1(bytes('cbaf', 'ascii')).hexdigest()
    test_hash4 = hashlib.sha1(bytes('12ac4', 'ascii')).hexdigest()
    test_hash5 = hashlib.sha1(bytes('123', 'ascii')).hexdigest()
    # print("Test hash: \n{}\n\n".format(test_hash))
    print("\nTest hashes:\n\n")
    print(test_hash)
    print(test_hash2)
    print(test_hash3)
    print(test_hash4)
    print(test_hash5)
    '''

    if wordlist_flag:
        print("Checking provided wordlists against the hashes first...\n")
        for wordlist_line in wordlists_container:
            wordlist_line_hash = hashlib.sha1(
                bytes(wordlist_line, 'ascii')).hexdigest()
            # print(
            # f"wordlist line: {wordlist_line}, wordlist hash: {wordlist_line_hash}")
            for password_hash in user_input_container:
                if wordlist_line_hash == password_hash:
                    print(
                        "\n\n!------------------------------------------------------------------!\n")
                    print(
                        "\n\tPassword: {}, found using a wordlist.\n(hash: {})\n\n".format(wordlist_line, password_hash))
                    print(
                        "!------------------------------------------------------------------!\n")
                    brute_forced_password = wordlist_line
                    brute_forced_password_hash = wordlist_line_hash
                    found_password_dict[password_hash] = brute_forced_password
                    # break
                else:
                    n = n + 1
                    continue
                if len(found_password_dict) == len(user_input_container):
                    break
                else:
                    continue
    print("\nContinuing to brute forcing...\n")

    # Looping attempts and testing if it matches the given hash
    for attempt in bruteforce(ascii_charset, minlength, maxlength):
        stdout.write("\r%d attempts" % n)
        stdout.flush()
        # Transform the attempt into a hash
        attempt_hash = hashlib.sha1(bytes(attempt, 'ascii')).hexdigest()
        # print(attempt)
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
    print(f"\nWriting the passwords to a file named: {output_file_name}")
    with open(ROOT_DIR + '/output/' + output_file_name, 'w+') as ofile:
        ofile.write(json.dumps(found_password_dict))
    
    print("\n[!] CLOSING THE PROGRAM...\n\n")

if __name__ == "__main__":
    main()
