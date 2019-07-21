# QR code generator
import qrcode

def generate_qr(Version = None, Error_correction = qrcode.constants.ERROR_CORRECT_M,Box_size = 10, Border = 2):
    qr = qrcode.QRCode(version = Version,
                      error_correction = Error_correction,
                      box_size = 10,
                      border = 2)
    data = input('Enter the data to be encoded:')
    
    qr.add_data(data)
    qr.make(fit = True)
    image = qr.make_image(fill_color = 'black', back_color = 'white')
    image.save('qr.png')
