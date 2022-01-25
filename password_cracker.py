import hashlib


def dictionary_attack(password_hash):

    dictionary = open(
        '/Users/danielnikkari/Desktop/Aalto/Security Engineering/Ex2/Python/Security_Engineering/wordlists/wordlist2.txt', 'r', encoding='utf-8')
    password_found = False

    for dict_item in dictionary:
        hashed_value = (hashlib.sha1(bytes(dict_item, 'utf-8'))).hexdigest()
        # print(hashed_value)
        if hashed_value == password_hash:
            password_found = True
            recovered_password = dict_item
    if password_found:
        print("Found match for hash value\n", password_hash)
        print("Password recovered: \n", recovered_password)
    else:
        print("Password not found.")


def main():
    #password_hash = input('Enter hashed value: ')
    password_list = open(
        '/Users/danielnikkari/Desktop/Aalto/Security Engineering/Ex2/Python/Security_Engineering/hashed_passowrds/dictionary8.txt', 'r', encoding='utf-8')
    for password in password_list:
        dictionary_attack(password)


if __name__ == "__main__":
    main()
