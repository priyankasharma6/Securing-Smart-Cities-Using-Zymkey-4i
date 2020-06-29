import zymkey
import filecmp
import defImg2hex
import Encryption_Zymkey
from PIL import Image
import os

#how many images in this directory?
files = os.listdir("Images")
file_count=len(files)
print ("Number of files: " + str(file_count) + "\n")

#for each image
for i in range (0,file_count):
    with open ("Images/" + files[i], "rb") as imageFile:
        print(files[i])
        #Convert image to hex
        defImg2hex.image2hex(imageFile)
        #Encryot the image and save into EncryptedImages folder
        Encryption_Zymkey.hexEncrypt(imageFile, i)
        #Decrypt back to original image and save the result into DecryptedImages
        Encryption_Zymkey.decryption(imageFile, i)
    
