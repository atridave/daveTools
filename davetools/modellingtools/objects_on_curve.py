import maya.cmds as cmds

def joints_on_curve():
    sel = cmds.ls(sl=1,fl=1)
    parent = cmds.joint(n='curve_root_jnt')
    for i in range(0,len(sel)):
        cmds.select(sel[i])
        pos = cmds.pointPosition(sel[i])
        jnt = cmds.joint(p=(pos[0], pos[1], pos[2]), n=('Curve_'+str([i])+'_jnt'))
        cmds.parent(jnt,parent)
        parent = jnt

sel = cmds.ls(sl=1)

for i in range(0,len(sel)):
    sp = cmds.polySphere(r=0.7,n=sel[i]+'_sGeo')
    cmds.pointConstraint( sel[i], sp )
    cmds.orientConstraint( sel[i], sp )


