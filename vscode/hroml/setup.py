from setuptools import find_packages, setup

setup(
    name='hroml',
    packages=find_packages(include=['hroml']),
    version='0.3.2',
    description='Python library for Hood College, CS543 Machine learning class',
    author='John Caruthers',
    install_requires=['numpy', 'pandas'],
)
