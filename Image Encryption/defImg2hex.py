from PIL import Image
import binascii

def image2hex(imageFile):
    byte_im = imageFile.read()
    print(" Binary data:")
    print(byte_im)
    
#convert binaey to hex
    hexstr = binascii.hexlify(byte_im)
    print(" Hex data:")
    print (hexstr)

#writing hex to a txt file
    txtFile = open ("TempFiles/imgHex_temp.txt", "wb")
    n = txtFile.write(hexstr)
    txtFile.close()

