import os

print(dir(os))  # dir(module) function gives all the methods and attributes that are in the module 

print(os.getcwd()) # to get current working directory

os.chdir('/home/akshay/pyt')  # to change the directory

print(os.getcwd())

print(os.listdir())  # lists the file in the current directory

# to make new folder within the current directory
os.chdir('/home/akshay')
os.mkdir('new_folder')
os.makedirs('new_folder_2/midfolder/infolder') # this method can make directories within directories but os.mkdir() can't
print(os.listdir())

os.rmdir('new_folder_2/midfolder/infolder') # will remove only the 'infolder'
os.rmdir('new_folder')
os.removedirs('new_folder_2/midfolder') # will delete the intermediate directories as well
os.mkdir('a.txt')
os.rename('a.txt','aaa.txt')

print(os.stat('simple.html')) # can be used with attributes like .st_size
print(os.stat('simple.html').st_size)

from datetime import datetime
mod_time=os.stat('simple.html').st_mtime
print(datetime.fromtimestamp(mod_time))

# to print the whole directory tree 
for dirpath,dirnames,filenames in os.walk('/home/akshay/pyt'):
 print('Current Path:',dirpath)
 print('Directories:',dirnames)
 print('Files:',filenames)
 print()

print(os.environ.get('HOME')) # prints the home directory i.e the environment
file_path=os.path.join(os.environ.get('HOME'),'test.txt')
print(file_path)

print(os.path.dirname('/tmp/abc/acd.txt')) # will print the directory name
print(os.path.basename('/tmp/abc/acd.txt')) # will print the basename
print(os.path.split('/tmp/abc/acd.txt')) # will print both the base and dir name

print(os.path.exists('/tmp/abc/acd.txt')) # to check the existence of a path
print(os.path.isfile('/tmp/abc/acd.txt')) # to check if it's a file
print(os.path.isdir('/tmp/abc/acd.txt')) # to check if it's a dir

print(os.path.splitext('/tmp/abc/acd.txt')) # splits the directory and the extension
print(dir(os.path))
 

