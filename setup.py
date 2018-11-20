import setuptools

with open("README.md", "r") as rm:
    long_description = rm.read()

setuptools.setup(
    name="pycsvify",
    version="0.0.3",
    author="Wessel Meijer",
    description="A Python library that allows easy CSV to Dict conversion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wesselmeijer/pycsvify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)