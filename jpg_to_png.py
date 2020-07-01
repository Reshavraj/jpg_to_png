'''
Created on 01-Jul-2020

@author: resha
'''
import sys
import os
from PIL import Image

'''Our steps towards Goal'''
#grab first and second argument
#check is new(output folder) exists, if not create
#loop through input 
#convert images to png
#save to the new folder


#1)grab first and second argument
image_folder= sys.argv[1]
output_folder= sys.argv[2]

#print(image_folder,output_folder)


#2)check is new(output folder) exists, if not create
if not os.path.exists(output_folder):
    os.makedirs(output_folder)


#3)loop through input 
for filename in os.listdir(image_folder):
    img= Image.open(f'{image_folder}{filename}')
    #4)convert images to png
    clean_name = os.path.splitext(filename)[0]
    #print(clean_name)
    #5)save to the new folder
    img.save(f'{output_folder}{clean_name}.png','png')
    print('All done.!!')
    
  
    
    
    
    
    
    
