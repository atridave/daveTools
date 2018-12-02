'''
Created on Aug 17, 2017

@author: adave
'''

import sys,os,json,subprocess
from PySide import QtCore 
from PySide import QtGui
import shiboken
import maya._OpenMayaUI as oui
import maya.cmds as cmds
import Red9.startup.setup as sDir


def getMayaWindow():
    pointer =  oui.MQtUtil_mainWindow()
    return shiboken.wrapInstance(long(pointer),QtGui.QWidget)

mayaParent =  getMayaWindow()




def ikGripUpdate():
    sel = cmds.ls(sl=1)
    ikGripUtil(sel).ikGripUpdateDoit()

class ikGripUtil:
    def __init__(self,ctrl):
        self.ctrl =  ctrl       
                   
    def error(self):
        QtGui.QMessageBox.critical(mayaParent,"Error","Select IKGrip and Run this Script")
    
    def ikGripUpdateDoit(self):
        if len(self.ctrl) != 1:
            self.error()
        else:
            ikGripCtrl = 'IkGripTarget_Ctr'
            rootCtrl = 'root_Ctr'
            name  =  self.ctrl[0].split(':')
            if name[1] != ikGripCtrl:
                self.error()
            else:
                rootCtrl =  (name[0]+':'+rootCtrl)
                info =  self.getInfo(rootCtrl)            
                tempFile = (cmds.file(q=1,sn=1)).replace('.ma','.py')
                ikGripValue = self.getikGripValue(rootCtrl)
                
                tempSaFile = self.writeTempFile(tempFile,info,ikGripValue)
                                     
                standalone().subProcess(tempSaFile)            
                os.remove(tempSaFile)

                text =  "IKgrip is updated \n"
                text += "submit your checked out weapon files\n"
                text += "after Testing in game"
                msgBox =  QtGui.QMessageBox.information(mayaParent,"Information",text)

        
                

 
    def getInfo(self,rootCtrl):
        info =  []
        nodeType = 'network'
        mTag = cmds.listConnections(rootCtrl,d=False, s=True ,et=1, t = nodeType)[0]
        eTag = cmds.listConnections( mTag, d=True, s=False,et=1, t= nodeType)[0]
        
        try:
            data =  json.loads(cmds.getAttr(eTag+'.assetData'))
            CHR =  cmds.getAttr(eTag+'.skeletonAlias')
            info.append(data['file_path'])
            info.append(CHR)
            return info
        except:
            text =  "You havn't attached weapon with Asset Manager \n"
            text += "Attach Weapon with Asset Manager and\n"
            text += "Run this script"
            msgBox =  QtGui.QMessageBox.critical(mayaParent,"Error",text)
            from Red9_ClientCore.CloudImp import MenuStubs;MenuStubs('CIG_Assetmanager')
            sys.exit()
       

    
    
    def getikGripValue(self,rootCtrl):
        cmds.select(cl=1)
        rootLoc =  cmds.spaceLocator( p=(0, 0, 0),n="ikGripRoot_loc")
        ikGripLoc =  cmds.spaceLocator( p=(0, 0, 0),n="ikGrip_loc")
        ikGripWorldloc = cmds.spaceLocator( p=(0, 0, 0),n="ikGripWorld_loc")
        cmds.parent(ikGripLoc[0],rootLoc[0])
        rootCon = ApplyConstrain(rootCtrl,rootLoc[0]).pointOriCon(0)
        ikGripCon = ApplyConstrain(self.ctrl,ikGripLoc[0]).pointOriCon(0)
        cmds.delete(rootCon[0],rootCon[1],ikGripCon[0],ikGripCon[1])
        con =  ApplyConstrain(ikGripWorldloc[0],rootLoc[0]).pointCon(0)
        cmds.delete(con[0])
        cmds.parent(ikGripLoc,w=1)
        tVal = cmds.getAttr(ikGripLoc[0]+'.translate')
        rVal = cmds.getAttr(ikGripLoc[0]+'.rotate')
        ikGripValue = [tVal[0][0],tVal[0][1],tVal[0][2],rVal[0][0],rVal[0][1],rVal[0][2]]
        cmds.delete(rootLoc,ikGripLoc,ikGripWorldloc)
        cmds.select(self.ctrl)
        return ikGripValue
    
    def writeTempFile(self,tempFile,info,ikGripValue):
       
        baseR9ScriptPath = sDir.red9ModulePath()
        ikGscript = os.path.abspath(os.path.join(baseR9ScriptPath,"../cig/anim/ikGripStandalone.py"))      
        dumpFile = (open(ikGscript,'r'))
        text =  dumpFile.readlines()
        dumpFile.close()
        text.insert(12,'scriptFile = "%s"\n' % (tempFile))
        text.insert(13,'basePath = "%s"\n' % info[0])
        text.insert(14,'ikGripCtrl = "IkGripTarget_Ctr"\n')
        text.insert(15,'CHR = "%s"\n' % info[1])
        text.insert(16,'ikGripCtrlValue = %s \n' % ikGripValue)
        fileW = open(tempFile,'w')         
        fileW.writelines(text)       
        fileW.close()
        return tempFile

    
class standalone:    
    def __init__(self):
        self.mayapy = (sys.executable).replace('maya','mayapy')        
        
    def subProcess(self,tempScriptFile):
        subprocess.Popen([self.mayapy,tempScriptFile]).communicate()
   
    



class ApplyConstrain:
    
    def __init__(self,source,target=None):
        self.source = source
        self.target = target           
        
    def pointCon(self,moV):
        self.con = cmds.pointConstraint((self.source),(self.target),mo = moV)
        return self.con
    
    def orientCon(self,moV):
        self.con = cmds.orientConstraint((self.source),(self.target),mo= moV)
        return self.con   

    def pointOriCon(self,moV):           
        self.con = [self.pointCon(moV),self.orientCon(moV)]       
        return self.con  




