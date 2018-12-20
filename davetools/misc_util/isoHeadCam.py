'''
Created on 7 Mar 2016

@author: adave
'''

import maya.cmds as cmds
import maya.mel as mel

def isoHeadCam():
    namespace = ''
    sel = cmds.ls(sl=1)
    print sel
    if (cmds.window("cam", exists=True)):
        cmds.deleteUI("cam")
    hedCamWin = cmds.window(t= 'HeadCamera',w=1000,h=500)
    headPanel = cmds.paneLayout()
    headMP = cmds.modelPanel(cam =cma)
    cmds.showWindow( hedCamWin )
    cmds.select('anyGeom',r=1)
    mel.eval('InvertSelection;')
    #cmds.select(tgl=1,vis=1,ado=1,r=1)
    cmds.isolateSelect(headMP,state=1)
     
    if len(sel) == 0:
        cmds.select(cl=1)
         
    else :
        cmds.select(sel)
      

isoHeadCam()
