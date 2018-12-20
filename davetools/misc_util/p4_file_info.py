import sys,os,glob,json
import P4

folder =  ''
basePath = ('/CryEngine'+(folder.split('CryEngine',1)[1]))


#os.system('explorer')
#os.startfile(folder)
#os.chdir(folder)
#icafs = glob.glob('*.i_caf')
##print(icafs)

#animSettings = glob.glob('*.animsettings')
##print(animSettings)

#print(len(animSettings)) 
##for file in glob.glob('*.i_caf'):
##    print(file) 


def P4s():
    p4 = P4Util()
    return p4

def openExportFiles(folder):
    os.chdir(folder)
    icafs = glob.glob('*.i_caf')
    animSettings = glob.glob('*.animsettings')
    p4 = P4s()

    for i in range(0,len(animSettings)):
        fileType =  checkfile(animSettings[i])
        if fileType == 'json':
            jfile =  json.loads(open(animSettings[i]).read())
            mayaFile = (jfile['info']['mayafile'])
            mayaFileS =  ('/CryEngine'+(mayaFile.split('CryEngine',1)[1]))            
            sFile = (p4.streamGetter()+mayaFileS)
            print sFile
            p4.checkOutfile('edit', sFile)
            #os.startfile(mayaFile)
    sys.exit()

def checkfile(inputFile):
    with open(inputFile) as unknownFile:
        ck = unknownFile.read(1)
        if ck != '<':
            return 'json'
        return 'XML'



class P4Util:
    
    def __init__(self):
        self.p4 = P4.P4()
        self.p4.connect()
        self.info = self.p4.run_info()
               
    def rootGetter(self):        
        return self.info[0]['clientRoot']
    
    def streamGetter(self):
        return self.info[0]['clientStream']      
        
    def checkOutfile(self,command,fullPath):
        try:
            self.p4.run('sync',"-f",fullPath)
            self.p4.run(command,"-f",fullPath)
        except:
            pass


openExportFiles(folder)
