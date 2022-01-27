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
                                                 for i in range(minlength, maxlength + 1)))


def main():
    # ret = list(bruteforce('abcde', 2))
    # print(ret)
    # print(string.ascii_lowercase)
    # print(string.ascii_uppercase)

    # Max length for the brute force
    maxlength = 16

    # Min length for the brute force
    minlength = 8

    # Number of iterations
    n = 0

    # Store the found password
    brute_forced_password = ""
    brute_forced_password_hash = ""

    # Container for the hashed passwords (dictionary8.txt)
    input_container = ['0bbdd1090c9c6b3edf6b4473ed560d7572e41af2', 'f514a141ce1724ace7b409dddbb9665fba03bd1d', 'a2f0823b34332f5166639cb0f95410b74086dcc0', 'a0fd9ef9d02998103fa094521a1c97af09afa9d9', 'bb1df91b4926618580f7bb4775ee09aea9301219']

    # Output filename
    output_file_name = "found_passwords.txt"

    # Dict for found passwords
    found_password_dict = {}


    print("\n\n********************************************************************************************************")
    print("\n\tWelcome to SHA-1 hashed password brute forcer!\n")
    print("\tMade by Daniel Nikkari\n")
    print("\tYour root directory: {}\n".format(ROOT_DIR))
    print("********************************************************************************************************\n")

    print("[!] Stop the loop at any time by pressing 'Ctrl-C'.\n")
    # Looping attempts and testing if it matches the given hash
    try:
        for attempt in bruteforce(ascii_charset_letters, minlength, maxlength):
            #stdout.write("\r%d " % n)
            stdout.write("\r{} {}".format(n, attempt))
            stdout.flush()
            # Transform the attempt into a hash
            attempt_hash = hashlib.sha1(bytes(attempt, 'ascii')).hexdigest()
            # print(attempt)
            for password_hash in input_container:
                # Compare the hashed guesses against the hashed passwords
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
            # Break the loop if all the given passwords are cracked
            if len(found_password_dict) == len(input_container):
                break
            else:
                continue
    except KeyboardInterrupt:
        pass

    stdout.write("\n")

    # Print out the found passowrds
    print("\nDictionary of found passwords:")
    print(found_password_dict)

    # Write the found passwords into a file
    print(f"\nWriting the passwords to a file named: {output_file_name}")
    with open(ROOT_DIR + '/' + output_file_name, 'w+') as ofile:
        ofile.write(json.dumps(found_password_dict))
    
    # Close the program
    print("\n[!] CLOSING THE PROGRAM...\n\n")

if __name__ == "__main__":
    main()