from setuptools import find_packages, setup 
from typing import List


def get_requirements(file_name: str) -> List[str]:
    '''
    This function will collect all the data from the file and return a list of requirements
    '''

    requirements = []
    with open(file_name, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    
    return requirements


setup(
    name='MLproject',
    version='0.0.1',
    author='Arslan',
    author_email='iarslankhalid@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)