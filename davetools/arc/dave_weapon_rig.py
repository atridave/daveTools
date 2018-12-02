
'''
Created on 10 Feb 2016

@author: adave
'''

''' Ex..  makeBasicSetup('blmg_fps_gmni_f55') for creating basic group with Joints '''
''' Add Extra joint which is needed by weapon Rig and parent it to root joint or respective joints '''
''' Run makeRig fuction form weapon class as an object to generate rig'''


import sys,os
import maya.cmds  as cmds
import maya.mel as mel
import arc.dave_weapon_util as cwutil

UIFile = ui.loadUiType(os.path.join(os.path.dirname(__file__), 'CIGWeaponRigUI.ui'))[1]

def cigWeaponRig():
    if (cmds.window('CIGWeaponRigUI',ex=1)):
        cmds.deleteUI('CIGWeaponRigUI')
    CIGWeaponRigUI().show()

class CIGWeaponRigUI(QMainWindow,UIFile):
    def __init__(self, parent = ui.MAYAWINDOW):
        super(CIGWeaponRigUI, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.basicSetupPushButton,SIGNAL("clicked()"),self.makeBasicSetup)
        self.connect(self.makeRigCtrlPushButton,SIGNAL("clicked()"),self.makerigCtrl)        

    def makeBasicSetup(self):
        print 'I will make basic setup'

    def makerigCtrl(self):
        print 'I will make Rig ctrls'

def makeBasicSetup(name):
    wr = weaponRig(name)
    wr.makeAllBasicGroup()
    wr.makeAllJnts()
    wr.makeRootRig()
    

class weaponRig():

    def __init__(self,itemName=None):
        self.itemName =  itemName
    
    def makeBasicGroup(self,name):
        self.name  =  name
        self.grp =  cmds.group( em=True, name= (self.name) )
        cmds.select(cl=1)
        return self.grp
        
        
    def makeAllBasicGroup(self):         
        self.itemGrp = self.makeBasicGroup(self.itemName)
        self.SceneRoot = self.makeBasicGroup('SceneRoot')
        self.makeEngineReady(self.SceneRoot,(90,0,180))
        
        self.grps = ['rig','geometry','export','cgf','skin','CHR','oldMeshRef']
        self.phyGrp = []
        for i in range(0,len(self.grps)):            
            self.phyGrp.append(self.makeBasicGroup(self.grps[i]+'_g'))   
       
        cmds.parent(self.phyGrp[0],self.itemGrp)
        cmds.parent(self.phyGrp[1],self.itemGrp)
        cmds.parent(self.phyGrp[2],self.phyGrp[1])
        cmds.parent(self.phyGrp[3],self.phyGrp[2])
        cmds.parent(self.phyGrp[4],self.phyGrp[2])
        cmds.parent(self.phyGrp[5],self.phyGrp[2])
        cmds.parent(self.phyGrp[6],self.phyGrp[2])
        cmds.parent(self.SceneRoot,self.phyGrp[0])       

        
                 
    def makeJnt(self,name,parent):
        self.name = name
        value =  [90,0,180]
        cmds.select(cl=1)        
        self.Jnt =  cmds.joint(n = self.name)
        self.makeEngineReady(self.Jnt,value)
        cmds.makeIdentity( self.Jnt,apply=True )
        cmds.parent(self.Jnt,parent)
      
            
            
    def makeAllJnts(self):
        self.joints =  ['root','weapon_term','trigger','magAttach','safe','magrelease','stock','ADS_align','IkGripTarget']
        for i in range(len(self.joints)):
            if i == 0:
                self.makeJnt(self.joints[i],'SceneRoot')
            else:
                self.makeJnt(self.joints[i], self.joints[0])           
       

    def makeEngineReady(self,obj,value):
        self.obj =  obj
        self.value =  value
        rotateAxies =  ['.rx','.ry','.rz']
               
        for i in range(len(self.value)):
            cmds.setAttr((self.obj+rotateAxies[i]),self.value[i])

    def makeRootRig(self):
        root =  'root'
        cmds.select(root)        
        self.makeRig()        
        cmds.parent(((cwutil.findParent(cmds.ls(sl=1)[0]).parent)),self.itemName)
        self.makePhysSetup()        
        self.red9HookUp()
        cmds.select('root_Ctr')

        
    def makeRig(self):
        self.sel = cmds.ls(sl=1)
        rigCtrls = []
        if self.sel:
            for i in range(len(self.sel)):
                cmds.select(cl=1)
                self.parent = cmds.listRelatives(self.sel[i],p=1)
                self.joint = cwutil.JointOperation().makeJnt(self.sel[i]+'_Ctr')
                self.jntG = cwutil.ApplyConstrain(self.joint).makeOffGrp(2)
                self.con =  cwutil.ApplyConstrain(self.sel[i],self.jntG).pointOriCon(0)
                cmds.delete(self.con[0],self.con[1])
                if(self.parent[0] != None ) and (self.parent[0] != 'SceneRoot' ):                    
                    cmds.parent(self.jntG,(self.parent[0]+'_Ctr'))
                self.con =  cwutil.ApplyConstrain( self.joint,self.sel[i]).pointOriCon(0)
                cwutil.LockHide(self.jntG,1,1,1,1,1,1,1,1,1,1)
                
                if self.sel[i] == 'root':
                    cwutil.FkCtrlRig(self.joint,2,5,15,15,17)
                else:
                    cwutil.FkCtrlRig(self.joint,2,5,5,5,6)
                
                cwutil.LockHide(self.joint,0,0,0,0,0,0,1,1,1,1,1)
                cwutil.DailyTool().appendIt(self.joint)
                cmds.select(self.joint)
        else:
            sys.stdout.write('give me some node to work')
        return rigCtrls

    def makePhysSetup(self):
        self.parentFPhyLoc =  cmds.spaceLocator(n=('root_PhysParentFrame'))
        self.phyLoc =  cmds.spaceLocator(n=('root_Phys'))
        self.makeEngineReady(self.parentFPhyLoc[0],(90,0,180))
        self.makeEngineReady(self.phyLoc[0],(90,0,180))        
        cmds.parent(self.phyLoc[0],self.parentFPhyLoc[0])
        cmds.parent(self.parentFPhyLoc,'rig_g')
        cwutil.LockHide(self.parentFPhyLoc[0],0,0,0,0,0,0,0,0,0,0)
        phyGeo =  cmds.polyCube(n='root_PhysGeo',w=10,h=20,d=50,ch=0)
        cmds.parent(phyGeo[0],'root')
        cmds.makeIdentity(phyGeo[0],apply=True )        
        cmds.addAttr('root_Ctr',ln='proxy',at = 'enum', en= ('Off:On'),k=1)
        cmds.connectAttr('root_Ctr.proxy',(phyGeo[0]+".visibility"), f=1)
        phyGeo = cmds.rename(phyGeo,'root_Phys')
        cmds.setAttr(('root_PhysParentFrame.visibility'),0)
        cwutil.LockHide('root_PhysParentFrame',0,0,0,0,0,0,0,0,0,1)
        cmds.select(cl=1)



