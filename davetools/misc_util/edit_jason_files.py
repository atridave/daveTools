'''
Created on Nov 8, 2016

@author: adave
'''

import os
import glob
import json

def getFiles(path,ext):
    files = []   
    os.chdir(path)
    sourcefiles =  glob.glob('*'+ext)
    for i in range(0,len(sourcefiles)):
        files.append((path+'\\'+sourcefiles[i]))
    return files

def editFiles(fileData ,skeletonAlias):
    openFile = json.loads(open(fileData,'r').read())
    with open(fileData, 'w') as outfile:
        openFile["build"]["skeletonAlias"] = skeletonAlias
        json.dump(openFile, outfile, indent=4, sort_keys=True)

def updateFiles(path,ext,skeletonAlias):
    filedata = getFiles(path,ext)
    for i in range(0,len(filedata)):
        editFiles(filedata[i],skeletonAlias)


path = 'path'
ext = '.animsettings'

updateFiles(path,ext,'changeIT')
