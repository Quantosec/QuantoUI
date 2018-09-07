#!python3

import os
import re

currentDirectory = os.getcwd()

# Get filenames for files
buildNamesFile = open(os.path.join(currentDirectory, "buildNames.txt"), "r")
buildNames = buildNamesFile.read()

minJS = buildNames.splitlines()[0]
minCSS = buildNames.splitlines()[1]

buildNamesFile.close()

# JavaScript files

workingFile = open(os.path.join(currentDirectory, minJS), "w")

workingFile.write("")
workingFile.close()

workingFile = open(os.path.join(currentDirectory, minJS), "a")

currentReadingDirectory = os.path.join(os.getcwd(), "src", "js")

for currentFile in os.listdir(os.path.join(currentReadingDirectory)):
    if not os.path.isdir(os.path.join(currentReadingDirectory, currentFile)):
        minified = open(os.path.join(currentReadingDirectory, currentFile), "r").read()
        minifiedLine = ""

        for i in range(0, len(minified.splitlines())):
            if not minified.splitlines()[i].startswith("//"):
                minifiedLine += minified.splitlines()[i]

        minified = re.sub("/\*.*?\*/", "", minifiedLine.replace("  ", "").replace("\t", ""), flags=re.DOTALL)

        workingFile.write(minified)

workingFile.close()

# CSS files

workingFile = open(os.path.join(currentDirectory, minCSS), "w")

workingFile.write("")
workingFile.close()

workingFile = open(os.path.join(currentDirectory, minCSS), "a")

currentReadingDirectory = os.path.join(os.getcwd(), "src", "css")

for currentFile in os.listdir(os.path.join(currentReadingDirectory)):
    if not os.path.isdir(os.path.join(currentReadingDirectory, currentFile)):
        minified = open(os.path.join(currentReadingDirectory, currentFile), "r").read()
        minifiedLine = ""

        for i in range(0, len(minified.splitlines())):
            minifiedLine += minified.splitlines()[i]

        minified = re.sub("/\*.*?\*/", "", minifiedLine.replace("  ", "").replace("\t", ""), flags=re.DOTALL)

        workingFile.write(minified)

workingFile.close()

# Documentation generation

## JavaScript files

workingFile = open(os.path.join(currentDirectory, "jsdocs.json"), "w")

workingFile.write("{\n")
workingFile.close()

workingFile = open(os.path.join(currentDirectory, "jsdocs.json"), "a")

currentReadingDirectory = os.path.join(os.getcwd(), "src", "js")

workingFileTemp = ""

for currentFile in os.listdir(os.path.join(currentReadingDirectory)):
    if not os.path.isdir(os.path.join(currentReadingDirectory, currentFile)):
        readingFile = open(os.path.join(currentReadingDirectory, currentFile), "r").read()

        for i in range(0, len(readingFile.splitlines())):
            if readingFile.splitlines()[i].startswith(" * @function"):
                workingFileTemp += '    "' + readingFile.splitlines()[i][13:] + '": {\n'
            elif readingFile.splitlines()[i].startswith(" * @params"):
                workingFileTemp += '        "params": ' + readingFile.splitlines()[i][11:] + ",\n"
            elif readingFile.splitlines()[i].startswith(" * @return"):
                workingFileTemp += '        "return": ' + readingFile.splitlines()[i][11:] + ',\n'
            elif readingFile.splitlines()[i].startswith(" * @info"):
                workingFileTemp += '        "info": "' + readingFile.splitlines()[i][9:] + '"\n    },\n\n'

workingFileTemp = workingFileTemp[:-3] + "\n"

workingFile.write(workingFileTemp + "}")
workingFile.close()

## CSS files

workingFile = open(os.path.join(currentDirectory, "cssdocs.json"), "w")

workingFile.write("{\n")
workingFile.close()

workingFile = open(os.path.join(currentDirectory, "cssdocs.json"), "a")

currentReadingDirectory = os.path.join(os.getcwd(), "src", "css")

workingFileTemp = ""

for currentFile in os.listdir(os.path.join(currentReadingDirectory)):
    if not os.path.isdir(os.path.join(currentReadingDirectory, currentFile)):
        readingFile = open(os.path.join(currentReadingDirectory, currentFile), "r").read()

        for i in range(0, len(readingFile.splitlines())):
            if readingFile.splitlines()[i].startswith(" * @selector"):
                workingFileTemp += '    "' + readingFile.splitlines()[i][13:] + '": {\n'
            elif readingFile.splitlines()[i].startswith(" * @info"):
                workingFileTemp += '        "info": "' + readingFile.splitlines()[i][9:] + '"\n    },\n\n'

workingFileTemp = workingFileTemp[:-3] + "\n"

workingFile.write(workingFileTemp + "}")
workingFile.close()