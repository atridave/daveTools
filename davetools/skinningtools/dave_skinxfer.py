''' 
    Created on Jan 3, 2018
    @author: adave

    Run daveSkinXfer() to use this script
'''

import maya.cmds as cmds
import maya.mel as mel
from PySide2 import QtCore 
from PySide2 import QtGui
from PySide2 import QtWidgets
import sys
import maya._OpenMayaUI as oui
import shiboken2 


def daveSkinXfer():
    if (cmds.window('skinXferUI',ex=1)):
        cmds.deleteUI('skinXferUI')
    daveSkinXferUI().show()
    


#get maya window as parent
def getMayaWindow():
    pointer =  oui.MQtUtil_mainWindow()
    return shiboken2.wrapInstance(long(pointer),QtWidgets.QWidget)
mayaParent =  getMayaWindow()


###compiled UI 
#normally shoulde be loaded from other file

class Ui_skinXferUI(object):
    def setupUi(self, skinXferUI):
        skinXferUI.setObjectName("skinXferUI")
        skinXferUI.resize(500, 370)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(skinXferUI.sizePolicy().hasHeightForWidth())
        skinXferUI.setSizePolicy(sizePolicy)
        skinXferUI.setMinimumSize(QtCore.QSize(500, 370))
        skinXferUI.setMaximumSize(QtCore.QSize(500, 370))
        skinXferUI.setBaseSize(QtCore.QSize(0, 0))
        skinXferUI.setWindowOpacity(1.0)
        self.centralWidget = QtWidgets.QWidget(skinXferUI)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setMinimumSize(QtCore.QSize(500, 370))
        self.centralWidget.setMaximumSize(QtCore.QSize(500, 370))
        self.centralWidget.setObjectName("centralWidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1, 0, 508, 365))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.sourcePushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourcePushButton.sizePolicy().hasHeightForWidth())
        self.sourcePushButton.setSizePolicy(sizePolicy)
        self.sourcePushButton.setMinimumSize(QtCore.QSize(350, 30))
        self.sourcePushButton.setMaximumSize(QtCore.QSize(350, 30))
        self.sourcePushButton.setObjectName("sourcePushButton")
        self.gridLayout.addWidget(self.sourcePushButton, 0, 0, 1, 1)
        self.hierarchycheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hierarchycheckBox.sizePolicy().hasHeightForWidth())
        self.hierarchycheckBox.setSizePolicy(sizePolicy)
        self.hierarchycheckBox.setMinimumSize(QtCore.QSize(150, 30))
        self.hierarchycheckBox.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.hierarchycheckBox.setFont(font)
        self.hierarchycheckBox.setObjectName("hierarchycheckBox")
        self.gridLayout.addWidget(self.hierarchycheckBox, 0, 1, 1, 1)
        self.sourcelistWidget = QtWidgets.QListWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sourcelistWidget.sizePolicy().hasHeightForWidth())
        self.sourcelistWidget.setSizePolicy(sizePolicy)
        self.sourcelistWidget.setMinimumSize(QtCore.QSize(500, 30))
        self.sourcelistWidget.setMaximumSize(QtCore.QSize(500, 30))
        self.sourcelistWidget.setObjectName("sourcelistWidget")
        self.gridLayout.addWidget(self.sourcelistWidget, 1, 0, 1, 2)
        self.targetPushButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetPushButton.sizePolicy().hasHeightForWidth())
        self.targetPushButton.setSizePolicy(sizePolicy)
        self.targetPushButton.setMinimumSize(QtCore.QSize(400, 30))
        self.targetPushButton.setObjectName("targetPushButton")
        self.gridLayout.addWidget(self.targetPushButton, 2, 0, 1, 2)
        self.targetlistWidget = QtWidgets.QListWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.targetlistWidget.sizePolicy().hasHeightForWidth())
        self.targetlistWidget.setSizePolicy(sizePolicy)
        self.targetlistWidget.setMinimumSize(QtCore.QSize(500, 200))
        self.targetlistWidget.setMaximumSize(QtCore.QSize(500, 200))
        self.targetlistWidget.setObjectName("targetlistWidget")
        self.gridLayout.addWidget(self.targetlistWidget, 3, 0, 1, 2)
        self.line = QtWidgets.QFrame(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(500, 0))
        self.line.setMaximumSize(QtCore.QSize(500, 40))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 2)
        self.transferButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transferButton.sizePolicy().hasHeightForWidth())
        self.transferButton.setSizePolicy(sizePolicy)
        self.transferButton.setMinimumSize(QtCore.QSize(500, 40))
        self.transferButton.setMaximumSize(QtCore.QSize(500, 40))
        self.transferButton.setObjectName("transferButton")
        self.gridLayout.addWidget(self.transferButton, 5, 0, 1, 2)
        skinXferUI.setCentralWidget(self.centralWidget)

        self.retranslateUi(skinXferUI)
        QtCore.QMetaObject.connectSlotsByName(skinXferUI)

    def retranslateUi(self, skinXferUI):
        skinXferUI.setWindowTitle(QtWidgets.QApplication.translate("skinXferUI", "daveSkinXfer", None))
        self.sourcePushButton.setText(QtWidgets.QApplication.translate("skinXferUI", "Source Object", None))
        self.hierarchycheckBox.setText(QtWidgets.QApplication.translate("skinXferUI", " Hierarchy", None))
        self.targetPushButton.setText(QtWidgets.QApplication.translate("skinXferUI", "Target Objects", None))
        self.transferButton.setText(QtWidgets.QApplication.translate("skinXferUI", "Transfer Weights", None))





