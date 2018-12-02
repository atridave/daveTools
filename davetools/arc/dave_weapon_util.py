'''
Created on May 14, 2018

@author: adave
'''



import maya.cmds as cmds


class DailyTool:
    
    def cls(self):
        cmds.select(cl =1)
        
    def sl(self,sel):
        cmds.select(sel)
    
    def sHI(self,selected):
        self.sl(selected)
        cmds.select(hi =1)
        self.selHi = cmds.ls(sl =1)
        return self.selHi
        
    def delHis(self,sel):
        cmds.delete(sel,ch = 1) 
        
        
    def delShape(self,sel):
        cmds.delete(sel,s =1)
    
    def appendIt(self,taret):
        self.temp = []
        for i in range(0,len(taret)):
            self.temp.append(taret[i])
        return self.temp
    

           
class parentIT:
    def __init__(self,child,parent):
        self.child = child
        self.parent = parent
        cmds.parent(self.child,self.parent)            
    
           
class Renamer:
    def __init__(self,name,newName):
        self.name = name
        self.newName = newName
        self.name = cmds.rename(self.name,self.newName)
        
        
class findParent:
    def __init__(self,child):
        self.child = child
        self.parent = cmds.listRelatives(self.child,p =1)
        
    
  
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
 

class JointOperation:
    
    def makeJnt(self,name):
        self.jnt =  cmds.joint(p=(0,0,0),n= name)
        return self.jnt
    
    def jointsInfo(self,joint,allJnt):
        self.stEd = []
        jnt = DailyTool()
        jnt.sl(joint)
        jnt.sHI(joint)
        self.allJoints = cmds.ls(sl =1,typ = 'joint')
        self.stEd.append(self.allJoints[0])
        self.stEd.append(self.allJoints[-1])
        
        if allJnt == 1:
            return self.allJoints
        else:
            return self.stEd       
        

    def jointRecreate(self,joint):
        prifix = 'new_'
        cmds.select(cl=1)
        self.newJnt  =  self.makeJnt(prifix+joint)
        print joint,self.newJnt
        aa =  ApplyConstrain(joint,self.newJnt).pointOriCon(0)
        cmds.delete(aa[0],aa[1])
        cmds.makeIdentity( apply=True, t=1, r=1, s=1)        
        print 'I am recreating all joints'        
        
        
    def creatCtrlJoints(self,xval,yval,zval):
        self.jnt = cmds.joint(p=(xval,yval,zval))
        return self.jnt
    
    def makeDuplicateJointChaines(self,SourceJoint,name,suffix):
        dJoints =  []
        joints =  cmds.duplicate(SourceJoint,n = (name+suffix),rc=1)
        dJoints.append(joints[0])
        for i in range(1,len(joints)):
            nameName =  (joints[i].strip((joints[i][-1])))
            newJntName = cmds.rename(joints[i],(nameName+suffix))
            dJoints.append(newJntName)
        return dJoints
        
        
   


class jointScale:
    def __init__(self,joints,axies,conAttr):
        self.conAttr = conAttr
        self.axies = axies
        self.joints  = joints        
        for i in range(0,len(self.joints)):
            cmds.connectAttr((self.conAttr),(self.joints[i]+'.'+self.axies),f=1)


class CurveOperation:
    
    def __init__(self,curve):
        self.curve = curve
    
    def curveCvInfo(self):
        cvInfo = []
        Degree = cmds.getAttr(self.curve+'.degree')
        Spans =  cmds.getAttr(self.curve+'.spans')
        Cvs = Degree+Spans
        cvInfo.append(Degree)       
        cvInfo.append(Cvs)
        return cvInfo
        
    def convertToBezier(self):
        dtO = DailyTool()
        dtO.sl(self.curve)
        cmds.nurbsCurveToBezier()
        dtO.delHis(self.curve)
        
    def curveSkinCtrls(self,allc,name):
        
        self.ctrlJnts = []
        dtO = DailyTool()
        Crv = self.curveCvInfo()
        joO = JointOperation()        
        dtO.delHis(self.curve)
                       
        for i in range(0,Crv[1]):
            dtO.cls()
            jntPV = cmds.getAttr(self.curve+'.cv[%d]' % i)
            jntP = jntPV[0]
            jnt = joO.creatCtrlJoints(jntP[0],jntP[1],jntP[2])
            self.ctrlJnts.append(jnt)
            dtO.cls()
        if allc == 0:
            cmds.delete(self.ctrlJnts[1])
            cmds.delete(self.ctrlJnts[(Crv[1]-2)])
            self.ctrlJnts.pop(1)
            self.ctrlJnts.pop(-2)
        cmds.select(self.ctrlJnts)
        sel = cmds.ls(sl=1)
        for i in range(0,len(sel)):
            a = i+1
            reJnt =cmds.rename((sel[i]),((name+'0%d') % a ) )
            self.ctrlJnts.pop(0)
            self.ctrlJnts.append(reJnt)
        cmds.select(self.ctrlJnts,self.curve)
        cmds.skinCluster(n = name+'_skin')
        
        return self.ctrlJnts
    
        
         
