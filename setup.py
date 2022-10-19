from setuptools import setup, find_packages

setup(
    name='comp0035_pbl4',
    version='1.1',
    author='Sarah Sanders',
    url='https://github.com/ucl-comp0035/comp0035_pbl4',
    python_requires='>=3.7',
    packages=find_packages(
        include=[
        ]
    ),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
    ],
    package_data={
        'paralympics_raw': ['paralympics_raw.csv'],
    },
)
