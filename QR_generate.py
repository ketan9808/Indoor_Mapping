# QR code generator
import qrcode

def generate_qr():
    qr = qrcode.QRCode(version = None,
                      error_correction = qrcode.constants.ERROR_CORRECT_M,
                      box_size = 10,
                      border = 2)
    data = input('Enter the data to be encoded:')
    qr.add_data(data)
    qr.make(fit = True)
    image = qr.make_image(fill_color = 'black', back_color = 'white')
    image.save('qr.png')
