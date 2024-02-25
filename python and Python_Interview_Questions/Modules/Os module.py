#Os module

# Handling the Current Working Directory
# Creating a Directory
# Listing out Files and Directories with Python
# Deleting Directory or Files using Python

import os
cwd = os.getcwd()
print("Current working directory",cwd)



def current_path():
    print("Current working before")
    print(os.getcwd())
    print()
current_path()
os.chdir('../')
current_path()
print("Current working after",os.getcwd())

#Creating a Directory
import os
directory = "Lingababu"
parent_dir = "C:\\Users\\ASUS\\Desktop\\Programming"
path = os.path.join(parent_dir,directory)
print(path )
os.mkdir(f"Directory created {directory}")
mode = 0o666
path=os.path.join(parent_dir,directory)
os.mkdir(path,mode)
print(f'Directory created {directory}')

#Check whether the directory exists or not
import os
path = "C:\\Users\\ASUS\\Desktop\\Programming\\Lingababu"
if not os.path.exists(path):
    os.mkdir(path)
    print(f"Directory created: {path}")
else:
    print(f"Directory'{path}' already exists.")


#list the directories
import os
path = "C:\\Users\\ASUS\\Desktop\\Programming"
dir_list = os.listdir(path)
print("Files and directories in", path,":")
print(dir_list)