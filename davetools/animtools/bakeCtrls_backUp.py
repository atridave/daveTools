'''
Created on Aug 15, 2017

@author: adave
'''

import maya.cmds as cmds
from PySide import QtCore 
from PySide import QtGui
import sys
import maya._OpenMayaUI as oui
import shiboken

def backCtrl():
    sel = cmds.ls(sl=1)
    if len(sel) == 2:
        if (cmds.window('bakeDialog',ex=1)):
            cmds.deleteUI('bakeDialog')         
        bakeCtrlsUI(sel[0],sel[1]).show() #load UI        
    else:
        sys.stderr.write("Please Select two ctrl Source then Target")  


#get maya window as parent
def getMayaWindow():
    pointer =  oui.MQtUtil_mainWindow()
    return shiboken.wrapInstance(long(pointer),QtGui.QWidget)
mayaParent =  getMayaWindow()



#Helper constraint class
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


###compiled UI 

class Ui_bakeDialog(object):
    def setupUi(self, bakeDialog):
        bakeDialog.setObjectName("bakeDialog")
        bakeDialog.resize(230, 60)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bakeDialog.sizePolicy().hasHeightForWidth())
        bakeDialog.setSizePolicy(sizePolicy)
        self.widget = QtGui.QWidget(bakeDialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 230, 60))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(230, 60))
        self.widget.setMaximumSize(QtCore.QSize(230, 60))
        self.widget.setObjectName("widget")
        self.layoutWidget = QtGui.QWidget(self.widget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 232, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startLabel = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startLabel.sizePolicy().hasHeightForWidth())
        self.startLabel.setSizePolicy(sizePolicy)
        self.startLabel.setMinimumSize(QtCore.QSize(54, 20))
        self.startLabel.setMaximumSize(QtCore.QSize(54, 20))
        self.startLabel.setObjectName("startLabel")
        self.horizontalLayout.addWidget(self.startLabel)
        self.startSpinBox = QtGui.QSpinBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startSpinBox.sizePolicy().hasHeightForWidth())
        self.startSpinBox.setSizePolicy(sizePolicy)
        self.startSpinBox.setMinimumSize(QtCore.QSize(50, 20))
        self.startSpinBox.setMaximumSize(QtCore.QSize(50, 20))
        self.startSpinBox.setMinimum(-1000000)
        self.startSpinBox.setMaximum(1000000)
        self.startSpinBox.setObjectName("startSpinBox")
        self.horizontalLayout.addWidget(self.startSpinBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.endLabel = QtGui.QLabel(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endLabel.sizePolicy().hasHeightForWidth())
        self.endLabel.setSizePolicy(sizePolicy)
        self.endLabel.setMinimumSize(QtCore.QSize(54, 20))
        self.endLabel.setMaximumSize(QtCore.QSize(54, 20))
        self.endLabel.setObjectName("endLabel")
        self.horizontalLayout_2.addWidget(self.endLabel)
        self.endSpinBox = QtGui.QSpinBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.endSpinBox.sizePolicy().hasHeightForWidth())
        self.endSpinBox.setSizePolicy(sizePolicy)
        self.endSpinBox.setMinimumSize(QtCore.QSize(50, 20))
        self.endSpinBox.setMaximumSize(QtCore.QSize(50, 20))
        self.endSpinBox.setMinimum(-1000000)
        self.endSpinBox.setMaximum(1000000)
        self.endSpinBox.setProperty("value", 0)
        self.endSpinBox.setObjectName("endSpinBox")
        self.horizontalLayout_2.addWidget(self.endSpinBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.bakePushButton = QtGui.QPushButton(self.widget)
        self.bakePushButton.setGeometry(QtCore.QRect(0, 30, 230, 30))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bakePushButton.sizePolicy().hasHeightForWidth())
        self.bakePushButton.setSizePolicy(sizePolicy)
        self.bakePushButton.setMinimumSize(QtCore.QSize(230, 30))
        self.bakePushButton.setMaximumSize(QtCore.QSize(230, 30))
        self.bakePushButton.setObjectName("bakePushButton")
        self.line_2 = QtGui.QFrame(self.widget)
        self.line_2.setGeometry(QtCore.QRect(0, 20, 231, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.retranslateUi(bakeDialog)
        QtCore.QMetaObject.connectSlotsByName(bakeDialog)

    def retranslateUi(self, bakeDialog):
        bakeDialog.setWindowTitle(QtGui.QApplication.translate("bakeDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.startLabel.setText(QtGui.QApplication.translate("bakeDialog", "StartFrame", None, QtGui.QApplication.UnicodeUTF8))
        self.endLabel.setText(QtGui.QApplication.translate("bakeDialog", "EndFrame", None, QtGui.QApplication.UnicodeUTF8))
        self.bakePushButton.setText(QtGui.QApplication.translate("bakeDialog", "Bake", None, QtGui.QApplication.UnicodeUTF8))



#mainUi and bake signal
class bakeCtrlsUI(QtGui.QDialog,Ui_bakeDialog):    
    def __init__(self,source,target, parent = mayaParent):
        super(bakeCtrlsUI, self).__init__(parent)
        self.setupUi(self)
        self.source = source
        self.target = target
        self.setWindowTitle('bakeCtrls')
        self.startFrame = cmds.playbackOptions(q=1,min =1)
        self.endFrame = cmds.playbackOptions(q=1,max =1)
        self.startSpinBox.setValue(self.startFrame)
        self.endSpinBox.setValue(self.endFrame)        
        self.connect(self.bakePushButton,QtCore.SIGNAL("clicked()"),self.bakeCtrlsDoit)
        
    def bakeCtrlsDoit(self):        
        startBFrame = self.startSpinBox.value()
        endBFrame = self.endSpinBox.value()
        
        if(self.startFrame != startBFrame):
            cmds.currentTime(startBFrame-1) 
            bstValue = list(((cmds.getAttr(self.target+".translate"))[0]))
            bstValue.extend(list(((cmds.getAttr(self.target+".rotate"))[0])))
            
            cmds.currentTime(startBFrame) 
            self.baker(startBFrame,endBFrame)
            cmds.currentTime(startBFrame-1)
                        
            attr = ['.tx','.ty','.tz','.rx','.ry','.rz']
            for i in range(0,6):
                cmds.setAttr((self.target+attr[i]),bstValue[i])
            
            cmds.setKeyframe(self.target)
            cmds.currentTime(self.startFrame)
            cmds.select(self.target)
        else:
            self.baker(startBFrame,endBFrame)  
             
      
        self.close()
        
    def baker(self,startBFrame,endBFrame):
        con = ApplyConstrain(self.source,self.target).pointOriCon(0)
        cmds.bakeResults(self.target, t=(startBFrame,endBFrame),at=['tx','ty','tz',"rx","ry","rz"], simulation=True )
        cmds.delete(con[0],con[1])       


