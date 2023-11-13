import os
import shutil

destpath = "D:/Downloads"
sourcepath = "D:/Desktop/Coding/Python/P102/Doc_files/"
allfiles = os.listdir(sourcepath)
for filename in allfiles:
    name, ext = os.path.splitext(filename)
    #print(name+ "\n" + ext)
    if ext=="":
        continue
    if ext in ['.txt', '.doc', '.docx', '.pdf']:
        path1 = sourcepath + '/' + filename
        path2 = destpath + '/' + "Doc_files"
        path3 = path2 + '/' + filename
        if os.path.exists(path2):
            print("Moving "+ filename + "...........")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving " + filename + ".......")
            shutil.move(path1,path3)
    
