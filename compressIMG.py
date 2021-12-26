# Compress Image Size

import PIL
from PIL import Image
from tkinter.filedialog import * 

file_path = askopenfilename()           # Ask Image Path From User
img = PIL.Image.open(file_path)         # Set Image to Pillow Library
myHeight, myWidth = img.size            # Set Height and Width of Image

# Compress Image
img = img.resize((myHeight,myWidth) , PIL.Image.ANTIALIAS)      
save_path = asksaveasfilename()         # Ask Save Path for Image

img.save(save_path+"_compressed.JPG")   
print("Image Compressed Successfully !")