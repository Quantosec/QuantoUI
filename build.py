#!python3

import os
import re

currentDirectory = os.getcwd()

# Get filenames for files
buildNamesFile = open(os.path.join(currentDirectory, "buildNames.txt"), "r")
buildNames = buildNamesFile.read()

licence = buildNames.splitlines()[0]
minJS = buildNames.splitlines()[1]
minCSS = buildNames.splitlines()[2]
docsJS = buildNames.splitlines()[3]
docsCSS = buildNames.splitlines()[4]

buildNamesFile.close()

# Clear all minified files

if minJS != "&":
    workingFile = open(os.path.join(currentDirectory, minJS), "w")

    workingFile.write("")
    workingFile.close()

if minCSS != "&":
    workingFile = open(os.path.join(currentDirectory, minCSS), "w")

    workingFile.write("")
    workingFile.close()

# Licence

if licence != "&":
    if minJS != "&":
        workingFile = open(os.path.join(currentDirectory, minJS), "w")

        workingFile.write("/*\n" + open(os.path.join(currentDirectory, licence), "r").read().replace("&copy;", "(C)") + "\n*/\n")
        workingFile.close()

    if minCSS != "&":
        workingFile = open(os.path.join(currentDirectory, minCSS), "w")

        workingFile.write("/*\n" + open(os.path.join(currentDirectory, licence), "r").read().replace("&copy;", "(C)") + "\n*/\n")
        workingFile.close()

# JavaScript files

if minJS != "&":
    workingFile = open(os.path.join(currentDirectory, minJS), "a")

    currentReadingDirectory = os.path.join(os.getcwd(), "src", "js", "lib")

    for currentFile in os.listdir(os.path.join(currentReadingDirectory)):
        if not os.path.isdir(os.path.join(currentReadingDirectory, currentFile)):
            workingFile.write("\n" + open(os.path.join(currentReadingDirectory, currentFile), "r").read() + "\n")

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

if minCSS != "&":
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

if docsJS != "&":
    workingFile = open(os.path.join(currentDirectory, docsJS), "w")

    workingFile.write("{\n")
    workingFile.close()

    workingFile = open(os.path.join(currentDirectory, docsJS), "a")

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

if docsCSS != "&":
    workingFile = open(os.path.join(currentDirectory, docsCSS), "w")

    workingFile.write("{\n")
    workingFile.close()

    workingFile = open(os.path.join(currentDirectory, docsCSS), "a")

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