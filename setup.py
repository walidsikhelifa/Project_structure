from setuptools import setup, find_packages
from typing import List
requirements_lst: List[str] = []
def get_requirements(file_path: str) -> List[str]:
    """ this function will return the list of requirements """
    try:
        with open('requirements.txt' , 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement!= '-e .':
                    requirements_lst.append(requirement)

    except FileNotFoundError:
        print('requirements.txt file not found. Please make sure it exists in the project directory.')
    return requirements_lst


setup(
    name='End to end network ML',
    version='0.0.1',
    author='Walid',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
) 