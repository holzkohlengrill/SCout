import setuptools

with open("readme.md", "r") as fp:
    long_description = fp.read()

setuptools.setup(
    name="pypiscout",
    version=1.3,
    license="MIT",
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
