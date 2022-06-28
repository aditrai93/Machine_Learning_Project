from setuptools import setup,find_packages
from typing import List


#Declaring variables for setup function
Name="housing-predictor"
Version="0.0.3"
Author="Aditya"
Description="This is my first ML project"
Package=['housing']
Requirement="requirement.txt"

def get_requirement_list()->List[str]:
    with open(Requirement) as requirement:
        return  requirement.readlines().remove('-e .')

setup(
    name=Name,
    version=Version,
    author=Author,
    description=Description,
    packages=find_packages(),
    install_requires= get_requirement_list()
)