from setuptools import setup, find_packages

setup(
    name='pynim',
    version='0.0.1',
    description='Demo for nim and python',
    author='Christopher J. Stehno',
    author_email='chris.stehno@gmail.com',
    license='unlicensed',
    packages=find_packages(exclude=['tests*']),
    entry_points="""
        [console_scripts]
        pynim = pynim.main:main
    """,
    install_requires=[
        'click',
        'rich',
    ],
)
