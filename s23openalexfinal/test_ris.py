"""test script for 06682 final project"""
from s23openalexfinal import Works


REFRIS = """TY  - JOUR
AU  - John R. Kitchin
PY  - 2015
TI  - Examples of Effective Data Sharing in Scientific Publishing
JO  - ACS Catalysis
VL  - 5
IS  - 6
SP  - 3894
EP  - 3899
DO  - https://doi.org/10.1021/acscatal.5b00538
ER  -"""


def test_ris():
    """test_ris() function for 06682 final project"""
    work = Works("https://doi.org/10.1021/acscatal.5b00538")

    assert REFRIS == work.ris
