"""
 decode the qrcode data ..! if u get the error like 'module not found' , the download vcredist_x64.exe (Visual C++
 Redistributable Packages for Visual Studio 2013) ..!
 
"""
from pyzbar.pyzbar import decode
from PIL  import Image

img = Image.open("C:\\Users\\Dhiraj\\Videos\\Python_Beginner_projects\\qrcode\\myqrcode.png")

result = decode(img)

print(result)








