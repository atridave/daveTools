#imprting moduls
import maya.cmds as cmds

class IKHandle(object):
    def __init__(self,start_joint, end_joint):
        self.start_joint =  start_joint
        self.end_joint =  end_joint        

    def apply_ik(self, type, num_s = None):
        if type == 'ikSplineSolver':
            ik =  cmds.ikHandle(sj = self.start_joint, ee = self.end_joint, sol =  type, ccv =1, ns = num_s)
        else:
            ik =  cmds.ikHandle(sj = self.start_joint, ee = self.end_joint, sol =  type)
        return self.rename_ikh(ik)

    def rename_ikh(ik):
        cmds.rename(ik[1],(self.startJoint+'_eff'))
        ik[1] = ik[1].replace(ik[1],(self.startJoint+'_eff'))
        num = len(ik)
        if num == 3:
            cmds.rename(ik[2],(self.startJoint+'_crv'))
            ik[2] = ik[2].replace(ik[2],(self.startJoint+'_crv'))
        return ik


class ApplyConstrain:
    
    def __init__(self,source,target=None):
        self.source = source
        self.target = target        
        
    def point_con(self,mov):
        self.con = cmds.pointConstraint((self.source),(self.target),mo = mov)
        return self.con
    
    def orient_con(self,moV):
        self.con = cmds.orientConstraint((self.source),(self.target),mo= moV)
        return self.con
    
    def parent_con(self,moV):
        self.con =cmds.parentConstraint((self.source),(self.target),mo = moV)
        return self.con
    
    def polevec_con(self):
        self.con = cmds.poleVectorConstraint(self.source,self.target)
        return self.con


    def pointori_con(self,mov):                
        con = [self.point_con(mov),self.orient_con(mov)]
        self.con = append_it(con)        
        return self.con
    
    def makecon_grp(self,con_type,name=None):
        cmds.select(cl= 1)
        if name == None:
            name = self.source       
            
        self.target = cmds.group(n = (name+'_g'),em =1)
        if con_type == 0:
            self.point_con(0)
        if con_type == 1:
            self.orient_con(0)
        if con_type == 2:
            self.pointori_con(0)
        for i in range(0,len(self.con)):
            cmds.delete(self.con[i])
                    
        return self.target
    
    def makeoff_grp(self,con_type,name=None):
        self.target = self.makecon_grp(con_type,name)
        cmds.parent(self.source, self.target)
        return self.target

class RelationNameHoler:
    def __init__(self,name,attrName):
        self.name = name
        self.attrName = attrName

class DriverDrivenAttrHolder:
    def __init__(self,defaultValue=None,minValue=None,maxValue=None):
        self.defaultValue = defaultValue
        self.minValue = minValue
        self.maxValue = maxValue

class AttributeHolder(RelationNameHoler,DriverDrivenAttrHolder):
    def __init__(self,name,attrName,defaultValue,minValue,maxValue):
        RelationNameHoler.__init__(self, name, attrName)
        DriverDrivenAttrHolder.__init__(self, defaultValue, minValue, maxValue)        


class AddDriverAttr(AttributeHolder):
    def __init__(self,name,attrName,defaultValue,minValue,maxValue,attrType):
        AttributeHolder.__init__(self, name, attrName, defaultValue, minValue, maxValue)
        self.attrType = attrType
        
        cmds.select(self.name)
        if self.attrType == 'float':
            cmds.addAttr(ln = self.attrName,dv = self.defaultValue,min = self.minValue,max = self.maxValue,at = self.attrType,k=1)
        elif self.attrType == 'enum':
            cmds.addAttr(ln=self.attrName,at ='enum',en = self.enum,k=1)
        elif self.attrType == 'bool':
            cmds.addAttr(ln=self.attrName,at ='bool',k=1)


class DriverDriven:
    
    def __init__(self,driven,dnAttr,dnDeValue,dnMin,dnMax,driver,drAttr,drDeValue,drMin,drMax,attrType,enum=None):
        self.driven = driven
        self.dnAttr = dnAttr
        self.dnDeValue = dnDeValue
        self.dnMin = dnMin
        self.dnMax = dnMax
        self.driver = driver
        self.drAttr = drAttr
        self.drDeValue = drDeValue
        self.drMin = drMin
        self.drMax = drMax
        self.attrType = attrType
        self.enum = enum

    
    def setDrive(self,count):
        self.driver = AddDriverAttr(self.driver,self.drAttr,self.dnDeValue,self.drMin,self.drMax,self.attrType,self.enum)
        self.driven = AttributeHolder(self.driven,self.dnAttr,self.dnDeValue,self.dnMin,self.dnMax)
        driverVal = [self.drDeValue,self.drMax,self.drMin]
        drivenVal = [self.dnDeValue,self.dnMax,self.dnMin]
                
        for i in range(0,count):
            cmds.setDrivenKeyframe((self.driven.name+'.'+self.driven.attrName),cd= (self.driver.name+'.'+self.driver.attrName),dv=(driverVal[i]),v=(drivenVal[i]))
        
    
    def ConnectAttr(self):
        self.driver = AddDriverAttr(self.driver,self.drAttr,self.dnDeValue,self.drMin,self.drMax,self.attrType,self.enum)
        self.driven = RelationNameHoler(self.driven,self.dnAttr)
        cmds.connectAttr((self.driver.name+'.'+self.driver.attrName),(self.driven.name+'.'+self.driven.attrName),f=1)
