from setuptools import setup,find_packages
from typing import List



# Declaring Variable For SetUp Function
PROJECT_NAME = "housing-pridictors"
VERSION = "0.0.3"
AUTHOR = "Dattatri Kore"
DESCRIPTION = "this is a first FSDS batch Machine Learning Project"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Decription: this function is going to return list of requirement 
    mention in requirements.txt

    ruturn this function is going to return a list which contain
    name of labraries mentioned in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author= AUTHOR,
    description=DESCRIPTION,
    packages= find_packages(),
    install_requires = get_requirements_list()

)
 