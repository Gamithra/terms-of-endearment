#!/usr/bin/python3
import sys, getopt, random

categories = ["affectionate", "attractive", "badass", "basic", "cute", "funny", "romantic"]

def main(argv):
    opts, args = getopt.getopt(argv,"h", ["category=", "sentence="])

    category = ""
    sentence = ""

    for opt, arg in opts:
        if opt == "-h":
            print("usage: ./endearment [category=<category>] [sentence=<sentence>]\n")
            print("available types:")
            print(", ".join(categories))
            sys.exit()
        if opt in ("--category"):
            category = arg
        if opt in ("--sentence"):
            sentence = arg

    if category == "":
        category = "all"

    l = open(category).read().splitlines()
    if sentence != "":
        print("\033[1;37;45m" + sentence + " " + random.choice(l).lower() + "\033[0;37;30m")
    else:
        print("\033[1;37;45m" + random.choice(l).lower() + "\033[0;37;30m")




if __name__ == "__main__":
    main(sys.argv[1:])
