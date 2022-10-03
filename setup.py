from setuptools import find_packages, setup
setup(
    name='gear',
    packages=find_packages(),
    version='0.1.0',
    description='My first Python library',
    author='JirayuL',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.1.3'],
    test_suite='tests',
)
