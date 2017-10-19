import os
import sys

filename = "test.txt"


# need more testing to test whether the lines and arguments to the
# functions are correct / as expected

## function to figure out all possible tags in the file
def find_unique_tags(filename):
    # list to store cateogories
    categories = []
    with open(filename) as file:
        for line in file:
            all_matches = line.split(":::")
            tags = all_matches[2:]
            tags = [tag.strip() for tag in tags]

            for tag in tags:
                if tag not in categories:
                    categories.append(tag)
    print("\nfound the following categories:\n")
    for cat in categories:
        print("  - {}".format(cat))
    return(categories)

def write_to_file(quote, author, category):
    filename = '{}.txt'.format(category)
    if os.path.isfile(filename):
        file = open(filename, "a+")
    else:
        file = open(filename, "w+")
    file.write("{}\n- {}\n\n".format(quote, author))
    file.close()


## creates list where each list is a different tag

categories = find_unique_tags(filename)

# new to make a new subdirectory to hold all the resulting files


with open(filename) as file:
    for i, line in enumerate(file):
        if line != "\n":
            all_matches = line.split(":::")

            number_matches = len(all_matches)

            if number_matches < 3:
                print("skipping line {}".format(i))

            cats = all_matches[2:]
            cats = [cat.strip() for cat in cats]

            for cat in cats:
                write_to_file(all_matches[0].strip(), all_matches[1].strip(), cat)
