# create normal and your own qr codes and encode /decode information from them .this project uses qrcode librar

import qrcode

# data we are gone encode imto qrcode
data = "let to do what world wanna to but never forget what u love to do"

img = qrcode.make(data)
img.save("C:\\Users\\Dhiraj\\Videos\\Python_Beginner_projects\\qrcode\\myqrcode.png")


