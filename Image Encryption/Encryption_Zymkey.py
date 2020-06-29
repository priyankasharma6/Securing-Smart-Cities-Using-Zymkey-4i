import zymkey
import filecmp
import binascii

def hexEncrypt(imageFile, index):
    #encryption ofa hex img
    print(" Start encryption:")
    EncryptedFileName = "EncryptedImages/encrypted_file_" + str(index) + ".txt"
    zymkey.client.lock("TempFiles/imgHex_temp.txt", EncryptedFileName)
    with open (EncryptedFileName,'rb') as file:
        data = file.read()
        print("      Encrypted data:")
        print(data)
        with open("EncryptedImages/encryptedImg" + str(index) +".jpg", 'wb') as image_file:
            image_file.write(data)
        print("      Encryption done")
        print(" -----------------")

def decryption(imageFile,index):
    print(" Start decryption:")
    #decrypting an encrypted file back to an image.
    EncryptedFileName = "EncryptedImages/encrypted_file_" + str(index) + ".txt"
    zymkey.client.unlock(EncryptedFileName, "TempFiles/my_decrypted_file.txt")
    with open ('TempFiles/my_decrypted_file.txt','rb') as defile:
        print("      decrypted hex data:")
        data = defile.read()
        print(data)
        print("      convert back to binary:")
        data = binascii.a2b_hex(data)
        print(data)
        outputFileName = "DecryptedImages/output" + str(index) + ".jpg"
        with open(outputFileName, 'wb') as image_file:
            image_file.write(data)
        print("      Done decryption - Reverted back to original image - output file saved.")
        print("==================================\n")