#main UI and signals 

class daveSkinXferUI(QtWidgets.QMainWindow,Ui_skinXferUI):
    def __init__(self, parent = mayaParent):
        super(daveSkinXferUI, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.sourcePushButton,QtCore.SIGNAL("clicked()"),self.updateSource)
        self.connect(self.targetPushButton,QtCore.SIGNAL("clicked()"),self.updateTarget)
        self.connect(self.transferButton,QtCore.SIGNAL("clicked()"),self.transferSkin)
        
    
    def updateSource(self):
        sel =  cmds.ls(sl =1,l=1)
        if(len(sel))== 1:
            self.sourcelistWidget.clear()
            self.sourcelistWidget.addItem(sel[0])
            self.sourcelistWidget.setCurrentRow(0)
            cmds.select(cl=1)
        elif(len(sel))==0:
            QtWidgets.QMessageBox.information(mayaParent,"Information","Please select atleast one source Object")
        else:
             QtWidgets.QMessageBox.critical(mayaParent,"Error","Please select only one source Object")


    def updateTarget(self):
        sel =  cmds.ls(sl =1,l=1)
        if(len(sel))== 0:
            QtWidgets.QMessageBox.information(mayaParent,"Information","Please select atleast one Target Object")
        else:
            self.targetlistWidget.clear()
            self.targetlistWidget.addItems(sel)
            self.targetlistWidget.setCurrentRow(0)
            
            
    def transferSkin(self):
        #check if list is empty
        if(self.sourcelistWidget.count()) == 0 or (self.targetlistWidget.count()) == 0:                             
            QtWidgets.QMessageBox.information(mayaParent,"Information","Please select Source and Target Objects")
        else:
            self.sourceObject =  self.sourcelistWidget.currentItem().text()    
             #check if source obj has skin
            if(SourceSkin(self.sourceObject).getSkinCluster()) == None and self.hierarchycheckBox.isChecked() == False :                                            
                QtWidgets.QMessageBox.critical(mayaParent,"Error","Please select Source Object with skin or Check Hierarchy option")                
            else:
                self.targetObjs = []
                for i in range(0,self.targetlistWidget.count()):
                    #get list of targets
                    self.targetObjs.append(self.targetlistWidget.item(i).text())                                    

                for i in range(0,len(self.targetObjs)):
                    #check if source and target are not same
                    if(self.sourceObject) == self.targetObjs[i]:
                        QtWidgets.QMessageBox.critical(mayaParent,"Error",("Source %s & Target %s Should not be the same" %( self.sourceObject,self.targetObjs[i])))
                    else:
                         #clean mesh
                        cmds.delete(self.targetObjs[i],ch=1)                                                        
                        try:
                            cmds.makeIdentity(self.targetObjs[i],apply=True, t=1, r=1, s=1, n=2 )
                        except:
                            pass
                        #Apply and transfer weights with respecting hierarchy
                        if(self.hierarchycheckBox.isChecked() == True):                            
                            self.sourceObject = HierarchyObjects(self.sourceObject).combineObject()
                            childrens = cmds.listRelatives(self.targetObjs[i],ad = 1,pa =1 ,type = 'transform',ni =1 )                                                      
                            for i in range(0,len(childrens)):
                                try:
                                    TransferWeight(self.sourceObject,childrens[i]).copySkin()                                    
                                except:
                                    pass                                
                            cmds.delete(self.sourceObject)                            
                        else:
                            #Apply and transfer weights 
                            TransferWeight(self.sourceObject,self.targetObjs[i]).copySkin()
                        QtWidgets.QMessageBox.information(mayaParent,"Information","Skin is transferred to Target Object ")
                        try:
                            print 'SkinDump is clean'                           
                        except:
                            pass
                        self.close()




