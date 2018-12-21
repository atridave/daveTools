'''
Created on Feb 1, 2017
@author: Atri Dave
'''
import sys
import maya.OpenMaya as OpenMaya
import maya.OpenMayaMPx as OpenMayaMPx
import maya.OpenMayaAnim as OpenMayaAnim
import math

nodeName =  "velocityNode"
nodeID  = OpenMaya.MTypeId(0x7ffff)

class velocityNode(OpenMayaMPx.MPxNode):
    
    velocity =  OpenMaya.MObject()
    inPutCurrentX = OpenMaya.MObject()
    inPutCurrentY = OpenMaya.MObject()
    inPutCurrentZ = OpenMaya.MObject()
    inPutPastX = OpenMaya.MObject()
    inPutPastY = OpenMaya.MObject()
    inPutPastZ = OpenMaya.MObject()
    inPutFutureX = OpenMaya.MObject()
    inPutFutureY = OpenMaya.MObject()
    inPutFutureZ = OpenMaya.MObject()

    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)
        
    def compute(self,plug,dataBlock):                           
          
        if plug == velocityNode.velocity:
             plugX = OpenMaya.MPlug( self.thisMObject(), OpenMaya.MFnDependencyNode(self.thisMObject()).attribute('inPutX'))
             plugY = OpenMaya.MPlug( self.thisMObject(), OpenMaya.MFnDependencyNode(self.thisMObject()).attribute('inPutY'))
             plugZ = OpenMaya.MPlug( self.thisMObject(), OpenMaya.MFnDependencyNode(self.thisMObject()).attribute('inPutZ'))
             time = OpenMayaAnim.MAnimControl.currentTime()
             valXPast = plugX.asDouble(OpenMaya.MDGContext(time-1))
             valYPast = plugY.asDouble(OpenMaya.MDGContext(time-1))
             valZPast = plugZ.asDouble(OpenMaya.MDGContext(time-1))
             valXcurr = plugX.asDouble(OpenMaya.MDGContext(time))
             valYcurr = plugY.asDouble(OpenMaya.MDGContext(time))
             valZcurr = plugZ.asDouble(OpenMaya.MDGContext(time))
             valXNext = plugX.asDouble(OpenMaya.MDGContext(time+1))
             valYNext = plugY.asDouble(OpenMaya.MDGContext(time+1))
             valZNext = plugZ.asDouble(OpenMaya.MDGContext(time+1))

             velocityVal =  (( (math.sqrt(((valXNext-valXcurr)*( valXNext-valXcurr))+(( valYNext-valYcurr)*(valYNext-valYcurr))+(( valZNext-valZcurr)*(valZNext-valZcurr))) +
                     math.sqrt(((valXcurr-valXPast)*(valXcurr-valXPast))+((valYcurr-valYPast)*(valYcurr-valYPast))+((valZcurr-valZPast)*(valZcurr-valZPast))))*0.5 ) *30)

             dataHandlevelocityVal =  dataBlock.outputValue(velocityNode.velocity)
             dataHandlevelocityVal.setFloat(velocityVal)            
             dataBlock.setClean(plug)
        else :
            return OpenMaya.kUnknownParameter                  
            
            
def nodeCreator():
    return OpenMayaMPx.asMPxPtr(velocityNode())


def nodeInitializer():
    
    mFnAttr =  OpenMaya.MFnNumericAttribute()
    velocityNode.velocity = mFnAttr.create("velocity",'velo',OpenMaya.MFnNumericData.kFloat)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(0)
    mFnAttr.setWritable(0)
    mFnAttr.setKeyable(0) 

    velocityNode.inPutCurrentX = mFnAttr.create("inPutX",'incX',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
         
    velocityNode.inPutCurrentY = mFnAttr.create("inPutY",'incY',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
     
    velocityNode.inPutCurrentZ = mFnAttr.create("inPutZ",'incZ',OpenMaya.MFnNumericData.kFloat,0.0)
    mFnAttr.setReadable(1)
    mFnAttr.setStorable(1)
    mFnAttr.setWritable(1)
    mFnAttr.setKeyable(1)
    
    
   
   
            
    velocityNode.addAttribute(velocityNode.velocity)
    velocityNode.addAttribute(velocityNode.inPutCurrentX)
    velocityNode.addAttribute(velocityNode.inPutCurrentY)
    velocityNode.addAttribute(velocityNode.inPutCurrentZ)   
         
    velocityNode.attributeAffects(velocityNode.inPutCurrentX,velocityNode.velocity)
    velocityNode.attributeAffects(velocityNode.inPutCurrentY,velocityNode.velocity)
    velocityNode.attributeAffects(velocityNode.inPutCurrentZ,velocityNode.velocity)


    
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject,'Atri Dave','1.0')
    try:
        mplugin.registerNode( nodeName, nodeID,nodeCreator,nodeInitializer )
    except:
        sys.stderr.write( "Failed to register Node: %s\n" % nodeName )
        raise

def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( nodeID )
    except:
        sys.stderr.write( "Failed to unregister Node: %s\n" % nodeName )
