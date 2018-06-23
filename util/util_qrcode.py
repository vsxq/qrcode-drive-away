import qrcode
import os
from config import base_url

from PIL import Image
background_img = Image.open(r"static/img/qrcode_background.jpg")
def make_qrcode(tel,code,url=""):
    url = base_url+"/scan?code="
    file_name=hex(int(tel))
    img_path = r'static/img/{}.jpg'.format(file_name)
    if os.path.exists(img_path):
        pass
    else:

        qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=8,
                   border=0,
                   )
        qr.add_data(url+code)
        qr.make(fit=True)
        img = qr.make_image()
        img = img.resize((500, 500))


        
        box = (320,760)

        background_img.paste(img,box)
        
        
        background_img.save(r"static/img/{}.jpg".format(file_name))
    return file_name