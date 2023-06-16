from setuptools import find_packages,setup
from typing import List

x = '-e .'
def get_requirement(file_path:str)->List[str]:
    #give the list of requirements
    requirements =[]
    with open(file_path) as file_object:
        requirements= file_object.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if x in requirements:
            requirements.remove(x)
    return requirements
    
setup(
    name = 'ml_project',
    version = '0.0.1',
    auther = 'shivam',
    author_email ='borseshivam01@gmail.com',
    packages = find_packages(),
    install_requires  = get_requirement('requirements.txt')
)