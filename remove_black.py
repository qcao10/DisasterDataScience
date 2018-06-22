from scipy import misc
import numpy as np
from PIL import Image
import os

delete_count = 0

for file in os.listdir():
    if file.endswith('.jpeg'):
        img = Image.open(file)
        #if black 
        if not img.getbbox():
            #remove .jpeg and .aux.xml
            os.remove(file)
            os.remove(file + '.aux.xml')
            delete_count += 1
            print('delete count: ', delete_count)
