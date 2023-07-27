# Coded by Takuro TOKUNAGA
# Created: April 20 2022
# Update history
# Updated: June 07 2022 / August 02, 2022 / March 14, 2023 / June 09, 2023

import time
import sys
import glob
import os
from remove import RemoveFile            # import function, called in the main

def main():
    start = time.time()

    # specify your folder of .wrl files, this is referred in the external functions
    vtk_dir = r"C:\Users\Takuro\Documents\Dropbox\1stAccount\FluidFEMCode\fluid\fluid\shear\files"
    # removal of unnecessary directories/files
    RemoveFile(vtk_dir)

    # time display
    elapsed_time = time.time()-start
    print("elapsed_time:{:.2f}".format(elapsed_time) + "[sec]")

if __name__ == "__main__":
    main()
