'''joint operations '''


def make_joint(name,x,y,z):
    return cmds.joint(p=(x, y, z),n = self.name) 

def distance_info(parent,child):
        parent_Val =  cmds.xform(parent,q=1,t=1,ws =1)
        child_val = cmds.xform(child,q=1,t=1,ws =1)
        self.distance = math.sqrt( (child_val[0]-parent_Val[0])*(child_val[0]-parent_Val[0])+ (child_val[1]-parent_Val[1])*(child_val[1]-parent_Val[1])+ (child_val[2]-parent_Val[2])*(child_val[2]-parent_Val[2]))
        return self.distance

class JointOperation(object):

    def __init__(self,name):
        self.name =  name
    
    def joints_info(self,all_jnt):
        self.sted = []        
        get_selection()
        self.all_joints = get_hierarchy_type(get_selection(),typ = 'joint')
        self.sted.append(self.all_joints[0])
        self.sted.append(self.all_joints[-1])        
        
        if all_jnt == 1:
            return self.all_joints
        else:
            return self.sted
      
    
    def joint_length_info(self,joint,jnt_count = None):
        length = 0
        self.jntCount = jnt_count
        jntChain = self.joints_info(joint,1)
        
        if (self.jntCount == None):
            self.jntCount  = len(jntChain)   
        
        for i in range(0,self.jntCount):
            dis = distance_info(jntChain[i], jntChain[i+1])
            length += dis
        return length   

    def joint_recreate(self,joint):
        prifix = 'new_'
        cmds.select(cl=1)
        self.newJnt  =  self.make_joint(prifix+joint)
        aa =  ApplyConstrain(joint,self.newJnt).pointOriCon(0)
        cmds.delete(aa[0],aa[1])
        cmds.makeIdentity( apply=True, t=1, r=1, s=1)        
        
    def joint_create_ctrl(self,xval,yval,zval):
        self.jnt = cmds.joint(p=(xval,yval,zval))
        return self.jnt
    
    def joint_make_duplicate_chain(self,SourceJoint,name,suffix):
        dJoints =  []
        joints =  cmds.duplicate(SourceJoint,n = (name+suffix),rc=1)
        dJoints.append(joints[0])
        for i in range(1,len(joints)):
            nameName =  (joints[i].strip((joints[i][-1])))
            newJntName = cmds.rename(joints[i],(nameName+suffix))
            dJoints.append(newJntName)
        return dJoints