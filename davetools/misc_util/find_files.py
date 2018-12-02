import os
import logging 
import webbrowser

logfile =  ((__file__).replace('.py','.log'))
try:
    os.remove(logfile)
except:
    pass

logging.basicConfig(filename= logfile,level=logging.DEBUG)  

path ='f:\\starcitizen\\CryEngine\\Data'
#tempFile = 'D:\\dave\\git\\daveCIG\\daveCIG\\CIGWork\\cigWorkMain\\cigWorkMain\\testXml.mtl'
ext = '.xml'

def findAndCheckFiles(folder,ext):
    configfiles = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in files if f.endswith(ext)]

    for i in range(0,len(configfiles)):
        #print configfiles[i]
        checkFile(configfiles[i],configfiles[i])
        #print("i have chacked %d files" % i)
        



def checkFile(sFile,dFile):

    #open file
    dumpFile = (open(sFile,'r'))
    text =  dumpFile.readlines()
    dumpFile.close()

    #print sFile
    for i in range(0,len(text)):
        #print text[i]
        found =  (text[i].find('lpst_fps_klwe_arclight.cdf'))

        if (found) != -1:
            #print 'file is', sFile,  "and it is in line ::: " , i+1
            logging.info('  file is %s and it is in line :::::  %d', sFile, i+1)

        found2 =  (text[i].find('behr_p4sc.cdf'))

        if (found2) != -1:
            print 'file is', sFile,  "and it is in line ::: " , i+1





findAndCheckFiles(path,ext)
webbrowser.open(logfile)

