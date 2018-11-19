import os
def parseCSV(location, seperator=","):
    """
    Parse a CSV file to a Python Dict

    :param location: The location of the csv file
    :param seperator: The seperator character of the csv file
    """
    if not os.path.isfile(location):
        raise Exception("File not found")
    try:
        csvFile = open(location, "r+")
        csvContent = csvFile.readlines()
        csvDict = {"_content" : {}}
        keyIndex = []
        keyCount = 0
        columnCount = 0
        for line in csvContent:
            if csvContent.index(line) == 0:
                for element in line.split(seperator):
                    keyIndex += [element]
                    csvDict["_content"][element] = []
                    keyCount += 1
                csvDict["_keyCount"] = keyCount
            else:
                position = 0
                for element in line.split(seperator):
                    csvDict["_content"][keyIndex[position]] += [element]
                    position += 1
                columnCount += 1
        csvDict["_columnCount"] = columnCount
        return csvDict

    except:
        raise Exception("Parsing error. Is it the right csv format? Is the seperator okay?")

