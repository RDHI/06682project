"""setup function for 06682 final project"""
from setuptools import setup

setup(
    name="s23openalexfinal",
    version="0.0.1",
    description="final project for 06682",
    maintainer="Ruili Ding",
    maintainer_email="ruilid@andrew.cmu.edu",
    license="MIT",
    packages=["s23openalexfinal"],
    entry_points={"console_scripts": ["oa = s23openalexfinal.main:main"]},
    long_description="""A long
      multiline description.""",
)
