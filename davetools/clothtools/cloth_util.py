'''Module for cloth utils '''

import maya.cmds as cmds
from core.core_kinematics import ApplyConstrain
import core.core_util as cutil

'''get nucleus'''

def get_nucleus():
    try:
        return cmds.ls(type = 'nucleus')[0]
    except :       
        return cutil.make_empty_group('clothSetup_g')      
    

def make_cloth_setup():
    cloth_root = get_nucleus()

    
