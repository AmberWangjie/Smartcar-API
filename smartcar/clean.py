import os
import sys

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
    Removes cache files and old migrations in the clean_list
    
    """
    for root, dirs, files in os.walk(path, topdown=False):
        for file_ in files:
            full_path = os.path.join(root, file_)
            remove(full_path)
 
        if not os.listdir(root):
            remove(root)
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    for path in REMOVE_LIST:
        cleanup(path)
    """ remove database tables and migrate the new schema """
    os.system("rm db.sqlite3")
    os.system("python3 manage.py makemigrations vehicles")
    os.system("python3 manage.py migrate")
