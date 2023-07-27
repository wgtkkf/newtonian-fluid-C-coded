# removal of directory
# Coded by Takuro TOKUNAGA
# Created: June 07 2022

import numpy as np
import shutil
import glob
import os
import time

start = time.time()

def RemoveFile(DirectoryPath):

    # remove the followings
    # 1. .vtk files

    temp = os.listdir(DirectoryPath) # do not delete

    try:
        # remove .dat file
        for item in temp:
            if item.endswith(".vtk"):
                os.remove(os.path.join(DirectoryPath, item))

    except:
        print('Removal completion.')

# time display
elapsed_time = time.time()-start
#print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")
