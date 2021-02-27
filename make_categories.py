import os
import sys
from typing import List

if len(sys.argv) != 2 and not os.path.exists("./quotes.txt"):
    sys.exit("pass a single argument: the path to the quotations file")
elif os.path.exists("./quotes.txt"):
    filename = "./quotes.txt"
else:
    filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit("Can't find {}".format(filename))


def find_unique_tags(filename: str) -> List[str]:
    """Scan the input file and identify all unique categories."""

    categories = set()
    with open(filename) as file:
        for line in file:
            all_matches = line.split(":::")
            tags = all_matches[2:]
            tags = [tag.strip() for tag in tags]

            for tag in tags:
                categories.add(tag)

    print("\nfound the following categories:\n")
    for cat in categories:
        print("  - {}".format(cat))

    return list(categories)


def write_to_file(quote, author, category):
    """Write a quote to a specific category file."""

    filename = os.path.join("./quotes", "{}.txt".format(category))

    if os.path.isfile(filename):
        file = open(filename, "a+")
    else:
        file = open(filename, "w+")

    file.write("{}\n- {}\n\n".format(quote, author))
    file.close()


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
