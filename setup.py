from setuptools import setup
from setuptools import find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(name='colorways',
    version='0.9.2',
    description='A Python library for procedural generation of color palettes, color manipulation, and color analysis.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jeremymadea/colorways',
    author='Jeremy Madea',
    author_email='jdmadea@gmail.com',
    license='MIT',
    packages=find_packages(),
    zip_safe=False)
