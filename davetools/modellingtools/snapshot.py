'''This function duplicates objets per frame and groups them'''

import maya.cmds as cmds
from animtools.anim_util import get_timerange
import core.core_util as cutil

def snapshot(object):
    frames = get_timerange()
    top_g = cutil.make_empty_group(object+'_meshes_g')
    for i in range(0,int(frames[2])):                
        mesh = cmds.duplicate(object, n=(object +'_'+ str(frames[0]+1)+'_geo'))
        cutil.parent_it(mesh,top_g)
        cmds.currentTime(cmds.currentTime(q=1)+1)

