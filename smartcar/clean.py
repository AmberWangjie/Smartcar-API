#rm db.sqlite3

#from path import path
import os
import sys

#DIRECTORY_V = /Users/AmberWang/smartcar/smartcar/vehicles
#DIRECTORY = vehicle
#d = path(DIRECTORY) 
#Replace DIRECTORY with your required directory
#num_files = len(d.files())

#print(num_files)

REMOVE_LIST = [ "vehicles/__pycache__",
                "vehicles/migrations",
                "smartcar/__pycache__"]
def remove(path):
    """
    Remove the file or directory
    """
    if os.path.isdir(path):
        try:
            os.rmdir(path)
        except OSError:
            print("Unable to remove folder: %s" % path)
    else:
        try:
            if os.path.exists(path):
                os.remove(path)
        except OSError:
            print("Unable to remove file: %s" % path)

def cleanup(path):
    """
    Removes files in the clean_list
    
    """
   # time_in_secs = time.time() - (number_of_days * 24 * 60 * 60)
    for root, dirs, files in os.walk(path, topdown=False):
        for file_ in files:
            full_path = os.path.join(root, file_)
           # stat = os.stat(full_path)
 
            # if stat.st_mtime <= time_in_secs:
            remove(full_path)
 
        if not os.listdir(root):
            remove(root)
 
#----------------------------------------------------------------------
if __name__ == "__main__":
   # path = int(sys.argv[1]), sys.argv[2]
    for path in REMOVE_LIST:
        cleanup(path)
    os.system("rm db.sqlite3")
    os.system("python3 manage.py makemigrations vehicles")
    os.system("python3 manage.py migrate")
