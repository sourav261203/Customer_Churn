from setuptools import find_packages,setup
from typing import List

Hypen_e_dot="-e ."

def get_requirements(file_path:str)->List[str]:
    # This function will return the list of requiremnets
    requirements=[]
    
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    
    return requirements


    


setup(
    name='Customer-Churn-ML',
    version='0.0.1',
    author='Sourav',
    author_email='skumar.choudhary2612@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')



)