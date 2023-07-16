import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_Q,
    box_size=10,
    border=3,
)
qr.add_data('s.id/1QdGu')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode_medium_Q.png")