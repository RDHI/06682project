import sys
from s23openalexfinal import Works


def main():
    orcid = sys.argv[2]
    operation = sys.argv[1]
    work = Works(sys.argv[2])
    if operation == "ris":
        print(work.ris)
    elif operation == "bib":
        print("nontnot")
