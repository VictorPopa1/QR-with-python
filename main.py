import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

link = "https://po`ligondetircluj.ro/"
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data('https://poligondetircluj.ro/')
#imgQR = qrcode.make(link)
qr.version = 5
qr.box_size = 40
qr.border = 2
qr.make(fit=True)
#qr.box_size =
img = qr.make_image(image_factory=StyledPilImage, embeded_image_path = r'C:\Users\Victor\Desktop\CSC logo strong.png')

print(type(img))

img.save("Poligon2.jpg")