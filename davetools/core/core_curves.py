class CurveOperation:
    def __init__(self, curve):
        self.curve = curve

    def curvecvinfo(self):
        cvinfo = []
        degree = cmds.getAttr(self.curve+'.degree')
        spans = cmds.getAttr(self.curve+'.spans')
        cvs = degree+spans
        cvinfo.append(degree)
        cvinfo.append(cvs)
        return cvinfo
   
    def curveskinctrls(self,allc,name):
        self.ctrljoitns = []
        crv = self.curvecvinfo() 
        
        for i in range(0,crv[1]):
            cmds.select(cl=1)
            jnt_PV = cmds.getAttr(self.curve+'.cv[%d]' % i)
            jnt_P = jnt_PV[0]
            jnt = make_joint(name,jnt_P[0],jnt_P[1],jnt_P[2])
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
        
   


        #create joints on cv numbers needs to create joints

class CurveUtil:
    def __init__(self, obj):
        self.obj = obj
        self.curve = get_shape(self.obj)

    def shapescaler(self,sx,sy,sz):
        cmds.scale(sx, sy, sz, self.curve)

    def shaperename(self):
        self.curve = rename_it(self.curve, (self.obj+'Shape'))

    def shapecolor(self,color):
        cmds.setAttr(self.curve+'.overrideEnabled',1)
        cmds.setAttr(self.curve+'.overrideColor',color)

    def shapedesign(self, sx, sy, sz, color):
        self.shaperename()
        self.shapescaler(sx, sy, sz)
        self.shapecolor(color)
        cmds.makeIdentity(self.obj, apply=True, t=1, r=1, s=1)
        cmds.delete(self.curve, ch=1)

    def shapeparent(self, ctrljnt):
        cmds.parent(self.curve, ctrljnt, r=1, s=1)
        cmds.delete(self.obj)


class CtrlLib(object):
    def __init__(self, name):
        self.name = name

    def make_dummyshape(self):
        return cmds.curve(d=3, p=[(0, 0, 0)], k=[0, 0, 0], n=self.name)

    def make_cube(self):
        return cmds.curve(d=1, p=[(1, 1, 1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, -1), (1, 1, -1),
                                  (-1, 1, -1), (-1, 1, 1), (1, 1, 1), (1, -1, 1), (1, -1, -1), (-1, -1, -1),
                                  (-1, -1, 1), (1, -1, 1), (-1, -1, 1), (-1, 1, 1)],
                          k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], n=self.name)

    def make_circle(self, nx, ny, nz, redi):
        return cmds.circle(nr=(nx, ny, nz), r=redi, ch=0, n=self.name)[0]

    def make_fourarrow(self):
        return cmds.curve(d=1, p=[(0, 0, -1.98), (-0.495, 0, -1.32), (-0.165, 0, -1.32), (-0.165, 0, -0.165),
                                  (-1.32, 0, -0.165), (-1.32, 0, -0.495), (-1.98, 0, 0), (-1.32, 0, 0.495),
                                  (-1.32, 0, 0.165), (-0.165, 0, 0.165), (-0.165, 0, 1.32), (-0.495, 0, 1.32),
                                  (0, 0, 1.98), (0.495, 0, 1.32), (0.165, 0, 1.32), (0.165, 0, 0.165), (1.32, 0, 0.165),
                                  (1.32, 0, 0.495), (1.98, 0, 0), (1.32, 0, -0.495), (1.32, 0, -0.165),
                                  (0.165, 0, -0.165), (0.165, 0, -1.32), (0.495, 0, -1.32), (0, 0, -1.98)],
                          k=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
                          n=self.name)

    def make_hip(self, nx, ny, nz, redi):
        ctrl = cmds.circle(nr=(nx, ny, nz), r=redi, ch=1, n=self.name, s=12)[0]
        cmds.select(cl=1)
        for i in range(0, 12, 2):
            cmds.select((ctrl+'.cv[%d]') % i, tgl=1)
        cmds.scale(2, 2, 2)
        return ctrl

    def make_cog(self):
        ctrl = self.make_cube()
        CurveUtil(ctrl).shapescaler(1,0.25,1)
        cmds.select(ctrl+'.cv[0:2]', ctrl+'.cv[5:8]', ctrl+'.cv[15]')
        cmds.scale(.8, .8, .8)
        cmds.select(cl=1)
        return ctrl


class MakeCtrl(CtrlLib):
    def __init__(self, name, choice, sx, sy, sz, color, sp=None, spjnt=None, nx=None, ny=None, nz=None, redi=None):
        CtrlLib.__init__(self, name)
        self.choice = choice
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.color = color
        self.sp = sp
        self.spjnt = spjnt
        self.nx = nx
        self.ny = ny
        self.nz = nz
        self.redi = redi

        if self.choice == 0:
            self.make_dummyshape()
        elif self.choice == 1:
            self.make_circle(self.nx, self.ny, self.nz, self.redi)
        elif self.choice == 2:
            self.make_cube()
        elif self.choice == 3:
            self.make_fourarrow()
        elif self.choice == 4:
            self.make_hip(self.nx, self.ny, self.nz, self.redi)
        elif self.choice == 5:
            self.make_cog()

    def doit(self):
        CurveUtil(self.name).shapedesign(self.sx, self.sy, self.sz, self.color)
        if self.sp:
            cmds.parent(get_shape(self.name), self.spjnt, r=1, s=1)
            cmds.delete(self.name)
            CurveUtil(self.spjnt).shaperename()