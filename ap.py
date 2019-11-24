import sys
from distutils.dir_util import copy_tree
import json

# read and parse JSON file
with open('settings.json') as json_file:
    data = json.load(json_file)
    closeWhenDone = data['closeWhenDone']
    ask = data['askBeforeCopying']

    spot = 0

    for i in data['output']:
        inputFolder = data['input'][spot]
        outputFolder = data['output'][spot]

        # Give output
        if (ask == False):
            pick = "y"
        else:
            pick = input("Are you sure you want to copy\n"+data['input'][spot]+" to "+ data['output'][spot]+"? [Y/N]")


        if pick == "y":
            print("Copying...")
            copy_tree(inputFolder, outputFolder)
            print("Coded with ♥ by Adam Jackson\n")

            print("Data Copied!")
            print("Copied from " + inputFolder + " to " + outputFolder)
            spot += 1

            if not closeWhenDone:
                input("Press any key to close...")
        elif (pick == "n"):
            sys.exit(0)
        else:
            print("Sorry invalid input")
            input("Press any key to close...")
