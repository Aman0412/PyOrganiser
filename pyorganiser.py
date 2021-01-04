import os 
import shutil


os.chdir('\\Users\\amanp\\Downloads')

download_files = os.listdir()


def clean(filetypes, path):
    for files in download_files:
        for f in filetypes:
            if files.endswith(f):
                pof = os.path.join(os.getcwd(),files)
                shutil.copy(pof, path)
                os.remove(files)
                print ("Moved: " + files)
                print ()

clean([".png","jpg", ".jpeg"], "C:\\Users\\amanp\\Downloads\\PyOrganise\\Picture files")
clean([".mp4", ".mov"], "C:\\Users\\amanp\\Downloads\\PyOrganise\\Picture files")
clean([".exe",".zip","tar.gz"], "C:\\Users\\amanp\\Downloads\\PyOrganise\\Picture files")
clean([".pdf",".doc",".docx",".ppt",".pptx","xls","xlsx",".csv"], "C:\\Users\\amanp\\Downloads\\PyOrganise\\Picture files")
