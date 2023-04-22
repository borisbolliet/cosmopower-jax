from setuptools import setup, find_packages
import shutil

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

PACKAGENAME = 'cosmopower-jax'

setup(
    name='cosmopower-jax',
    version="0.1.0",
    author='Davide Piras',
    author_email='davide.piras@unige.ch',
    description='Differentiable cosmological emulators',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dpiras/cosmopower-jax',
    license='GNU General Public License v3.0 (GPLv3)',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=['pickle',
                      'jax',
                      'matplotlib>=3.1.2',
                      'numpy>=1.17.4',
                      ]
                      )
