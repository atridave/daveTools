'''This is for making  name_EXPORT.ma file from name_rig.ma file'''

import re
import maya.cmds as cmds

def makeExportFile(filePath=None):
    if filePath == None:
        filePath = cmds.file(q=1,sn=1)
        fileName = cmds.file(q=1,sn=1,shn=1)
        print filePath ,fileName       
    else:
        print 'hello'

    topG = '|'+(re.sub('_rig.ma','',fileName))
    print topG
    cmds.setAttr((topG+'.v'), 0)
    cmds.setAttr((topG+'.v'),l = 1)
    childs =  getChilds('cgf_g')
    childs.append(getChilds('skin_g'))
    for i in range(0,len(childs)):
        cmds.parent(childs[i],w =1)

    fileExportSaveAs(filePath)
 
    
def getChilds(object):
    return(cmds.listRelatives(object,c=1))

def fileExportSaveAs(filePath):
    ExportPath =  (filePath).replace('_rig','_EXPORT')
    cmds.file(rn = ExportPath)
    cmds.file(save=1,f=1)


    

makeExportFile()