from setuptools import find_packages, setup

setup(
    name='hroml',
    packages=find_packages(include=['hroml']),
    version='0.1.10',
    description='Python library for Hood College, CS543 Machine learning class',
    author='John Caruthers',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.1.0'],
    test_suite='tests'
)
