﻿#!/usr/bin/python
""" G6 to CUB file conversion tool
By Gwenegan Hudin & Nicolas Busseneau
11/02/2013
gwenegan.hudin@insa-rennes.fr

"""

import re
import os, sys
import tempfile
import subprocess
import zlib, zipfile

def convert(inFile):
    inFile.readline()

    # Run showg and store output in a tempFile file
    tempFile = tempfile.NamedTemporaryFile()
    tempFile.readline()
    subprocess.call("\"" +  os.getcwd() + "/\"" + "showg " + "\"" + inFile.name + 
                    "\" " + tempFile.name, shell = True)

    # Looks for the order of the graph in the file
    # Typically, will match "Graph X, order N." and capture N
    for line in tempFile :
	    matchObj = re.match(r'^.+,\s\D+\s(\d+).\s$', line)
	    if matchObj :
		    order = int(matchObj.group(1));
		    break
		
    # Stores the edges of the graph in an array
    graphSets = []
    for line in tempFile :
        node, edges = line.split(':')
        edges = (edges.replace(';','')).split() # Suppress the final ';' and stores edges
        graphSets.insert(int(node), edges)
        
    # Generates the .cub output file
    outputname = inFile.name.split('.')[0]
    outFile = open(os.getcwd() + "/" + outputname + ".cub", 'w+')

    outFile.write(str(order) + "\n")
    for i in range(0, order) :
        outFile.write(str(i) + "\t")
        edges = "\t".join(graphSets[i])
        outFile.write(edges + "\n")
        
        
    outFile.flush()

    inFile.close()
    tempFile.close()
    outFile.close()

# Opens the input file (stdin if not given)
inFile = open(sys.argv[1])
if zipfile.is_zipfile(inFile):
    myzip = zipfile.ZipFile(inFile)
    for filename in myzip.namelist():
        myFile = myzip.open(filename, 'rU')
        convert(myFile)
    myzip.close()
else:
    convert(inFile)
