# PyCSVify [![Build Status](https://travis-ci.org/wesselmeijer/pycsvify.svg?branch=master)](https://travis-ci.org/wesselmeijer/pycsvify)
A Python library that allows easy conversion from CSV to Dict and back!

## Install

This python library requires Python3, if you already have it installed; use `pip install pycsvify` to download and install the library.

If not, download [Python3](https://www.python.org/) first.

## Usage

To convert a CSV file to a dictionary, use `parseCSVfile(location, seperator)`

To convert a CSV string to a dictionary, use `parseCSV(csvString, itemSeperator, lineSeperator)`

To convert a dictionary to a CSV string, use `exportCSV(dictionary, itemSeperator, lineSeperator)`

---

[PyPi page](https://pypi.org/project/pycsvify/)