class Curve(object):
    def __init__(self,curve):
        self.curve = curve
        
class ShapeScaler(Curve):
    def __init__(self,curve,sx,sy,sz):
        Curve.__init__(self, curve)
        self.sx = sx
        self.sy = sy
        self.sz = sz
        cmds.select(self.curve)
        cmds.scale(self.sx,self.sy,self.sz)
        cmds.makeIdentity( apply=True, t=1, r=1, s=1)

class ShapeFinder(Curve):
    def __init__(self,curve):
        Curve.__init__(self,curve)
        self.shape = cmds.listRelatives(self.curve)
        

class ShapeRenamer(ShapeFinder):
    def __init__(self,curve,spName):
        ShapeFinder.__init__(self, curve)
        self.spName = spName
        self.shape = cmds.rename(self.shape,(self.spName+'Shape'))
        
        
class ShapeColor(ShapeRenamer):
    def __init__(self,curve,spName,color):
        ShapeRenamer.__init__(self,curve,spName)
        self.color = color
        cmds.setAttr(self.shape+'.overrideEnabled',1)
        cmds.setAttr(self.shape+'.overrideColor',color)
        
        
        
        
class ShapeDesigner(ShapeColor):
    def __init__(self,curve,spName,color):
        ShapeColor.__init__(self,curve,spName,color)
        cmds.select(self.curve)
        cmds.makeIdentity( apply=True, t=1, r=1, s=1)
        cmds.delete(self.curve,ch =1)
        
        
    def shapeParent(self,ctrlJnt):
        self.ctrlJnt = self.spName
        cmds.parent(self.shape,self.ctrlJnt,r=1,s=1)
        cmds.delete(self.curve)


 



class CtrlLib(object):
    def __init__(self,name):
        self.name = name
        
    def addShapeCurve(self):
        self.ctrl = cmds.curve(d=3,p=[(0,0,0)],k = [0,0,0], n = (self.name))
        
    def makeRefLine(self):
        self.ctrl = cmds.curve(d=1,p=[(0,0,0),(0,0,12)],k = [0,1], n = (self.name))
            
    def makeCube(self):
        self.ctrl =  cmds.curve(d = 1, p = [((1), (1), (1)), ((1), (1), -(1)), (-(1), (1) ,-(1)), (-(1), -(1), -(1)) , ((1), -(1) ,-(1)) , ((1), (1), -(1)) , (-(1), (1), -(1)) , (-(1), (1), (1)) , ((1), (1), (1)) , ((1), -(1), (1)) , ((1) ,-(1), -(1)) , (-(1), -(1) ,-(1)) , (-(1), -(1), (1)) , ((1), -(1), (1)) , (-(1), -(1), (1)) , (-(1), (1) ,(1))],k = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 ], n = (self.name))
        return self.ctrl
    
    def makeCircle(self,nx,ny,nz,redi):
        self.ctrl = cmds.circle(nr = (nx,ny,nz),r=redi,ch=0, n = (self.name))
        self.ctrl = self.ctrl[0]
        return self.ctrl
    
    
    def addDummyShape(self):
        self.ctrl = cmds.curve(d=3,p=[(0,0,0)],k = [0,0,0],n=(self.name))
        return self.ctrl
    
    def makeFourArrow(self):
        self.ctrl = cmds.curve(d=1,p = [(0, 0 ,-1.98) ,(-0.495, 0, -1.32) ,(-0.165 ,0 ,-1.32) ,(-0.165, 0 ,-0.165) ,(-1.32, 0 ,-0.165) ,(-1.32, 0, -0.495) ,(-1.98, 0, 0) ,(-1.32, 0 ,0.495) ,(-1.32, 0, 0.165) ,(-0.165, 0, 0.165) ,(-0.165, 0, 1.32) ,(-0.495, 0, 1.32) ,(0, 0, 1.98) ,(0.495, 0, 1.32) ,(0.165, 0, 1.32) ,(0.165, 0 ,0.165) ,(1.32, 0, 0.165) ,(1.32, 0, 0.495) ,(1.98, 0, 0) ,(1.32, 0 ,-0.495) ,(1.32, 0 ,-0.165) ,(0.165, 0 ,-0.165) ,(0.165, 0 ,-1.32) ,(0.495, 0 ,-1.32) ,(0, 0 ,-1.98)],k = [ 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 , 18 , 19 , 20 , 21 , 22 , 23 , 24], n = (self.name)  )
        return self.ctrl
    
    def makeHip(self,nx,ny,nz,redi):
        self.ctrl = cmds.circle(nr = (nx,ny,nz),r=redi,ch=1, n = (self.name),s=12)
        self.ctrl = self.ctrl[0] 
        cmds.select(cl=1)     
        for i in range(0,12,2):
            cmds.select((self.ctrl+'.cv[%d]')%i,tgl =1)
        cmds.scale(2,2,2)
                    
        return self.ctrl
        
    def makeCog(self):
        self.ctrl = self.makeCube()
        ShapeScaler(self.ctrl,1,0.25,1)
        cmds.select(self.ctrl+'.cv[0:2]',self.ctrl+'.cv[5:8]',self.ctrl+'.cv[15]' )
        cmds.scale(.8,.8,.8)
    
        

    




