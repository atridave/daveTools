'''
This script copy and rename files
Author : Atri Dave
Date : 1/10/2018
'''

import os,sys,shutil,stat,glob,distutils





def copyAndRenameFiles():
    
    #folder paths and creating temp folder for renaming 
    #path =  'f:\\starcitizen\\CryEngine\\Data\\Animations\\fps_weapons\\weapons_v7\\gmni\\pistols'
    #path =  'f:\\starcitizen\\CryEngine\\Data\\Animations\\Characters\\Human\\male_v7\\use'
    path =  'f:\\starcitizen\\CryEngine\\Data\\Objects\\fps_weapons\\weapons_v7\\klwe\\pistols'
    pathOut = os.path.abspath(os.path.join(path,".."))
    tempFolder =  'rename'
    tempfolderPath = os.path.join(pathOut,tempFolder)

    #coping contents of folder to new rename folder & deleting source folder 
    try:
        shutil.rmtree(tempfolderPath,onerror=onReadOnlyError)
    except:
        pass
    shutil.copytree(path,tempfolderPath)
        #shutil.rmtree(path,onerror=onReadOnlyError)
    #copyFolder = distutils.dir_util.copy_tree(path,tempfolderPath)



    #get all files and rename it 

    os.chdir(tempfolderPath)
    content =  glob.glob('*')
    files = [] 
    folders = []


    
    for i in range(0,len(content)):
        #print content[i]
        contentPath =  os.path.join(tempfolderPath,content[i])        
        if(os.path.isdir(contentPath)):
            #os.chdir(contentPath)
            #innerFiles = glob.glob('*')
            #for j in range(0,len(innerFiles)):
            #    innerFilesPath =  os.path.join(contentPath,innerFiles)
            #    os.renames(innerFilesPath,(innerFilesPath).replace('_l86','LH86'))
            print 'foldes found '
            
        else:
            files.append(contentPath)
            os.rename(contentPath,(contentPath).replace('_l86','_lh86'))

    for i in range(0,len(folders)):
        os.chdir(folders[i])
        inContent = glob.glob('*')
        for j in range(0,len(inContent)):
            inContentPath =  os.path.join(folders[i],inContent[j])
            files.append(inContentPath)

        #for j in range(0,len(content)):
        #    contentPath =  os.path.join(folders,content[i])
        #    if(os.path.isfile(contentPath)):
        #        files.append(contentPath)
        


        
    #print 'I found foulders %s' % folders
    #print 'I found files %s' % files

    #for i in range(0,len(files)):
    #    #print files[i]
    #    oldStr =  str(files[i]).find('_l86')
    #    if(oldStr) != -1:
    #        newName = str(files[i]).replace('_l86','LH86')
    #        #print newName
    #        os.rename(file[i],newName)
    #        #print 'Found file %s' % files[i]
        
          
            
        
       
    

 #for removing readOnly files which works with suthil.rmtree 
def onReadOnlyError(func,path,exe_info):
     os.chmod(path,stat.S_IWRITE)
     os.unlink(path)
     



    
    #content =  os.listdir(path)
    #files =  []
    #folders = []
    #for i in range(0,len(content)):
    #    fullFilename = os.path.join(path,content[i])
    #    if(os.path.isfile(fullFilename)):
    #        print 'I am file %s' % content[i]
            
    #        tempName =  str(content[i]).replace(content[i],('__'+content[i]))
    #        shutil.copy(fullFilename,(path+tempName))
    #        print tempName
    #    if(os.path.isdir(os.path.join(path,content[i]))):
    #        print 'I am dir %s' % content[i]




def renameFiles():
    #path =  'f:\\starcitizen\\CryEngine\\Data\\Animations\\Characters\\Human\\male_v7\\rename'
    #path =  'f:\\starcitizen\\CryEngine\\Data\\Animations\\fps_weapons\\weapons_v7\\gmni\\rename'
    path =  'f:\\starcitizen\\CryEngine\\Data\\Objects\\fps_weapons\\weapons_v7\\klwe\\rename'
    files =  os.listdir(path)
    
    for i in range(0,len(files)):
        filePaths =  os.path.join(path,files[i])
        os.rename(filePaths,filePaths.replace('lpst_fps_klwe_arclightnew','lpst_fps_klwe_arclight'))       
        
        

def changeMode():
    #path =  'f:\\starcitizen\\CryEngine\\Data\\Animations\\Characters\\Human\\male_v7\\rename'
    path =  'f:\\starcitizen\\CryEngine\\Data\\Objects\\fps_weapons\\weapons_v7\\klwe\\rename'
    #path =  'f:\\starcitizen\\CryEngine\\Data\\Animations\\fps_weapons\\weapons_v7\\gmni\\rename'
    files =  os.listdir(path)
    for i in range(0,len(files)):
        filePaths =  os.path.join(path,files[i])
        print filePaths
        os.chmod(filePaths,stat.S_IWRITE)




if __name__ == '__main__':
    copyAndRenameFiles()
    renameFiles()
    changeMode()

