"""entry point of 06682 final project"""
import sys
from s23openalexfinal import Works


def main():
    """main"""
    orcid = sys.argv[2]
    operation = sys.argv[1]
    work = Works(orcid)
    if operation == "ris":
        print(work.ris)
    elif operation == "bib":
        print(work.bibtex())
