import os

MOD_FOLDER = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\GUILTY GEAR STRIVE\\RED\\Binaries\\Win64"
os.chdir(MOD_FOLDER)

TARGET_DIRECTORY = os.path.join(os.getcwd(), "disable")

TARGET_FILE = 'dwmapi.dll'

fldrs = os.listdir(os.getcwd())

if 'disable' in fldrs :
  print('should move back the file and delete the folder !')
  os.rename( os.path.join(TARGET_DIRECTORY, TARGET_FILE), os.path.join(os.getcwd(), TARGET_FILE) )
  os.rmdir(TARGET_DIRECTORY)
else :
  print('should create the folder then move the file in !')
  os.mkdir(TARGET_DIRECTORY)
  os.rename( os.path.join(os.getcwd(), TARGET_FILE), os.path.join(TARGET_DIRECTORY, TARGET_FILE) )
