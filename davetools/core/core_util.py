'''importing moduls'''
import math
import maya.cmds as cmds


def make_empty_group(name):
    cmds.select(cl=1)
    return cmds.group(em=1, n= name)

def get_selection():
    return cmds.ls(sl=1)

def get_hierarchy_type(obj, type = None):
    cmds.select(obj,hi=1)
    if type == None:
        return get_selection()
    else:
        return cmds.ls(sl=1, type=type)

def parent_it(childs, parent):
    for i in range(0,len(childs)):
        cmds.parent(childs[i], parent)

def get_parent(child):
    return cmds.listRelatives(child, p=1)

def append_it(taret):
    temp = []
    for i in range(0,len(taret)):
        temp.append(taret[i])
    return temp

def rename_it(name, newname):
    return cmds.rename(name, newname)

def get_shape(obj):
    return cmds.listRelatives(obj)[0]


def lock_hide(obj, tx, ty, tz, rx, ry, rz, sx, sy, sz, v, radi=None):
    attrval = [tx, ty, tz, rx, ry, rz, sx, sy, sz, v]
    attrs = ['.tx', '.ty', '.tz', '.rx', '.ry', '.rz', '.sx', '.sy', '.sz', '.v']

    for i in range(0, len(attrs)):
        if attrval[i] == 1:
            key = 0
        else:
            key = 1
        cmds.setAttr((obj+attrs[i]), l=attrval[i], k=key)

    if radi:
        cmds.setAttr(obj+'.radi', l=0, k=1)
        cmds.setAttr(obj+'.radi', l=1, k=0)