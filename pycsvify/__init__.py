name = "pycvsify"

import os
def parseCSVfile(location, seperator=","):
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
        itemCount = 0
        for line in csvContent:
            if csvContent.index(line) == 0:
                for element in line.split(str(seperator)):
                    keyIndex += [element]
                    csvDict["_content"][element] = []
                    keyCount += 1
                csvDict["_keyCount"] = keyCount
            else:
                position = 0
                for element in line.split(str(seperator)):
                    csvDict["_content"][keyIndex[position]] += [element]
                    position += 1
                    itemCount += 1
                columnCount += 1
        csvDict["_columnCount"] = columnCount
        csvDict["_itemCount"] = itemCount
        return csvDict

    except:
        raise Exception("Parsing error. Is it the right csv format? Is the seperator okay?")

def parseCSV(csvString, seperator=","):
    """
    Parse a CSV string to a Python Dict

    :param csvString: The csv string variables
    :param seperator: The seperator character of the csv string
    """
    try: 
        csvContent = csvString.split("\n")
        csvDict = {"_content" : {}}
        keyIndex = []
        keyCount = 0
        columnCount = 0
        itemCount = 0
        for line in csvContent:
            if csvContent.index(line) == 0:
                for element in line.split(str(seperator)):
                    keyIndex += [element]
                    csvDict["_content"][element] = []
                    keyCount += 1
                csvDict["_keyCount"] = keyCount
            else:
                position = 0
                for element in line.split(str(seperator)):
                    csvDict["_content"][keyIndex[position]] += [element]
                    itemCount += 1
                    position += 1
                columnCount += 1
        csvDict["_columnCount"] = columnCount
        csvDict["_itemCount"] = itemCount
        return csvDict

    except:
        raise Exception("Parsing error. Is it the right csv format? Is the seperator okay?")

def exportCSV(dictionary, itemSeperator=",", lineSeperator="\n"):
    """
    Generate a CSV string from a dictionary

    :param dictionary: A properly formatted python dictionary
    :param itemSeperator: The seperator that is used to identify individual items
    :param lineSeperator: The seperator that is used to identify individual lines
    """

    resultString = ""
    keyCounter = 0
    keyList = dictionary.keys()

    
    #First Line generation
    for key in keyList:
        resultString += key
        if (keyCounter + 1 != len(keyList)):
            resultString += str(itemSeperator)
        else:
            resultString += str(lineSeperator)
        keyCounter += 1

    itemList = []
    #Second Onwards Line Generation
    for key in keyList:
        itemIndex = 0
        for item in dictionary[key]:
            if len(itemList) < itemIndex + 1:
                itemList += [[str(item)]]
            else:
                try:
                    itemList[itemIndex] += [str(item)]
                except:
                    raise Exception("Incomplete dictionary or improperly formatted.")
            itemIndex += 1

    for itemColumn in itemList:
        itemIndex = 0
        for item in itemColumn:
            resultString += item
            if (itemIndex + 1 != len(itemColumn)):
                resultString += str(itemSeperator)
            else:
                resultString += str(lineSeperator)
            itemIndex += 1

    return resultString




