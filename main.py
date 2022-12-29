import qrcode

input_data = input("Enter the string that want to make its qr code : ")
name = input("Enter the name of the file : ")
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(input_data)
qr.make(fit=True)
img = qr.make_image(fill='red', back_color='red')
img.save(name + '.png')