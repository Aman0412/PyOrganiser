import os 
import shutil


os.chdir('\\Users\\amanp\\Downloads')

download_files = os.listdir()

for files in os.listdir():
    if files.endswith(".jpg") or files.endswith(".png") or files.endswith(".mp4") or files.endswith(".gif") or files.endswith(".jpeg"):
        pof = os.path.join(os.getcwd(),files)
        shutil.move(pof,"C:\\Users\\amanp\\Downloads\\PyOrganise\\Picture Files")
        print ("Moved: " + files)
        print ()
        
    elif files.endswith(".exe") or files.endswith(".zip"):
        pof2 = os.path.join(os.getcwd(),files)
        shutil.move(pof2,"C:\\Users\\amanp\\Downloads\\PyOrganise\\.exe and zip Files")
        print ("Moved: " + files)
        print ()

    elif files.endswith(".mp4") or files.endswith(".mov"):
        pof3 = os.path.join(os.getcwd(),files)
        shutil.move(pof3,"C:\\Users\\amanp\\Downloads\\PyOrganise\\Video files")
        print ("Moved: " + files)
        print ()


    elif files.endswith(".pdf") or files.endswith(".docx") or files.endswith(".doc") or files.endswith(".ppt") or files.endswith(".pptx") or files.endswith(".xls") or files.endswith(".xlsx") or files.endswith.(".csv"):
        pof3 = os.path.join(os.getcwd(),files)
        shutil.move(pof3,"C:\\Users\\amanp\\Downloads\\PyOrganise\\Microsoft Office files")
        print ("Moved: " + files)
        print ()
