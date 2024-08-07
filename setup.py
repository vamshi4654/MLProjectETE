from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='vamshi',
author_email='g.vamshi123@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)


# -------------------------------------------------------------
#written by me
# from setuptools import find_packages,setup
# from typing import List

# HYPEN = "-e ."

# def get_requirements(file_path:str)-> List[str]:
#     content = []
#     with open(file_path) as file:
#         content = file.readlines()
#         content = [content.replace("\n"," ") for content in content]

#         if HYPEN in content:
#             content.remove(HYPEN)
#     return content

# #this function will return the list of requirements
    


# setup(
# name = 'mlproject',
# packages = find_packages(),
# requires = get_requirements('requirements.txt')
# # the install requires is an list we need to give the what are the 
# # packages need to install like pandas ,numpy
# # but when we want to install new package it will be difficult to add 
# # so we can write all the packages in requirements.txt and can call fro here.

# )