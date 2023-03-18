#creating color qr code
import qrcode

def qrcode_generator(txt):
    qr=qrcode.QRCode(version=1,
                      error_correction=qrcode.ERROR_CORRECT_L,
                      box_size=10,
                      border=10)
    qr.add_data(txt)
    qr.make(fit=True)
    img= qr.make_image(fill_color='black',back_color='white')
    img.save("./image1.png")


inp =input("enter the data for which qrcode need to be generaated\n")
qrcode_generator(inp)