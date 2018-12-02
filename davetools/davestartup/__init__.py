import sys
import maya.cmds as cmds




def start_up():
    print 'I will do everything for you  %s and I am from %s' % (__name__,__file__)
    sys.path.append('D:\dave\pythonWorkSpace\ARC\CORE')
    sys.path.append('D:\dave\git\CIGDave\CIGDave\CIGScripts')    
    sysPath()
    if cmds.commandPort(':7720',q=1) !=1:       
        cmds.commandPort(n=':7720',eo =0 ,nr=1)
    print 'I have connected eclips'
    
    




def sysPath():
    print 'sys.path:'
    paths  = sys.path
    for i in range(len(paths)):
        print '     ' + (paths[i])

