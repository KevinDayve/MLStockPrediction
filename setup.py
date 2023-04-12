from setuptools import find_packages, setup
from typing import List

Hyphen = "-e ."

def get_requirements(file_path:str) -> List[str]:
    """
    This function will return a list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [requirement.replace("\n", "") for requirement in requirements]

        if Hyphen in requirements:
            requirements.remove(Hyphen)

    return requirements


setup(
    name = "ML Portfolio",
    version = "0.0.1",
    author = "Kevin Dave",
    author_email = "kevindave5735@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)
