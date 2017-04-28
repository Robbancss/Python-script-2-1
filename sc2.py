import types
import re
import json
import os

for fileNames in os.listdir('./'):
    ls = []
    if fileNames[5:] == ".prog":
        with open(fileNames, 'r') as progFile:

            for line in progFile:
                ls.append(line.replace("ELAGAZAS", "if").replace("CIKLUS", "for"))

        with open(fileNames.replace(".prog", ".py"), 'w') as pyFile:
            for line in ls:
                szokoz = "    "
                four = re.search("\s{4}\w+", line)
                if line.find("[[") != -1:
                    pyFile.write(line.replace("[[", ":\n"+szokoz).replace(";", "\n"+szokoz).replace("]]", ""))
                else:
                    pyFile.write(line.replace(";","\n"))