class MakeCtrl(CtrlLib):
    def __init__(self,name,choice,sx,sy,sz,color,sp =None,spJnt = None,nx=None,ny=None,nz=None,redi=None):
        CtrlLib.__init__(self, name)
        self.choice = choice
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.color = color
        self.sp = sp
        self.spJnt = spJnt
        
        
        
        if self.choice == 0:
            self.addShapeCurve()
           
        if self.choice == 2:
            self.makeCube()
            
        if self.choice == 1:
            self.makeCircle(nx, ny, nz, redi)
        
        if self.choice == 3:
            self.makeFourArrow()
        
        if self.choice ==4:
            self.makeHip(nx, ny, nz, redi)
        
        if self.choice ==5:
            self.makeCog()
        

            
            
        ShapeScaler(self.name,self.sx,self.sy,self.sz)
        ShapeDesigner(self.name,self.name,self.color)
        
        if self.sp :
            ShapeDesigner(self.name,self.spJnt,self.color).shapeParent(self.spJnt)
            
    
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
    
    def parentCon(self,moV):
        self.con =cmds.parentConstraint((self.source),(self.target),mo = moV)
        return self.con
    
    def poleVecCon(self):
        self.con = cmds.poleVectorConstraint(self.source,self.target)
        return self.con


    def pointOriCon(self,moV):
        dtO = DailyTool()        
        con = [self.pointCon(moV),self.orientCon(moV)]
        self.con = dtO.appendIt(con)        
        return self.con
    
    def makeConGrp(self,conType,name=None):
        dtO = DailyTool()
        dtO.cls()
        if name == None:
            name = self.source       
            
        self.target = cmds.group(n = (name+'_g'),em =1)
        if conType == 0:
            self.pointCon(0)
        if conType == 1:
            self.orientCon(0)
        if conType == 2:
            self.pointOriCon(0)
        for i in range(0,len(self.con)):
            cmds.delete(self.con[i])
        
        return self.target
    
    def makeOffGrp(self,conType,name=None):
        self.target = self.makeConGrp(conType)
        cmds.parent(self.source, self.target)
        return self.target
  



class JointRigInfo(object):
    def __init__(self,startJoint):
        self.startJoint = startJoint
        self.joint =  JointOperation()
        dtO = DailyTool()
        self.stEd = self.joint.jointsInfo(self.startJoint,0)
        self.allJnts = self.joint.jointsInfo(self.startJoint,1)
        dtO.cls()        
        


class FkCtrlRig(JointRigInfo):
    def __init__(self,startJoint,ctrlChoice,sx,sy,sz,color,nx=None,ny=None,nz=None,redi=None):
        JointRigInfo.__init__(self, startJoint)        
        self.ctrlChoice = ctrlChoice
        self.sx = sx
        self.sy = sy
        self.sz =sz
        self.color = color       
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.redi = redi
        for i in range(0,len(self.allJnts)):
            cmds.select(self.allJnts[i])
            MakeCtrl(self.allJnts[i]+'_ctrl',self.ctrlChoice,self.sx,self.sy,self.sz,self.color,1,self.allJnts[i],self.nx,self.ny,self.nz,self.redi)


