import hashlib
import string
from random import *
from itertools import chain, product
from sys import stdout

# Ask for password hash
password_hash = input("Enter the password hash: ")

# Get all ASCII characters
ascii_charset = string.printable

# Initiate character container
possible_characters = []

# Append all possible characters into the container
for char in ascii_charset:
    possible_characters.append(char)
# print(possible_characters)

# Initiate an empty guess
guess = ""

# Loop to generate guesses util one is the right guess


def bruteforce(charset, maxlength):
    n = 9
    return (''.join(candidate)
            for candidate in chain.from_iterable(product(charset, repeat=i)
                                                 for i in range(n, maxlength + 1)))


def main():
    #ret = list(bruteforce('abcde', 2))
    # print(ret)
    # print(string.ascii_lowercase)
    # print(string.ascii_uppercase)

    # Max length for the brute force
    maxlength = 10

    # Number of iterations
    n = 0

    # Store the found password here
    brute_forced_password = ""
    brute_forced_password_hash = ""

    print("\n!-------------------------------------------------!\n")
    print("Starting the loop\n")

    test_hash = hashlib.sha1(bytes('000001mu', 'ascii')).hexdigest()
    print("Test hash: \n{}\n\n".format(test_hash))

    # Looping attempts and testing if it matches the given hash
    for attempt in bruteforce(ascii_charset, maxlength):
        #stdout.write("\rAttempts: {}, Attempt: {}".format(n, attempt))
        # stdout.flush()

        # Transform the attempt into a hash
        attempt_hash = hashlib.sha1(bytes(attempt, 'ascii')).hexdigest()
        if attempt_hash == test_hash:
            print("Password {} found after {} tries".format(attempt, n))
            brute_forced_password = attempt
            brute_forced_password_hash = attempt_hash
            break
        else:
            n = n + 1
            continue
    # stdout.write("\n")

    print("Found hash: {}\nThe given hash: {}".format(
        attempt_hash, password_hash))


if __name__ == "__main__":
    main()
