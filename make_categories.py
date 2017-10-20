import os
import sys

if len(sys.argv) != 2 and not os.path.exists('./quotes.txt'):
    sys.exit("pass a single argument: the path to the quotations file")
elif os.path.exists('./quotes.txt'):
    filename = './quotes.txt'
else:
    filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit("Can't find {}".format(filename))

## function to figure out all possible tags in the file
def find_unique_tags(filename):
    """Scan the input file and identify all unique categories."""
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
    """Write a quote to a specific category file."""
    filename = os.path.join('./quotes', '{}.txt'.format(category))
    if os.path.isfile(filename):
        file = open(filename, "a+")
    else:
        file = open(filename, "w+")
    file.write("{}\n- {}\n\n".format(quote, author))
    file.close()


## creates list where each list is a different tag
categories = find_unique_tags(filename)

# new to make a new subdirectory to hold all the resulting files
if not os.path.isdir("./quotes"):
    os.mkdir("./quotes")

with open(filename) as file:
    for i, line in enumerate(file):
        if line != "\n":

            try:
                quote, author, *cats = line.split(":::")

                cats = [cat.strip() for cat in cats]

                for cat in cats:
                    write_to_file(quote.strip(), author.strip(), cat)

            except ValueError:
                print("skipping line {}".format(i))
