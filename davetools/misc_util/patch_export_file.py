import maya.cmds as cmds
import sys,os,json,subprocess




def patchit():
    sel = cmds.ls(sl=1)
    PatchFile(sel[0]).pathIt()

class PatchFile:

    def __init__(self,jnt):
        self.jnt =  jnt

    def pathIt(self):        
        basePath = cmds.file(q=1,sn=1)
        tempFile = (basePath).replace('.ma','.py')
        print 'Hello I am after Chr'
        CHR = ((cmds.file(q=1,sn=1,shn=1)).rsplit('_rig.ma'))[0]
        print CHR
        
        name =  self.jnt
        xValue =  cmds.getAttr(name+'.tx')
        yValue =  cmds.getAttr(name+'.ty')
        zValue =  cmds.getAttr(name+'.tz')


        tempSaFile = self.writeTempFile(tempFile,basePath,name,xValue,yValue,zValue,CHR)
        standalone().subProcess(tempSaFile)
        os.remove(tempSaFile)


    def writeTempFile(self,tempFile,basePath,name,xValue,yValue,zValue,CHR):        
        saCcript = os.path.abspath("path")      
        dumpFile = (open(saCcript,'r'))
        text = dumpFile.readlines()
        dumpFile.close()
        text.insert(10,'scriptFile = "%s"\n' % (tempFile))
        text.insert(11,'jntName = "%s"\n' % name)
        text.insert(12,'xValue = %f \n' % xValue)
        text.insert(13,'yValue = %f \n' % yValue)
        text.insert(14,'zValue = %f\n' % zValue)
        text.insert(15,'CHR = "%s"\n' % CHR)
        text.insert(16,'basePath = "%s"\n' % basePath)
        
        fileW = open(tempFile,'w')         
        fileW.writelines(text)       
        fileW.close()
        return tempFile



class standalone:    
    def __init__(self):
        self.mayapy = (sys.executable).replace('maya','mayapy')        
        
    def subProcess(self,tempScriptFile):
        subprocess.Popen([self.mayapy,tempScriptFile]).communicate()



#patchit()
