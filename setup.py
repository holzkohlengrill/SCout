import setuptools

with open("readme.md", "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name="pypiscout",
    version=2.13,
    license="MIT",
    author="Marcel Schmalzl",
    description="Description Special Character Out (aka pypiscout) | Prints uniformly formatted console output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/holzkohlengrill/SCout",
    packages=["pypiscout"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
