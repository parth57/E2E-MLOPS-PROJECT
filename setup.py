from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of packages/libraries like pandas
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [line.replace('\n','') for line in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements
        
file_path = 'requirements.txt'

setup(
    name = 'First_E2E',
    version = '0.0.1',
    author = 'Parth',
    author_email = 'parthagarwal57@gmail.com',
    packages = find_packages(),                   # searches every folder with package, for eg - src
    install_requires = get_requirements(file_path)
    )