import os



path ='f:\\starcitizen\\CryEngine\\Data\\Scripts\\Entities\\Items\\XML\\fps_weapons'
tempFile = 'D:\\dave\\git\\daveCIG\\daveCIG\\CIGWork\\cigWorkMain\\cigWorkMain\\testXml.mtl'
ext = '.xml'

def findAndWriteFiles(folder,ext):
    configfiles = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in files if f.endswith(ext)]

    for i in range(0,len(configfiles)):
        print configfiles[i]
        writeFile(configfiles[i],configfiles[i])


def writeFile(sFile,dFile):

    #open file
    dumpFile = (open(sFile,'r'))
    text =  dumpFile.readlines()
    dumpFile.close()

    #print sFile

    
    for i in range(0,len(text)):
        #print text[i]
        validOut =  (text[i].find('bpst_fps_gmni_l86.cdf'))     


        if (validOut) != -1:
            print "line is " , i
            text[i] = text[i].replace('bpst_fps_gmni_l86.cdf' ,'bpst_fps_gmni_LH86.cdf' )                      
            writrNewFile(dFile,text)


def writrNewFile(dFile,text):
     filew = open(dFile,'w')
     filew.writelines(text)
     filew.close()
     print "i have written %s file " % dFile


findAndWriteFiles(path,ext)




