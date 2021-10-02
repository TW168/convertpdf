#%%
import os
from datetime import datetime
from pdf2image import convert_from_path
import tempfile
import pytesseract
from pytesseract import Output
import pandas as pd

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

# convert to png
init_time = datetime.now()

filename='/mnt/c/sampledocs/sample3.pdf'
save_dir = '/home/uux/convertpdf'
 
with tempfile.TemporaryDirectory() as path:
     images_from_path = convert_from_path(filename, output_folder=path, last_page=1, first_page =0)
 
base_filename  =  os.path.splitext(os.path.basename(filename))[0] + '.png'     
 
images=convert_from_path(filename)

for i, image in enumerate (images):
    fname= 'image'+str(i)+'.png'
    image.save(fname, 'PNG')
# end convert   

#%%

d = pytesseract.image_to_data('image4.png', output_type='data.frame')

# %%
# %%
# Convert MTD Shipment to int
str_mtdshipment=d.loc[110, 'text']
MTD_shipment = int(str_mtdshipment.replace(',', '') )

# %%
# Converting Mach 2 side blacklog to int
str_mach2sidebacklog=d.loc[154, 'text']
Mach2SideBacklog= int(str_mach2sidebacklog.replace(',',''))


# %%
lsi=[]




# def main():
#     pages = convert_from_path("presentation.pdf", first_page=2,
#                               single_file=True)
#     pages[0].save("test_pdf2image.jpg", quality=85)

# if __name__ == "__main__":
#     main()quit()