#Source object class for finding skin and influance joints
class SourceSkin:
    def __init__(self,source):
        self.source =  source
   
    def getSkinCluster(self):      
        oHis =  cmds.listHistory(self.source,pdo =1)
        skin = cmds.ls(oHis,type = 'skinCluster') or [None]       
        return(skin[0])

    def getSourceInfJnt(self):
        self.sSkin = self.getSkinCluster()
        self.infJnt =  cmds.skinCluster(self.sSkin,q=1,wi =1)


#Inherited from SourceSkin class with apply skin and copySkin class h

class TransferWeight(SourceSkin):
    def __init__(self,source,target):
        SourceSkin.__init__(self,source)
        self.target =  target        
        self.getSourceInfJnt()
        
    def applySkin(self):        
        cmds.select(self.infJnt)
        self.tarSkin = cmds.skinCluster(self.infJnt,self.target,tsb =1,dr=4,mi=4,sm=1)[0]       

    def copySkin(self):
        self.applySkin()
        cmds.copySkinWeights(ss = self.sSkin,ds = self.tarSkin,nm =1,sa='closestPoint',ia = 'oneToOne')
        self.cleanMesh()
        cmds.select(self.target)
       

    def cleanMesh(self):
         selT =  cmds.ls(type = 'tweak' )
         selBind = cmds.ls(type='dagPose')         
         if(selT):
             cmds.delete(selT)
         if(selBind):
            cmds.delete(selBind)


class HierarchyObjects:
    def __init__(self,parentObject):
        self.parentObject =  parentObject   
        
    def findSkinChildren(self):
        self.children = cmds.listRelatives(self.parentObject,ad = 1,f =1,type = 'transform')
        skinChild = []
        for i in range(0,len(self.children)):
            if(SourceSkin(self.children[i]).getSkinCluster()) != None:
                skinChild.append(self.children[i])
        return skinChild


    def combineObject(self):
        self.skinChilds = self.findSkinChildren()       
        combObjG = []        
        for i in range(0,len(self.skinChilds)):
            dupObj = cmds.duplicate(self.skinChilds[i],n = (self.skinChilds[i]+'_skinDump'))[0]
            TransferWeight(self.skinChilds[i],dupObj).copySkin()            
            combObjG.append(dupObj)
        cmds.select(combObjG)        
        combineMesh = (cmds.polyUniteSkinned(ch= 0,muv =1)[0])
        cmds.select('*_skinDump')        
        cmds.delete(cmds.ls(sl=1)) 
        return combineMesh


       

