import qrcode
from PIL import Image

QR_Code=qrcode.make(input("Enter/Paste your url:"))

Image_Name=input("save your file with(put .png at the end of the name):")
QR_Code.save(Image_Name)

Saved_Image_URL="path of the file where you wanna save the created QR"%(Image_Name)

Image=Image.open(Saved_Image_URL)
Image.show()