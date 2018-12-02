'''
Created on Aug 17, 2017

@author: adave
'''

import maya.standalone
maya.standalone.initialize(name='python')
import maya.cmds as cmds
import sys,P4,shutil,os




def updateIkGrip(basePath):
    fhig = FileHandleIkGrip(basePath)
    fhig.cheOutFiles()   
    fhig.updateFiles()
    fhig.moveCHR()
    os._exit(0)





    


class FileHandleIkGrip():
    def __init__(self,basePath):
        self.basePath =  basePath
        self.p4 = P4Util()
        self.rigSfile = (self.p4.streamGetter()+self.basePath)
        self.rigRfile = (self.p4.rootGetter()+self.basePath)
        self.ExportFile = (self.rigSfile).replace('_rig','_EXPORT')
        self.ExportRFile = (self.rigRfile).replace('_rig','_EXPORT')
        self.chr =  (self.rigSfile.replace('!source/','').replace('_rig.ma','.chr'))
        self.ExSchr =  self.rigRfile.replace('_rig.ma','.chr')
        self.ExDChr = (self.rigRfile.replace('!source/','').replace('_rig.ma','.chr'))
        self.chrName = ('cryExportNode_'+CHR)
        self.files = [(self.ExportRFile),(self.rigRfile)]
        
    def cheOutFiles(self):
        cFiles = [self.rigSfile,self.ExportFile,self.chr]
        for i in range(0,len(cFiles)):
            self.p4.checkOutfile('edit', cFiles[i])
    
    def updateFiles(self):
        
        for i in range(0,len(self.files)):
            cmds.file(self.files[i],f=1,open=1)
            self.adjustParent()
            if i == 0:               
                self.exportCHR()                
            cmds.file(force=True, type='mayaAscii', save=True )          
        
    
    def adjustParent(self):
        parent = (cmds.listRelatives(ikGripCtrl,p =1))[0]
        LockHide(parent,0,0,0,0,0,0,1,1,1,1)
        cmds.select(cl=1)
        tempLoc = cmds.spaceLocator( p=(0, 0, 0),n="tempGrip_loc")
        attr = ['.tx','.ty','.tz','.rx','.ry','.rz']
        for i in range(0,6):
            cmds.setAttr((tempLoc[0]+attr[i]),ikGripCtrlValue[i])
        con = ApplyConstrain(tempLoc[0],parent).pointOriCon(0)
        cmds.delete(con[0],con[1],tempLoc[0])
        LockHide(parent,1,1,1,1,1,1,1,1,1,1)
    
    def exportCHR(self):
        parent = (cmds.listRelatives(self.chrName,p =1))
        if parent != None:
            cmds.parent(self.chrName,w=1)        
        cmds.file("dummyExportName",op = (("cryExportType=geom;crySelectedMaterialsOnly=1;selectedExportNodes={0};cryExportType=geom;crySelectedMaterialsOnly=1;selectedExportNodes={1};cryExportRemoveNamespaces=1;cryExportExportANMs=1;cryExportExportSceneAsZUp=0;").format(self.chrName,self.chrName)),typ = "MayaCryExport",pr =1,ea = 1)
        if parent != None:
            cmds.parent(self.chrName,parent)
        
    
    def moveCHR(self):
        shutil.move(self.ExSchr, self.ExDChr)
        
                

        
        
        
#To do : need to put all helperScripts  in general utility file  
    


class P4Util:
    
    def __init__(self):
        self.p4 = P4.P4()
        self.p4.connect()
        self.info = self.p4.run_info()
               
    def rootGetter(self):        
        return self.info[0]['clientRoot']
    
    def streamGetter(self):
        return self.info[0]['clientStream']      
        
    def checkOutfile(self,command,fullPath):
        try:
            self.p4.run('sync',"-f",fullPath)
            self.p4.run(command,"-f",fullPath)
        except:
            pass
        
        
class LockHide:
    def __init__(self,obj,tx,ty,tz,rx,ry,rz,sx,sy,sz,v,radi = None):
        self.obj = obj
        self.tx = tx
        self.ty = ty
        self.tz = tz
        self.rx = rx
        self.ry = ry
        self.rz = rz
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.v = v
        self.radi = radi
        
        self.attrs = ['.tx','.ty','.tz','.rx','.ry','.rz','.sx','.sy','.sz','.v']
        self.attrVal = [self.tx,self.ty,self.tz,self.rx,self.ry,self.rz,self.sx,self.sy,self.sz,self.v]
              
        for i in range(0,len(self.attrs)):
            if self.attrVal[i] == 1:
                key = 0
            else :
                key = 1
            cmds.setAttr((self.obj+self.attrs[i]),l=self.attrVal[i],k=key)
        
        if self.radi:
            cmds.setAttr(self.obj+'.radi', l=0,k=1)
            cmds.setAttr(self.obj+'.radi', l=1,k=0)
            
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


updateIkGrip(basePath)
