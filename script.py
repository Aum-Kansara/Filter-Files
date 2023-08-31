import os

more_files_folder=input("Enter whole path of folder which contains More files :")
less_files_folder=input("Enter whole path of folder which contains Lore files :")
more_files_folder.replace('\\','/')
less_files_folder.replace('\\','/')
files=list(map(lambda x:x.split('.')[0],os.listdir(less_files_folder)))
current_path=os.getcwd()
extention=os.listdir(more_files_folder)[0].split('.')[1]
os.mkdir("Common Files")
os.mkdir("Uncommon Files")

for i in os.listdir(more_files_folder):
    for j in os.listdir(less_files_folder):
        os.chdir(more_files_folder)
        with open(i,'rb') as f1:
            if i.split('.')[0] in files:
                path=f"{current_path}/Common Files"
            else:
                path=f"{current_path}/Uncommon Files"
            os.chdir(path)
            with open(i,'wb') as f2:
                f2.write(f1.read())