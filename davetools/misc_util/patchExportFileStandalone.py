import maya.standalone
maya.standalone.initialize(name='python')
import maya.cmds as cmds
import sys,P4,shutil,os


























def patchFile():
    fhp = FileHandlePatcher(basePath)
    fhp.cheOutFiles()   
    fhp.updateFiles()    
    os._exit(0)




class FileHandlePatcher():
    def __init__(self,basePath):
        self.basePath =  (basePath).rsplit('F:/starcitizen')[1]
        self.p4 = P4Util()


        self.rigSfile = (self.p4.streamGetter()+self.basePath)
        self.rigRfile = (self.p4.rootGetter()+self.basePath)
        self.ExportFile = (self.rigSfile).replace('_rig','_EXPORT')
        self.ExportRFile = (self.rigRfile).replace('_rig','_EXPORT')
        self.chr =  (self.rigSfile.replace('!source/','').replace('_rig.ma','.chr'))
        self.ExSchr =  self.rigRfile.replace('_rig.ma','.chr')
        self.ExDChr = (self.rigRfile.replace('!source/','').replace('_rig.ma','.chr'))
        self.chrName = ('cryExportNode_'+CHR)
        self.files = [(self.ExportRFile)]
        
    def cheOutFiles(self):
        cFiles = [self.ExportFile,self.chr]
        for i in range(0,len(cFiles)):
            self.p4.checkOutfile('edit', cFiles[i])
    
    def updateFiles(self):
        
        for i in range(0,len(self.files)):
            cmds.file(self.files[i],f=1,open=1)
            self.addJoint()             
            cmds.file(force=True, type='mayaAscii', save=True )          
        
    
    def addJoint(self):
        cmds.select(cl =1)
        self.adsJnt = cmds.joint( p=(xValue, zValue, yValue),n = jntName)
        self.adsJnt = cmds.parent(self.adsJnt,"root")
        
        print self.adsJnt
        print 'Above is new name'
        cmds.select(self.adsJnt)
        print 'I have select the joint'
        cmds.setAttr((self.adsJnt[0]+'.jointOrientX'),0)
        cmds.setAttr((self.adsJnt[0]+'.jointOrientY'),0)
        cmds.setAttr((self.adsJnt[0]+'.jointOrientZ'),0)
        

    def exportCHR(self):
        cmds.loadPlugin( 'F:\\SCTools\\Tools\\ArtTools\\Maya\\Red9_Dev\\Red9_ClientCore\\CloudImp\\plugins\\2016\\MayaCryExport22016_64.mll' )
        parent = (cmds.listRelatives(self.chrName,p =1))
        if parent != None:
            cmds.parent(self.chrName,w=1)        
        cmds.file("dummyExportName",op = (("cryExportType=geom;crySelectedMaterialsOnly=1;selectedExportNodes={0};cryExportType=geom;crySelectedMaterialsOnly=1;selectedExportNodes={1};cryExportRemoveNamespaces=1;cryExportExportANMs=1;cryExportExportSceneAsZUp=0;").format(self.chrName,self.chrName)),typ = "MayaCryExport",pr =1,ea = 1)
        if parent != None:
            cmds.parent(self.chrName,parent)
        
    
    def moveCHR(self):
        shutil.move(self.ExSchr, self.ExDChr)



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

patchFile()