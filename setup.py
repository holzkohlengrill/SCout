import setuptools
from SCout.SCout import VERSION

with open("readme.md", "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name="SCout | Standard Character Out",
    version=VERSION,
    author="Marcel Schmalzl",
    description="Prints formatted console output tagged as info, warning or error. Usage is similar to `print()`.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/holzkohlengrill/SCout",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
