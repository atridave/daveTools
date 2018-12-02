import maya.cmds as cmds


def cut_meshes(mesh, pcx, pcy, pcz, rx, ry, rz, delete_source):

    meshes = MeshPolyCut(mesh, pcx, pcy, pcz, rx, ry, rz).generate_mesh
    if delete_source == 1:
        cmds.delete(mesh)
    return meshes


class MeshPolyCut:
    def __init__(self, mesh, pcx, pcy, pcz, rx, ry, rz):

        self.mesh = mesh
        self.pcx = pcx
        self.pcy = pcy
        self.pcz = pcz
        self.rx = rx
        self.ry = ry
        self.rz = rz
        self.rrx = self.rx-180
        self.leftMesh = None
        self.rightMesh = None

    def duplicate_mesh(self):
        self.leftMesh = cmds.duplicate(self.mesh, n=(self.mesh[0] + '_left'))
        self.rightMesh = cmds.duplicate(self.mesh, n=(self.mesh[0] + '_right'))

    @staticmethod
    def cut_mesh(obj, pcx, pcy, pcz, rx, ry, rz):
        cmds.polyCut(obj, pc=(pcx, pcy, pcz), ro=(rx, ry, rz), df=1, ef=1, eox=0.5, eoy=0.5, eoz=0.5, ps=(1, 1), ch=0)

    @property
    def generate_mesh(self):

        meshes = []
        self.duplicate_mesh()
        self.cut_mesh(self.leftMesh, self.pcx, self.pcy, self.pcz, self.rx, self.ry, self.rz)
        self.cut_mesh(self.rightMesh, self.pcx, self.pcy, self.pcz, self.rrx, self.ry, self.rz)
        meshes.append(self.leftMesh)
        meshes.append(self.rightMesh)
        return meshes
