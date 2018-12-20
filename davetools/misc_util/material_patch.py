import os



path ='s'
tempFile = ''
ext = '.mtl'

def findAndWriteFiles(folder,ext):
    configfiles = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in files if f.endswith(ext)]

    for i in range(0,len(configfiles)):
        #print configfiles[i]
        writeFile(configfiles[i],configfiles[i])






def writeFile(sFile,dFile):

    #open file
    dumpFile = (open(sFile,'r'))
    text =  dumpFile.readlines()
    dumpFile.close()

    #print sFile

    
    for i in range(0,len(text)):
        #print text[i]
        validOut =  (text[i].find('Shader="NoDraw"'))
        valid =  (text[i].find('Shader="Nodraw"'))
        proxy =  (text[i].find('Name="proxy"'))
        Proxy =  (text[i].find('Name="Proxy"'))
        PROXY_mat =  (text[i].find('Name="PROXY_mat"'))
        proxy_mat = (text[i].find('Name="proxy_mat"'))
        Proxy_mat = (text[i].find('Name="Proxy_mat"'))


        if (proxy) != -1:
            print "line is " , i
            text[i] = text[i].replace('Shader="Illum"' ,'Shader="Nodraw"' )
            text[i] = text[i].replace('SurfaceType=""' ,'SurfaceType="mat_nodraw"' )            
            writrNewFile(dFile,text)

        if (Proxy) != -1:
            print "line is " , i
            text[i] = text[i].replace('Name="Proxy"' ,'Name="proxy"' )
            text[i] = text[i].replace('Shader="Illum"' ,'Shader="Nodraw"' )
            text[i] = text[i].replace('SurfaceType=""' ,'SurfaceType="mat_nodraw"' )            
            writrNewFile(dFile,text)

        if (PROXY_mat) != -1:
            print "line is " , i
            text[i] = text[i].replace('Name="PROXY_mat"' ,'Name="proxy"' )
            text[i] = text[i].replace('Shader="Illum"' ,'Shader="Nodraw"' )
            text[i] = text[i].replace('SurfaceType=""' ,'SurfaceType="mat_nodraw"' )            
            writrNewFile(dFile,text)

        if (proxy_mat) != -1:
            print "line is " , i
            text[i] = text[i].replace('Name="proxy_mat"' ,'Name="proxy"' )
            text[i] = text[i].replace('Shader="Illum"' ,'Shader="Nodraw"' )
            text[i] = text[i].replace('SurfaceType=""' ,'SurfaceType="mat_nodraw"' )            
            writrNewFile(dFile,text)

        if (Proxy_mat) != -1:
            print "line is " , i
            text[i] = text[i].replace('Name="Proxy_mat"' ,'Name="proxy"' )
            text[i] = text[i].replace('Shader="Illum"' ,'Shader="Nodraw"' )
            text[i] = text[i].replace('SurfaceType=""' ,'SurfaceType="mat_nodraw"' )            
            writrNewFile(dFile,text)



        if (validOut) != -1:
            print "line is " , i
            text[i] = text[i].replace('Shader="NoDraw"' ,'Shader="Nodraw"' )
            text[i] = text[i].replace('SurfaceType=""' ,'SurfaceType="mat_nodraw"' )
            writrNewFile(dFile,text)


        if (valid) != -1:
            print "line is " , i
            text[i] = text[i].replace('SurfaceType=""' ,'SurfaceType="mat_nodraw"' )
            writrNewFile(dFile,text)





def writrNewFile(dFile,text):
     filew = open(dFile,'w')
     filew.writelines(text)
     filew.close()
     print "i have written %s file " % dFile


findAndWriteFiles(path,ext)



